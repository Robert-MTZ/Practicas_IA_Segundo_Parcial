# Practica_092_Generacion_de_Mapas_SLAM_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Generacion_de_Mapas_SLAM

import g2o
import numpy as np
import matplotlib.pyplot as plt

# Definimos la función para generar datos de prueba
def generar_datos_test(num_poses, num_landmarks, ruido_obs=0.1, ruido_odom=0.1):
    poses_verdaderas = [np.array([0.0, 0.0])]
    landmarks_verdaderos = [np.array([5.0, 5.0])]
    odometria = []

    # Generamos posiciones verdaderas y odometría
    for i in range(1, num_poses):
        nueva_pose = poses_verdaderas[-1] + np.random.normal(scale=ruido_odom, size=2)
        poses_verdaderas.append(nueva_pose)
        odometria.append(g2o.EdgeSE2(g2o.SE2(nueva_pose[0], nueva_pose[1], 0.0), g2o.SE2(poses_verdaderas[-2][0], poses_verdaderas[-2][1], 0.0), [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]))
    
    # Generamos landmarks verdaderos y observaciones
    for i in range(num_landmarks):
        landmark = np.random.rand(2) * 10
        landmarks_verdaderos.append(landmark)
        for pose_idx in range(1, num_poses):
            if np.random.rand() > 0.8:  # Simulamos observaciones con cierta probabilidad
                observacion = g2o.EdgeSE2PointXY()
                observacion.set_vertex(0, odometria[pose_idx - 1])
                observacion.set_vertex(1, landmark)
                observacion.set_measurement(landmark - poses_verdaderas[pose_idx])
                observacion.set_information(np.eye(2) / ruido_obs)
                odometria[pose_idx - 1].add_edge(observacion)
    
    return poses_verdaderas, landmarks_verdaderos, odometria

# Generamos datos de prueba
poses_verdaderas, landmarks_verdaderos, odometria = generar_datos_test(50, 20)

# Inicializamos el optimizador
optimizador = g2o.SparseOptimizer()

# Creamos vértices para las poses
for i, pose in enumerate(poses_verdaderas):
    v_se2 = g2o.VertexSE2()
    v_se2.set_id(i * 2)
    v_se2.set_estimate(g2o.SE2(pose[0], pose[1], 0.0))
    if i == 0:  # Fijamos la primera pose
        v_se2.set_fixed(True)
    optimizador.add_vertex(v_se2)

# Creamos vértices para los landmarks
for i, landmark in enumerate(landmarks_verdaderos):
    v_punto = g2o.VertexPointXY()
    v_punto.set_id(i * 2 + 1)
    v_punto.set_estimate(landmark)
    optimizador.add_vertex(v_punto)

# Añadimos las relaciones de odometría al optimizador
for edge in odometria:
    optimizador.add_edge(edge)

# Optimizamos el grafo
optimizador.initialize_optimization()
optimizador.optimize(10)

# Recuperamos las poses estimadas
poses_estimadas = []
for i in range(len(poses_verdaderas)):
    pose_vertex = optimizador.vertex(i * 2)
    poses_estimadas.append([pose_vertex.estimate().translation().x(), pose_vertex.estimate().translation().y()])

# Recuperamos los landmarks estimados
landmarks_estimados = []
for i in range(len(landmarks_verdaderos)):
    landmark_vertex = optimizador.vertex(i * 2 + 1)
    landmarks_estimados.append(landmark_vertex.estimate())

# Visualizamos el mapa
plt.figure(figsize=(8, 6))
plt.plot([pose[0] for pose in poses_verdaderas], [pose[1] for pose in poses_verdaderas], 'r--', label='Poses Verdaderas')
plt.plot([pose[0] for pose in poses_estimadas], [pose[1] for pose in poses_estimadas], 'b-', label='Poses Estimadas')
plt.scatter([landmark[0] for landmark in landmarks_verdaderos], [landmark[1] for landmark in landmarks_verdaderos], c='g', marker='o', label='Landmarks Verdaderos')
plt.scatter([landmark[0] for landmark in landmarks_estimados], [landmark[1] for landmark in landmarks_estimados], c='b', marker='x', label='Landmarks Estimados')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('SLAM con g2o')
plt.legend()
plt.grid(True)
plt.show()
