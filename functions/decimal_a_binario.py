#FUNCIÓN PARA CONVERTIR UN NÚMERO DECIMAL A BINARIO
def decimal_a_binario(numero):
  if numero < 1024:
    
    if numero == 0:
      return 0
      
    else:
      binario = ""
      while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
      return binario
      
  else:
    print("El número debe ser mayor o igual a 0 y menor a 1024, vuelva a intentarlo")

num_decimal = int(input("Ingrese un número decimal para convertirlo a binario: "))
print(f"El número {num_decimal} en binario es {decimal_a_binario(num_decimal)}")