"""
Escribir una función que reciba dos parámetros: (i) una lista desordenada y (ii) una expresión 
(una expresión es parámetro que puede ser evaluado a True o False). 
Si el valor de la expresión es Verdadera (True), la lista se ordenara en forma descendente, 
en otro caso de manera ascendente. 
Por defecto, si la función es llamada sin una "expresión" (solo la lista) 
debe retornar una lista ordenada de forma ascendente.
"""
def function(lista, expresion = True):
    if expresion == True:
        return sorted(lista)
    else:
        return sorted(lista,reverse=True)
mi_lista = [7, 4, 8, 9, 1, 6]
lista_ordenada = function(mi_lista, expresion = True)
print(lista_ordenada)

