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

chocolates = suma(30, 5)
quesillo = resta(80, 4)
pollos = multiplica(90, 2)
tickets = divide(100, 2)

#Acá un ejercicio matemático por puntos extras
print("Resuelve lo siguente")

que = suma(chocolates, resta(quesillo, multiplica(pollos, divide(tickets, 2))))

print("Eso resulta en: ", que, "¿Lo puedes hacer a mano?")