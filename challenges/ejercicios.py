#Variables y Strings
var1 = "Asomate"
var2 = "por"
var3 = "la"
var4 = "ventana"
var5 = " "
print(var1 + var5 + var2 +var5 + var3 + var5 + var4)

#Conversión de Libras a Kilos
print("LIBRAS A KILOS")
libras = float(input("Ingrese el peso en libras: "))
kilos = libras*2.205
print(f"{libras} * 2.205 = {kilos} kilos")

#Cálculo de Área y Perímetro de un Triangulo
print("ÁREA DE UN TRIÁNGULO")
base = float(input("Ingrese la base de su triángulo: "))
altura = float(input("Ingrese la altura de su triángulo: "))
area = (base*altura)/2
print(f"El área del triángulo es {area}")
print("PERÍMETRO DE UN TRIÁNGULIO")
l1 = float(input("Ingrese la medida de un lado de su triángulo: "))
l2 = float(input("Ingrese la medida de otro lado de su triángulo: "))
l3 = float(input("Ingrese la medida del tercer lado de su triángulo: "))
perimetro = l1 + l2 + l3
print(f"El perímetro del triángulo es {perimetro}")

#Atínale al precio con if
print("ATÍNALE AL PRECIO")
precio = int(input("¿Cuál crees que sea el precio? > "))
if precio > 1500:
  print("El precio es mayor")
elif precio < 1500:
  print("El precio es menor")
else:
  print("¡Felicidades! Le atinaste al precio")

#Conversión de Moneda
print("CONVERSIÓN DE MONEDA")
def convertir_moneda(cantidad, tasa):
  print(f"{cantidad} de tu moneda actual equivalen a {cantidad*tasa} de la moneda a la que convertiste")

cantidad = float(input("Ingresa la cantidad de dinero: "))
tasa = float(input("Ingresa la tasa de cambio: "))
convertir_moneda(cantidad, tasa)

#Calculadora de Descuento de Compras
print("CALCULADORA DE DESUENTO")
def calcular_descuento(precio_original, porcentaje_descuento):
  print(f"Su precio con descuento es: {precio_original - (precio_original*(porcentaje_descuento/100))}")

precio = int(input("Ingrese el precio de su artículo: "))
descuento = int(input("Ingrese el porcentaje de descuento: "))
calcular_descuento(precio, descuento)