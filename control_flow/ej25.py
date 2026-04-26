i = 0
numeros = []

while i < 6:
  print(f"Por el momento i vale {i}")
  numeros.append(i)
  
  i = i + 1
  print("Numeros ahora: ", numeros)
  print(f"Pero ahora i vale {i}")

print("Los números dentro de la lista son: ")

for num in numeros:
  print(num)