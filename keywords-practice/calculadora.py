#try, break, except, finally
def start():
  while True:
    try:
      print("  CÁLCULADORA")
      print("Escribe \"1\" para hacer una suma")
      print("Escribe \"2\" para hacer una resta")
      print("Escribe \"3\" para hacer una multiplicación")
      print("Escribe \"4\" para hacer una división")

      choice = input("> ")

      if choice == "1":
        suma()
        break
      elif choice == "2":
        resta()
        break
      elif choice == "3":
        mult()
        break
      elif choice == "4":
        div()
        break
      else:
        print("Escribe una opción válida, vuelve a intentarlo")
        break

    except ZeroDivisionError:
      print("No se puede dividir entre 0, ingresa otra cifra")
      div()

    except ValueError:
      print("Ingresaste un símbolo invalido, vuelve a intentarlo")
      start()

    finally:
      print("¡Vuelva a utilizar esta calculadora pronto")

def suma():
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))
  resultado = num1 + num2
  print(f"{num1} + {num2} = {resultado}")

def resta():
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))
  resultado = num1 - num2
  print(f"{num1} - {num2} = {resultado}")

def mult():
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))
  resultado = num1 * num2
  print(f"{num1} * {num2} = {resultado}") 

def div():
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))
  resultado = num1 / num2
  print(f"{num1} / {num2} = {resultado}")

start()