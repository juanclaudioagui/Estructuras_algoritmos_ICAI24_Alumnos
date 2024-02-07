# Ejercicio sobre Factorización (2/Feb/2023)
## Introducción
Cualquier número puede ser descompuesto en factor de potencias de números primos que son sus divisores. Vamos a ver algunos algoritmos básicos en este mundo cercano a al teoría de números, y a la criptografía.

## Algoritmos a utilizar
### 1) **Verificar si un número es primo**
Basta con ver si el resto de dividir por 2, o por todos los impares hasta la raíz cuadrada de n, es cero.  
Qué complejidad tiene este algoritmo ?

### 2) **Algoritmo para hallar los factores primos de un número**
El algoritmo es sencillo:

* Busca 2 como divisor, tantas veces como sea posible, dividiendo por 2 el número aportado
* Busca, impares de 3... hasta sqrt(n) y divide si la division es entera
* Si queda algo por encima de la raíz de n es que este es un número primo que divide  n

Utilizamos el subtipo de diccionario <strong>Counter</strong> para acumular los factores y su multiplicidad

Hay tres fases. Cuál es el orden de complejidad de cada una ? Alguna domina a las otras ?

## Medición de Tiempos
Escribe los algoritmos y verifícalos. Puede ser interesante construir una función que retorna un número aleatorio en un rango dado.

Ve con cuidado, los tiempos de ejecución pueden ser muy largos para números muy grandes. En Teoría de Números y en criptografía,  se utilizan números con cientos de dígitos. Hasta donde puedes ir con tu ordenador? Es Python un problema?

Mide tiempos de ejecución del algoritmo de Factorización. Es siempre comparable el coste de ejecución, para dos números comparables, o no? Si lo es, con unas pocas veces que midas te valdrá.  Si no, hay que medir más y ver que hacer con la dispersión de los resultados

## Complejidad Algoritmica
### Análisis teórico
Para el algoritmo  de Factorización, cuál es la complejidad máxima de cada paso ? Se puede ignorar alguno ? 
Cuál es la complejidad resultante del algoritmo ?

### Análisis Práctico
Con las mediciones  realizadas y el análisis teórico realizado. Concuerdan ? 

Haz un  análisis de regresión ( ajustar un polinomio de cierto grado a los datos de la medición. Puedes usar   la función polyfit en la librería numpy de Python ) y ajusta el modelo teórico a los resultados de la medición

>Concuerdan ??

## Bonus track
Examina el package de **primeFac** de python, y corre los mismos test con la librería de Python y compara los resultados.
