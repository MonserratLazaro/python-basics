#FUNCIÓN PARA CONVERTIR UN NÚMERO DECIMAL A BINARIO CON FUNCIÓN bin()
def decimal_a_binario(decimal):
  if decimal < 1024:
    binario = bin(decimal)[2:]
    print(f"El número {decimal} en sistema binario es: {binario}")
  else:
    print("El número debe ser menor a 1024, vuelva a intentarlo")

num_decimal = int(input("Ingrese un número decimal para convertirlo a binario: "))
decimal_a_binario(num_decimal)