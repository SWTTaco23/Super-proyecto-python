#Eliminacion de espacios en blanco
programming_language = "     python    "
print(programming_language)
print("Efecto del lstrip")
print(programming_language.lstrip())
print("efecto del rstrip")
print(programming_language.rstrip())
print("efecto del strip")
print(programming_language.strip())

#Syntax error
message = "una fortaleza de python es su comunidad"
print(message)
message = 'una fortaleza de 'python' es su comunidad'
print(message)