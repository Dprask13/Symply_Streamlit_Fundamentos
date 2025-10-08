# Teoría de SymPy para Ingeniería

## Visión general de SymPy
SymPy es una biblioteca de Python dedicada al cálculo simbólico. Permite manipular expresiones matemáticas de forma exacta, facilitando la resolución de problemas complejos en ingeniería y ciencias aplicadas.

## Álgebra simbólica
SymPy permite definir variables simbólicas y operar con ellas para simplificar, expandir y factorizar expresiones algebraicas. Ejemplo conceptual:

```pseudo
Definir variables simbólicas x, y
Expandir (x + y)^2
Simplificar expresión racional
```

## Cálculo: derivadas e integrales
La biblioteca facilita el cálculo de derivadas e integrales de funciones simbólicas, tanto simples como compuestas.

```pseudo
Derivar f(x) respecto a x
Integrar f(x) respecto a x
Calcular derivada parcial de f(x, y) respecto a y
```

## Ecuaciones algebraicas y diferenciales
SymPy resuelve ecuaciones algebraicas y sistemas de ecuaciones, así como ecuaciones diferenciales ordinarias.

```pseudo
Resolver ecuación cuadrática en x
Resolver sistema de ecuaciones lineales
Resolver ecuación diferencial de primer orden
```

## Matrices
Permite trabajar con matrices simbólicas: operaciones, determinantes, inversas y autovalores.

```pseudo
Definir matriz simbólica A
Calcular determinante de A
Encontrar autovalores de A
```

## Unidades y constantes
SymPy incluye módulos para manejar unidades físicas y constantes universales, útiles en aplicaciones de ingeniería.

```pseudo
Asignar unidades a variables
Utilizar constante de gravitación universal
```

## Buenas prácticas
- Definir variables simbólicas con nombres claros.
- Documentar cada paso matemático.
- Validar resultados simbólicos antes de usarlos en cálculos numéricos.
- Integrar SymPy con Streamlit para visualización interactiva.

## Ejemplos conceptuales para Streamlit
- Mostrar la simplificación de una expresión ingresada por el usuario.
- Visualizar la derivada de una función simbólica en un gráfico.
- Resolver y mostrar el paso a paso de una ecuación diferencial.
- Presentar matrices y sus propiedades de forma interactiva.

> Este documento sirve como referencia teórica para el desarrollo de aplicaciones educativas en Streamlit usando SymPy. No contiene código ejecutable, solo bloques ilustrativos para orientar la implementación.