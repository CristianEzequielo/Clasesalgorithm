"""
Escribir una función iterativa que calcule la potenciación de un numero. 
Recibe como parámetros dos números (naturales) a y b devuelve el valor de a**b.
"""
def potenciacion_iterativa(a,b):
    i=1
    for x in range(b):
        i *= a
    print(i)

potenciacion_iterativa(2,5)