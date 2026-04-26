def angulo(radianes):
  grados = radianes * (180 / 3.1416)
  print(f"El ángulo en grados es de: {grados}")
  return grados

angulo_rad = float(input("Ingrese el ángulo en radianes: "))
angulo(angulo_rad)