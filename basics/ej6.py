print("Los caminos de la vida")
print("no son como yo pensaba")
print("como los imaginaba")
print("no son como yo {}".format('creía')) #'creía' se inserta en el lugar de los corchetes debido al format

print("coro" * 10) #La palabra coro se imprime 10 veces seguidas

#Declaración de variables con caracteres
x1 = 'P' 
x2 = 'O'
x3 = 'L'

print(x1 + x2 + x3 + x3 + x2) #"suma" de caracteres para formar la palabra POLLO
print(x1 + x2 + x3 + x2) #"suma" de caracteres para formar la palabra POLO

formateando = "{} {} {} {}" #declaración de variable igual a 4 pares de corchetes

#lo que está escrito dentro de los paréntesis después del format se imprime en lugar de los paréntesis de la variable formateando
print(formateando.format(1,2,3,4))
print(formateando.format('UNO', 'DOS', 'TRES', 'CUATRO')) 
print(formateando.format(True, False, True, False))
print(formateando.format(formateando, formateando, formateando, formateando)) 
print(formateando.format("Intenta", "tu propia", "canción", "aquí"))