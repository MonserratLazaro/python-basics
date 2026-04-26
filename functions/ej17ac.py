from sys import argv 
script, archivo_entrada = argv

def imprime_todo(f):
  print(f.read())

def regresa(f):
  f.seek(7) 

def imprime_una_linea(cuenta_linea, f):
  print(cuenta_linea, f.readline())

archivo_actual = open(archivo_entrada)

print("Primero imprimamos el archivo completo:\n")
imprime_todo(archivo_actual)

print("Ahora regresemos tal como un cassette")
regresa(archivo_actual)

print("Imprimamos cinco lineas, partiendo de la segunda:")

linea_actual = 1
imprime_una_linea(linea_actual, archivo_actual)

linea_actual = linea_actual + 1
imprime_una_linea(linea_actual, archivo_actual)

linea_actual = linea_actual + 1
imprime_una_linea(linea_actual, archivo_actual)

linea_actual = linea_actual + 1
imprime_una_linea(linea_actual, archivo_actual)

linea_actual = linea_actual + 1
imprime_una_linea(linea_actual, archivo_actual)