elementos = []

for i in range(0, 6):
  print(f"Agregar {i} a la lista")
  elementos.append(i)
  print(f"El elemento es: {i}")

cuenta = []

for cifras in range(10, 21):
  print(f"Agregando {cifras} a la cuenta")
  cuenta.append(cifras)

for cifras in cuenta:
  print(f"{cifras} ya está en la cuenta")

billetes = []

for dinero in range(1000, 1010):
  print(f"Tengo {dinero} billetes")
  billetes.append(dinero)

for dinero in billetes:
  print(f"Te doy {dinero} billetes")