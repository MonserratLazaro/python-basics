la_cuenta = [1, 2, 3, 4, 5]
frutas = ["sandía", "peras", "fresas", "uvas"]
cambio = [1, "centavos", 2, "pesos", 3, "billetes"]

#Este será el primer tuipo de loop que va sobre una lista
for numero in la_cuenta:
  print(f"Esta es la cuenta {numero}")

#Lo mismo que arriba
for fruta in frutas:
  print(f"Un tipo de fruta: {fruta}")

#También podemos ir a través de listas mixtas
#Nota que debemos usar {} pues no sabemoos lo que hay en la lista
for i in cambio:
  print(f"Tengo {i}")

#Podemos también construir listas, iniciamos con una lista vacía
elementos = []

#Luego usamos la función range() para que haga una cuenta de 0 a 5
for i in range(0, 6):
  print(f"Agregar {i} a la lista")
  #append es una dunción que las listas pueden entender
  elementos.append(i)

#ahora pdemos imprimirlos
for i in elementos:
  print(f"El elemento es: {i}")