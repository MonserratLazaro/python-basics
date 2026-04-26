from sys import argv

script, desde_archivo, hacia_archivo = argv 

en_archivo = open(desde_archivo).read()

print(f"Presiona enter para copiar {desde_archivo} en {hacia_archivo}, CTRL-C para abortar"); input()

archivo_salida = open(hacia_archivo, 'w').write(en_archivo)

print("¡Listo!")