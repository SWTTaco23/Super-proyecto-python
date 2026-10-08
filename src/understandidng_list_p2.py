#Agregando elementos a una lista
motorcycles = ['honda', 'mortalika', 'yamaha']
print(motorcycles)

#Metodo append
motorcycles.append("kawasaki")
print(motorcycles)

"""
   El metodo append ayuda a crear listas

"""
#El metodo insert nos ayuda a agregar elementos a una lista en un indice especifico
motorcycles_3 = ["honda", "yamaha", "suzuki"]
print("\nLista Original")
print(motorcycles_3)
motorcycles_3.insert(-2, 'ducati')
print("Lista despues del metodo insert")
print(motorcycles_3)
#Se le llama argumentos a la cantidad de cosas que te solicita append o insert, insert pide 2, append 1

#Metodo .pop() Elimina el ultimo elemento de la lista
#pero nos permite utilizar el elemento despues de eliminarlo
"""
   El metodo pop elimina
   elementos de una lista 
   por indice
"""
print("\n\tAqui apreni a utilizarr el metodo pop" .upper())
motorcycles_4 = ['honda', 'suzuki', 'hd', 'mortalika']
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop()
print(f"Tu motocicleta borrada es: {deleted_motorcycle}")
print(motorcycles_4)

#Tarea estudiar el metodo de ls listas .reverse()
#Estudiar metodos build-in: sortedd, len()

#.REVERSE()
"""
   El metodo .reverse() invierte el orden de los elementos
   de una lista, haciendo que el ultimo pase a ser el primero
   y el primero pase a ser el ultimo. Modifica directamente
   la lista original y no crea una nueva. Por ejemplo, si la 
   lista contieme 1,2,3 y 4, despues de usar .reverse() quedara
   como 4,3,2 y 1.
"""
numeros = [1, 2, 3, 4, 5]
numeros.reverse()

print(numeros)#5,4,3,2,1

#Sortedd
"""
   La funcion .sorted() ordena los elementos de una coleccion
   y devuelve una nueva lista, sin modificar la original.
   Por defecto ordena los numeros de menor a mayor y los textos
   de manera alfabetica. Por ejemplo si una lista contiene 
   3,1 y 2 al usar sorted se obtiene una nueva lista con
   1,2 y 3, tambien permite ordenar de forma descendente
   usando reverse = True 
"""

#len()
"""
   Devuelve la cantidad de elementos que contiene una coleccion,
   como una lista, tupla o diccionario. Tambien permite contar los 
   caracteres de un texto, incluyendo espacios y signos. Por ejemplo,
   si una lista contiene 10, 20 y 30, len() devuelve 3 porque tiene 3 argumentos
"""