## Autor
Este código fue escrito por Raquel Iveth Selma.

# Experimentos Probabilísticos y Cuánticos
Este repositorio contiene un conjunto de funciones y pruebas en Python relacionadas con experimentos probabilísticos y cuánticos. Los experimentos incluyen las siguientes funcionalidades:

## 1. Experimento de Canicas Booleanas
- Función: canicas_booleanas(matriz_probabilidades, estado_inicial)
- Descripción: Realiza un experimento de canicas booleanas multiplicando una matriz de probabilidades por un estado inicial.

## 2. Experimento de Rendijas Clásico Probabilístico
- Función: rendijas_clasico_probabilistico(matriz_transicion, estado_inicial, num_pasos)
- Descripción: Simula un experimento de múltiples rendijas con comportamiento clásico probabilístico. Calcula el estado resultante después de un número dado de pasos.

## 3. Experimento de Rendijas Cuántico
- Función: rendijas_cuantico(matriz_transicion, estado_inicial)
- Descripción: Simula un experimento de múltiples rendijas con comportamiento cuántico. Calcula el estado resultante.

## 4. Función para Graficar Probabilidades
- Función: graficar_probabilidades(vector_estado, nombres_estados, titulo, nombre_archivo)
- Descripción: Crea un gráfico de barras que muestra las probabilidades en un vector de estados y lo guarda en un archivo de imagen.

## Ejecución de Pruebas
El repositorio también incluye un conjunto de pruebas unitarias para las funciones mencionadas. Estas pruebas están definidas en el archivo test.py y se pueden ejecutar utilizando el módulo unittest de Python. Las pruebas verifican que las funciones se comporten como se espera y produzcan resultados correctos.

Para ejecutar las pruebas, puedes utilizar el siguiente comando en la línea de comandos:

bash
Copy code
python -m unittest test
Asegúrate de que las dependencias, como numpy y matplotlib, estén instaladas en tu entorno de Python antes de ejecutar las pruebas.

## Dependencias
Este código utiliza las siguientes dependencias:

- numpy: Para realizar cálculos matriciales.
- matplotlib: Para crear gráficos y visualizaciones.
Asegúrate de que estas dependencias estén instaladas en tu entorno de Python antes de ejecutar el código.

