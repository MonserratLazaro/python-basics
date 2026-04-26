def perimetro(diametro):
  print("Calculando perímetro...")
  perimetro = 3.1416 * diametro
  print(perimetro)
  return perimetro

print("Calculadora de áreas y perímetros de círculos")

print("> PERÍMETRO \nIngrese el diámetro de su círculo: ")
resultado = perimetro(float(input()))

def area(radio):
  print("Calculando área...")
  area = 3.1416 * (radio*radio)
  print(area)
  return area

print("> ÁREA \nIngrese el radio de su círculo: ")
resultado = area(float(input()))