# Descripción de la Actividad

Este proyecto tiene como objetivo calcular y describir diferentes medidas estadísticas que ayudan a caracterizar conjuntos de datos.

## 1. Medidas para Describir Conjuntos de Datos

### Media
La media aritmética, también conocida como promedio, es la suma de todos los valores en un conjunto de datos dividida por el número de valores. Es una medida de tendencia central que proporciona una representación general del conjunto.

**Cálculo**:
Media = (Suma de todos los valores) / (Número de valores)

### Mediana
La mediana es el valor que se encuentra en el centro de un conjunto de datos cuando estos están ordenados. Si el número de valores es impar, la mediana es el valor del medio; si es par, es el promedio de los dos valores centrales.

**Cálculo**:
- Ordenar los datos.
- Si el número de valores (n) es impar: Mediana = valor en la posición (n+1)/2
- Si n es par: Mediana = (valor en la posición n/2 + valor en la posición (n/2)+1) / 2

### Moda
La moda es el valor o valores que aparecen con mayor frecuencia en un conjunto de datos. Puede haber más de una moda (distribución multimodal) o ninguna (si todos los valores son únicos).

**Cálculo**:
Contar la frecuencia de cada valor y seleccionar el que tenga la mayor frecuencia.

### Varianza
La varianza mide la dispersión de los valores en un conjunto de datos con respecto a su media. Cuanto mayor sea la varianza, más dispersos están los datos.

**Cálculo**:
Varianza = (Suma de los cuadrados de las diferencias respecto a la media) / (Número de valores)

### Desviación Estándar
La desviación estándar es la raíz cuadrada de la varianza y proporciona una medida de la dispersión de los datos en las mismas unidades que los datos originales. Es una forma más intuitiva de entender la variabilidad.

**Cálculo**:
Desviación Estándar = √(Varianza)

### Coeficiente de Variación
El coeficiente de variación es una medida de la dispersión relativa de un conjunto de datos. Se expresa como un porcentaje y se calcula dividiendo la desviación estándar por la media.

**Cálculo**:
Coeficiente de Variación = (Desviación Estándar / Media) × 100

### Normalización Z
La normalización Z transforma los datos de manera que tengan una media de 0 y una desviación estándar de 1. Esto permite comparar datos en diferentes escalas y es útil en el análisis de datos.

**Cálculo**:
Z_i = (valor original - Media) / Desviación Estándar

## 2. Funciones en Python

El proyecto incluye implementaciones de estas medidas en Python a través de la clase `Actividad2`. A continuación, se presentan las funciones utilizadas para calcular cada medida:
