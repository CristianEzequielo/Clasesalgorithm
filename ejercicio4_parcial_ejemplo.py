"""
Escribir una función recursiva que calcule la potenciación de un numero. 
Recibe como parámetros dos números (naturales) a y b devuelve el valor de a**b.
"""
def potenciacion_recursiva(a,b):
    #caso base
    if b == 1:
        return a
    elif b <= 0:
        return 1
    #llamada recursiva
    else:
        return a * potenciacion_recursiva(a,b-1)
    
resultado = potenciacion_recursiva(2,-1)
print(resultado)
