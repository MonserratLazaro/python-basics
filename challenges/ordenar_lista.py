numeros = []
print("""Ingrese un número para su lista, presione ENTER para seguir ingresando números.
Una vez que haya terminado de ingresar todos los números, presione ENTER nuevamente o ingrese cualquier otro caracter para terminar.""")

try:
  while True:
    numero = int(input("> "))
    numeros.append(numero)
except ValueError:
  pass

orden = input("Ingrese el orden deseado (asc, desc o none): ")

def ordenar_lista(lista, orden):
  if orden == "asc":
    lista.sort()
    print(lista)

  elif orden == "desc":
    lista.sort(reverse=True)
    print(lista)

  elif orden == "none":
    print(lista)

  else:
    print("Orden no válido, vuelva a intentar usando asc, desc o none")

ordenar_lista(numeros, orden)