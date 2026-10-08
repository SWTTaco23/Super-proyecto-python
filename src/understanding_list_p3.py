#Trabajando con listas
magicians = ['Hermione', 'Harry', 'Ron', 'voldemort', 'snape']
print("Imprimir con un for")
for magician in magicians:
    print(magician)


#NO OLVIDAR IDENTAR - Traceback identation error
magicians = {'Alice', 'David', 'Caroline'}
for magician in magicians:
print(magician) #identation error


#Error de logica - logic error
for magician in magicians:
    print(magician)
print(f'No puedo esperar a ver el siguiente truco' [magician])