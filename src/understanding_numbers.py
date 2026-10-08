#Numeros
#Enteros - Integers
"""
 Los numeros enteros los podemos
 sumar (+), restar (-), multiplicar (*)
 y dividir (/)
"""
print(2+3)
print(3-2)
print(3*2)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1+number_2) 

#Potencias **n
print(3**2) #3^2
print(10%2) #Modulo (mod)
age = 17
print(age)
name = "Fernando Walle"
print(name, age)
#Floats
"""
   Python llama Floats a cualquier numero
   con punto decimal
"""
print(2*0.1)
print(2*0.2)

#Imprimir la edad de alguien
age = 17 #Variable del tipo int
#message = "Fernando tiene" + age + "años" (ERROR)
message = "Fernando tiene" + str(age) + " años"
print(message) 

"""
   TyperError: Python no puede reconocer el tipo de 
   informacion que se esta utilizando
"""
message_f = f"Charly tiene {age} años."
print(message_f)

#Metodo build-in type()
print(type(age), type("Hola"), type(0.54), type(True))