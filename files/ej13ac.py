print("Ingrese el nombre del archivo: ", end='')
filename = input() #se guarda el archivo ingresado por el usuario en la variable.

print(f"Vamos a borrar el archivo {filename}.")
print("Si no quieres eso, oprime CTRL-C (^C).")
print("Si lo quieres borrar, oprime ENTER")
#se le pregunta al usuario si quiere eliminar el archivo
input("?")
#al presionar ENTER el programa continua, si se presiona CTRL-C ocurre una interrupción de teclado y el programa se descontinua

print("Abriendo archivo...")
destino = open(filename, 'w') #El archivo se abre. 
#El parámetro 'w' indica que tenemos la intención de escribir en el archivo. Al usar 'write' lo que escribamos se sobreescribirá sobre el texto original del archivo, por lo tanto se puede decir que tiene la misma función de 'truncate' de eliminar el contenido y no depende de este para borrar el archivo

print("Truncando el archivo. ¡Adiós!")
destino.truncate() #elimina el contenido del archivo, sin embargo no funcionará si no se escribe el parametro 'w' con anterioridad.

print("Por favor dame tres strings")
#se guardan en tres variables los strings que ingrese el usuario.
linea1 = input("Linea 1: ")
linea2 = input("Linea 2: ")
linea3 = input("Linea 3: ")

print("Ahora voy a escribir esto en el archivo")
 
destino.writelines([linea1, "\n", linea2, "\n", linea3]) #se escriben los strings guardados en el archivo. 'writelines' es un método que permite escribir más de un argumento en una sola línea, cada argumento o string representa una línea diferente que se agragará al archivo.

print("Y finalmente, lo cerramos")
destino.close() #El archivo se cierra.