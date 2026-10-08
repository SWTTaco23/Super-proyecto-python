"""
   Lasmlistas nos permiten almacenar informacion en un 
   lugar, la cantidad que desees: ya sean pocos
   elementos o millones de elementos

   Una lista es una coleccion de items que tiene un
   orden particular. Se pueden crear listas que 
   incluyan strings, enteros, floats, los nombres
   de tu familia. etc.


   Ejemplo:
   """
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'apache']
print(bicycles)

#Como podemos acceder a los elementos de una lista?
"""
   Las listas son colecciones ordenadas. Se puede acceder
   a un elemento de una lista diciendole a Python la 
   posicion o indice del elemento deseado.
   
   Para obtener el valor deseado, se debe escribir el nombre de la 
   lista, seguido del indice del elemento entre corchetes.
"""
print(bicycles[0], bicycles[1], bicycles[2])

print(bicycles[0].upper())

#LOS INDICES COMIENZAN DE 0

#Accediendo al ultimo numero de una lista
print(bicycles[-1])

#utilizando valores individuales de una lista
message = f"My first bicycle was a" {bicycles[-1].upper()}
print (message)
