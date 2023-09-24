import unittest
import numpy as np
from canicasBooleanas import canicas_booleanas, rendijas_clasico_probabilistico, rendijas_cuantico, graficar_probabilidades

class TestExperimentos(unittest.TestCase):

    def test_canicas_booleanas(self):
        matriz_probabilidades = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
        estado_inicial = np.array([1, 0, 0])
        resultado = canicas_booleanas(matriz_probabilidades, estado_inicial)
        resultado_esperado = np.array([0, 1, 0])
        np.testing.assert_array_equal(resultado, resultado_esperado)

    def test_rendijas_clasico_probabilistico(self):
        matriz_transicion = np.array([[0.5, 0.25, 0.25], [0.25, 0.5, 0.25], [0.25, 0.25, 0.5]])
        estado_inicial = np.array([1, 0, 0])
        num_pasos = 3
        resultado = rendijas_clasico_probabilistico(matriz_transicion, estado_inicial, num_pasos)
        resultado_esperado = np.array([0.4375, 0.375, 0.1875])
        np.testing.assert_allclose(resultado, resultado_esperado, atol=1e-6)

    def test_rendijas_cuantico(self):
        matriz_transicion = np.array([[0.5, 0.25, 0.25], [0.25, 0.5, 0.25], [0.25, 0.25, 0.5]])
        estado_inicial = np.array([1, 0, 0])
        resultado = rendijas_cuantico(matriz_transicion, estado_inicial)
        resultado_esperado = np.array([0.5, 0.25, 0.25])
        np.testing.assert_allclose(resultado, resultado_esperado, atol=1e-6)

    def test_graficar_probabilidades(self):
        vector_estado = np.array([0.5, 0.25, 0.25])
        nombres_estados = ['Estado 1', 'Estado 2', 'Estado 3']
        titulo = 'Prueba de Gráficos'
        nombre_archivo = 'prueba_grafico.png'

        # Ejecuta la función de gráficos y verifica que no haya errores
        try:
            graficar_probabilidades(vector_estado, nombres_estados, titulo, nombre_archivo)
        except Exception as e:
            self.fail(f"La función de gráficos generó un error: {e}")

if __name__ == '__main__':
    unittest.main()
