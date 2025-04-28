import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generar_rorschach_3d(ancho=50, alto=50, profundidad=50, simetria='x'):
    """
    Genera un patrón 3D con efecto Rorschach aplicando simetría en el eje especificado.

    Parámetros:
    - ancho: Número de divisiones en el eje X.
    - alto: Número de divisiones en el eje Y.
    - profundidad: Número de divisiones en el eje Z.
    - simetria: Eje de simetría ('x', 'y', 'z').

    Retorna:
    - x, y, z: Coordenadas 3D.
    - valores: Valores de intensidad para los puntos.
    """
    # Crear un espacio tridimensional con valores aleatorios
    x = np.linspace(-1, 1, ancho)
    y = np.linspace(-1, 1, alto)
    z = np.linspace(-1, 1, profundidad)
    x, y, z = np.meshgrid(x, y, z)
    
    # Generar una función aleatoria para crear patrones
    valores = np.sin(10 * (x**2 + y**2 + z**2)) + np.random.rand(*x.shape) * 0.5
    
    # Aplicar simetría tipo espejo
    if simetria == 'x':
        valores = (valores + valores[::-1, :, :]) / 2
    elif simetria == 'y':
        valores = (valores + valores[:, ::-1, :]) / 2
    elif simetria == 'z':
        valores = (valores + valores[:, :, ::-1]) / 2
    else:
        raise ValueError("El parámetro 'simetria' debe ser 'x', 'y' o 'z'.")
    
    return x, y, z, valores

# Configuración inicial
x, y, z, valores = generar_rorschach_3d(ancho=50, alto=50, profundidad=50, simetria='x')

# Crear la figura 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Crear el gráfico de puntos 3D
puntos = ax.scatter(x, y, z, c=valores.flatten(), cmap='viridis', alpha=0.7)

# Agregar una barra de color para visualizar la intensidad
fig.colorbar(puntos, ax=ax, shrink=0.5, aspect=10)

# Configurar los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Mostrar la figura
plt.show()