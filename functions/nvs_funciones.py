import random
from urllib.request import urlopen

#urlopen
url = 'https://www.google.com/?hl=es'
contenido = urlopen(url).read()
#print(contenido)

#str
numero = 56
texto = "alumnos"
print(str(numero) + " " + texto)

#strip
saludo = "  Buenos días "
print(saludo.strip())

#capitalize
print('hola, ¿CÓMO estás?'.capitalize())

#sample
animales = ["perros", "gatos", "serpientes", "conejos", "loros"]
print(random.sample(animales, 3))

#count
color = "Amarillo"
veces = color.count("l")
print(f"La letra 'l' aparece {veces} veces en la palabra {color}")

#randint
print(random.randint(10, 20))

#replace
print("Hola, Juan".replace("Juan", "Pedro"))
print("aaaaaa".replace("a", "x", 4))

#keys
diccionario = {'nombre': 'Monserrat',
              'apellido1': 'Lázaro',
              'apellido2': 'Salinas'}
print(diccionario.keys())

#shuffle
random.shuffle(animales)
print(animales)

#EOFError
try:
  nombre = input("Ingresa tu nombre: ")
  print(f"Tu nombre es {nombre}")
  
except EOFError:
  print("Se alcanzo el final de archivo inesperadamente")