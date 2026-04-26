import math

#DESCUENTO
def descuento_articulo(precio, descuento):
  print("DESCUENTO")
  precio_final = precio - ((descuento / 100) * precio)
  print("El precio final es:", precio_final)
  return precio_final

precio = int(input("Ingrese el precio del producto: "))
descuento = int(input("Ingrese el descuento en porcentaje: "))
descuento_articulo(precio, descuento)

#RADIANES
def radianes_a_grados(radianes):
  print("RADIANES A GRADOS")
  grados = (radianes * 180) / math.pi
  print(f"{radianes} radianes equivalen a {grados} grados")

angulo_rad = float(input("Ingrese el ángulo en radianes: "))
radianes_a_grados(angulo_rad)

#ORDENAR LSITA
def ordenar(lista, string):
  print("LISTA ORDENADA")
  if string == "asc":
    lista.sort()
    print(lista)
  elif string == "desc":
    lista.sort(reverse=True)
    print(lista)
  elif string == "none":
    print(lista)
  else:
    print("Ingrese una opcion valida")

lista = []
print("Ingrese los numeros de la lista, presione \".\" para terminar: ")
numero = input("> ")
while numero != ".":
  lista.append(numero)
  numero = input("> ")

print("""Ingrese la forma de ordenar las lista. 
  \"asc\" = ascendente 
  \"desc\" = descendente
  \"none\" = sin ordenar""")
string = input("> ")

ordenar(lista, string)