from sys import argv #se importa la función variable 'argv' desde el modulo 'sys'

script, filename = argv #se declara la variable 0 y 1 dentro de 'argv' 

txt = open(filename) 
#se abre el contenido de la variable 'filename' dentro de la variable'txt'

print(f"Aquí esta tu archivo {filename}:") #se imprime el texto dentro de los paréntesis junto al nombre del archivo de texto declarado en 'filename'
print(txt.read()) #se imprime el contenido del archivo de texto

print("Escribe el texto de nuevo:") #se imprime el texto de los paréntesis
filename_denuevo = input("> ") #en la variable 'filename_denuevo' se guarda otro archivo de texto que el usuario ingrese

txt_denuevo = open(filename_denuevo) #se abre el contenido de la variable 'filename_denuevo' dentro de la variable 'txt_denuevo'

print(txt_denuevo.read()) #se imprime el contenido del segundo archivo de texto