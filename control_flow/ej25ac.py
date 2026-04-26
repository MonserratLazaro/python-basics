num_inicial = 10
lista_numeros = []

while num_inicial < 200: #mientras la condición se cumpla ocurre lo siguente:
  print(f"Por el momento i vale {num_inicial}")
  lista_numeros.append(num_inicial) #se ingresan los números a la lista vacia
  
  num_inicial = num_inicial * 2 #num_inicial va cambiando de valor
  print("Numeros ahora: ", lista_numeros)
  print(f"Pero ahora i vale {num_inicial}")

#cuando la condición se rompe y while se termina de ejecutar, el código continua
print("Los números dentro de la lista son: ")

for elemento in lista_numeros: #for loop para imprimir todos los elementos de la lista
  print(elemento)