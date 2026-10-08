players = ["jason", "benjamin", "bryian", "Shecid", "allison", "wendy"]
print ("Lista original:", players)

#slicing
print(players[3:6])

"""
    El slicing me permite trabajar con un grupo
    especifico de una lista: al resultado se le conoce como
    "Un slice".
"""


print("1:4", players[1:4])
print(":3", players[:3])
print("2:", players[2:])
print("-3:", players[-3:])

#Casos especiales de slicing
print("Casos especiales")
print(players)
print(players[1:10])
print(players[1:10])
print(players[-10:10])
print(players[6:1])
print(players[:0])
print(players[0:1])

#Looping through a slice
print("Looping through a slice")
students = ["jason", "benjamin", "bryian", "Shecid", "allison", "wendy"]

#Slicing [::] Tarea
for student in students[3:5]:
    print(f"el estudiante"[3:5]"va a pasar la materia")