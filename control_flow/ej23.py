personas = 30
carros = 40
camiones = 15

if carros > personas: #si carros es mayor que personas, se imprime este string
  print("Tomemos los carros")
elif carros < personas: #si por el contrario, carrros es menor que personas, se imprime este otro string
  print("No tomemos los carros")
else: #si no se cumple ninguna de las condiciones anteriores, se imprime esto
  print("No podemos decidir")

if camiones > carros:
  print("Son muchos camiones")
elif camiones < carros:
  print("Tomemos el camión")
else:
  print("Aún no podemos decidir")

if personas > camiones:
  print("OK, solo tomemos el camión")
else:
  print("Bien, quedemonos en casa")