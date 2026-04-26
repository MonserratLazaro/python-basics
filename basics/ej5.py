tipos_de_perros = 10 
x = f"conozco unas {tipos_de_perros} razas de perros" #esta variable contiene un f-string

raza1= "PAleman"
raza2= "Bulldog"
y = f"unos son {raza1} y otros son {raza2}" #variable igual a un f-string

print(x)
print(y)

#impresion de f-strings
print(f"Por un lado sigo: {x}") 
print(f"Por otro lado digo: {y}")

razas_adicionales = False 
mas_razas = "¿Cónozco más razas de perros? {}"

#se imprime la variable mas_razas y en los corchetes se inserta la variable razas_adicionales
print(mas_razas.format(razas_adicionales))

x1 = "Este es el lado izquierdo de ..."
x2 = "un string largo, en donde este es su lado derecho"

print(x1 + x2) #"suma" de strings para unir dos partes de una oración