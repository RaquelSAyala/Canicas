import numpy as np
import matplotlib.pyplot as plt


def canicas_booleanas(matriz_probabilidades, estado_inicial):
    resultado = np.dot(matriz_probabilidades, estado_inicial)
    return resultado

def rendijas_clasico_probabilistico(matriz_transicion, estado_inicial, num_pasos):
    estado_actual = estado_inicial
    for _ in range(num_pasos):
        estado_actual = np.dot(matriz_transicion, estado_actual)
    return estado_actual

def rendijas_cuantico(matriz_transicion, estado_inicial):
    resultado = np.dot(matriz_transicion, estado_inicial)
    return resultado

def graficar_probabilidades(vector_estado, nombres_estados, titulo, nombre_archivo):
    plt.bar(range(len(vector_estado)), vector_estado)
    plt.xticks(range(len(vector_estado)), nombres_estados)
    plt.xlabel('Estados')
    plt.ylabel('Probabilidad')
    plt.title(titulo)
    plt.savefig(nombre_archivo)
    plt.show()
