import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def generar_imagen_abstracta(ancho=800, alto=800, colores=5):
    # Crear un lienzo con valores aleatorios
    lienzo = np.random.rand(alto, ancho, 3)
    
    # Generar patrones abstractos
    for _ in range(colores):
        x = np.random.randint(0, ancho)
        y = np.random.randint(0, alto)
        radio = np.random.randint(50, 200)
        color = np.random.rand(3)
        
        for i in range(alto):
            for j in range(ancho):
                distancia = np.sqrt((i - y)**2 + (j - x)**2)
                if distancia < radio:
                    lienzo[i, j] = (lienzo[i, j] + color) / 2

    # Normalizar valores para asegurarse de que estén entre 0 y 1
    lienzo = np.clip(lienzo, 0, 1)
    
    # Mostrar y guardar la imagen
    plt.imshow(lienzo)
    plt.axis('off')
    plt.savefig("imagen_abstracta.png", dpi=300, bbox_inches='tight', pad_inches=0)
    plt.show()

# Llamar a la función para generar la imagen
try:
    generar_imagen_abstracta()
except Exception as e:
    print(f"Error: {e}")