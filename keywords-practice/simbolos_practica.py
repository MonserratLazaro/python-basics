#with, as
archivo = input("Introduce el nombre del archivo: ")
with open(f'{archivo}', 'w') as file:
  file.write('Prueba')
  print("Se ha escrito el texto en el archivo")

#class
class Perro:
  def __init__(self, raza, color):
    self.raza = raza
    self.color = color

  def __str__(self):
    return f"El perro es un {self.raza} y es de color {self.color}"

perro = Perro("golden retriver", "dorado")
print(perro)

#continue
for i in range(0, 6):
  if i == 4:
    continue
  print(i)

#pass
num = int(input("Intrduce un número: "))
if num == 10:
  print("El número es 10")
else:
  pass
  
#assert 
v1 = "h"
assert v1 == "h"
#assert v1 == "k", el programa termina con un error debido a que es False

#del
v2 = "hola"
del v2
#print(v2), si se intenta imprimir resulta en un error, la variable no existe

#global
v4 = "adiós"
def funcion():
  print(f"Hola y {v4}")
funcion()

#lambda
prueba = lambda x: x + 5
print(f"Prueba de lambda: {prueba(20)}")

#is
v5 = v1
print(v5 is v1)

#yield
def generador():
  x = 1
  yield x
  x += 1
  yield x

g = generador()  
print(next(g))
print(next(g))

#exec
exec('print("Pruebas de exec 1")')
x = 'print("Prueba de exec 2")'
exec(x)

#raise
print("\nPrueba de raise: \n")
v3 = 4
if v3 > 3:
  raise Exception('v3 es mayor que 3') #El programa termina en un error 