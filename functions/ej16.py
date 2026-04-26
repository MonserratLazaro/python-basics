def queso_y_galletas(cuenta_queso, cajas_galletas): 
  print(f"Tienes {cuenta_queso} quesos")
  print(f"Tienes también {cajas_galletas} cajas de galletas")
  print("Suficiente para una reunioncilla")
  print("Trae aguas frescas")

print("Le podemos dar números directo a la función:")
queso_y_galletas(20, 30)

print("O, podemos usar variables de nuestro script:")
cantidad_de_queso = 10
cantidad_de_galletas = 50

queso_y_galletas(cantidad_de_queso, cantidad_de_galletas)

print("Incluso podemos hacer matemáticas ahí dentro:")
queso_y_galletas(10 + 20, 10 - 6)

print("Y también podemos combinar ambas cosas, variables y matemáticas:")
queso_y_galletas(cantidad_de_queso + 100, cantidad_de_galletas + 1000)