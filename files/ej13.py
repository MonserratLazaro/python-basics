from sys import argv
script, filename = argv

print(f"Vamos a borrar el archivo {filename}.")
print("Si no quieres eso, oprime CTRL-C (^C).")
print("Si lo quieres borrar, oprime ENTER")

input("?")

print("Abriendo archivo...")
destino = open(filename, 'w') 

print("Truncando el archivo. ¡Adiós!")
destino.truncate()

print("Por favor dame tres strings")

linea1 = input("Linea 1: ")
linea2 = input("Linea 2: ")
linea3 = input("Linea 3: ")

print("Ahora voy a escribir esto en el archivo")

destino.write(linea1)
destino.write("\n")
destino.write(linea2)
destino.write("\n")
destino.write(linea3)
destino.write("\n")

print("Y finalmente, lo cerramos")
destino.close() 