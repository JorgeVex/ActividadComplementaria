"""
Descripción de la actividad
    1. Considere las siguientes médidas para describir conjuntos de datos:
    - Media
    - Mediana
    - Moda
    - Varianza
    - Desviación Estandar
    - Coeficiente de variación
    - Normalización Z
    2. Describa formalmente cada medida y presente cómo se construyen.
    3. Cree las funciones en python. Presente el código y expliquelo.
"""

from collections import Counter
import math
import random

class Actividad2():
    
    def __init__(self, data):
        
        self.data = data
    
    def media(self):
        """
        La mediana es el valor central de un conjunto de datos ordenados. 
        Si el número de valores es impar, es el valor del medio; si es par, 
        es el promedio de los dos valores centrales.
        Se calcula sumando un grupo de números y dividiendo a continuación por el recuento de dichos números.
        Por ejemplo, el promedio de 2, 3, 3, 5, 7 y 10 es 30 dividido por 6, que da como resultado 5.
        """
        return sum(self.data) / len(self.data)
    
    def mediana(self):
        """
        La mediana es el valor central de un conjunto de datos ordenados. 
        Si el número de valores es impar, es el valor del medio; si es par, es el promedio de los dos valores centrales.
        Para obtener la mediana, se ordenan los elementos ya sea de una lista, o mejor dicho, de un conjunto de datos
        de forma ascendente o descendente, y se selecciona el valor central que divide en 2 el conjunto de datos
        """
        
        encontrar_dato = sorted(self.data)
        n = len(encontrar_dato)
        valor_medio = n // 2
        if n % 2 == 0:
            return (encontrar_dato[valor_medio - 1] + encontrar_dato[valor_medio]) / 2
        else:
            return encontrar_dato[valor_medio]
    
    def moda(self):
        """
        La moda es el valor que aparece con más frecuencia en el conjunto de datos.
        """        
        conteo = Counter(self.data)
        valorModa = max(conteo.values())
        moda = [i for i, v in conteo.items() if v == valorModa]
        return moda
    
    def varianza(self):
        """
        La varianza mide la dispersión de un conjunto de datos respecto a su media. 
        Se calcula como la media de las diferencias al cuadrado entre cada valor y la media.
        """
        valor_media = self.media()
        return sum((x - valor_media) ** 2 for x in self.data)/len (self.data)
    
    def desviacion_estandar(self): 
        """
        La desviación estándar es la raíz cuadrada de la varianza y también mide la dispersión de los datos. 
        Es más intuitiva ya que se encuentra en las mismas unidades que los datos originales.
        """
        return math.sqrt(self.varianza())
    
    def coeficiente_variacion(self):
        """
        El coeficiente de variación es la relación entre la desviación estándar y la media, expresada como un porcentaje. 
        Es útil para comparar la variabilidad de diferentes conjuntos de datos.
        """
        return (self.desviacion_estandar() / self.media()) * 100
    
    def normalizacion_Z(self):
        """
         La normalización Z transforma los datos de modo que tengan una media de 0 y una desviación estándar de 1. 
         Esto se utiliza para comparar datos en diferentes escalas.
        """
        valor_medio = self.media()
        desv_estand = self.desviacion_estandar()
        
        return [( x - valor_medio) / desv_estand for x in self.data]


#Generar una lista de 20 numeros aleatorios entre 1 y 5
data = [random.randint(1, 5) for _ in range(20)]

#Imprimir los numeros de la lista de forma horizontal, separado por comas
print(", ".join(str(number) for number in data))

ejemploUso = Actividad2(data)
print("Media:", ejemploUso.media())
print("Mediana:", ejemploUso.mediana())
print("Moda:", ejemploUso.moda())
print("Varianza:", ejemploUso.varianza())
print("Desviación Estándar:", ejemploUso.desviacion_estandar())
print("Coeficiente de Variación:", ejemploUso.coeficiente_variacion())
print("Normalización Z:", ejemploUso.normalizacion_Z())

