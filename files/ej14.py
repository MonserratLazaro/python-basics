from sys import argv
from os.path import exists 

script, desde_archivo, hacia_archivo = argv 

print(f"Copiando {desde_archivo} hasta {hacia_archivo}")

en_archivo = open(desde_archivo)
datos = en_archivo.read()

print(f"El archivo inicial es de {len(datos)} bytes de largo")

print(f"¿Existe el archivo de salida?{exists(hacia_archivo)}")
print("List, presiona enter para continuar, CTRL-C para abortar")
input()

archivo_salida = open(hacia_archivo, 'w')
archivo_salida.write(datos)

print("Bien, todo listo")

archivo_salida.close()
en_archivo.close()