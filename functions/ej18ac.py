def suma(a, b):
  print(f"Sumando {a} + {b}")
  return a + b 

def resta(a, b):
  print(f"Restando {a} - {b}")
  return a - b 

def multiplica(a, b):
  print(f"Multiplicando {a} * {b}")
  return a * b

def divide(a, b):
  print(f"Dividiendo {a} / {b}")
  return a / b

print("Hagamos algo de matemáticas solo con funciones")

choco = int(input("Ingrese un número para sumar: "))
lates = int(input("Ingrese otro número para sumar: "))
suma(choco, lates)
quesillo = int(input("Ingrese un número para la resta: "))
queso = int(input("Ingrese un número para restarle al primero: "))
resta(quesillo, queso)
pollos = int(input("Ingrese un número para multiplicar: "))
gallinas = int(input("Ingrese otro número para multiplicar: "))
multiplica(pollos, gallinas)
tickets = int(input("Ingrese un número para dividr: "))
pases = int(input("Ingrese otro número para dividr: "))
divide(tickets, pases)
