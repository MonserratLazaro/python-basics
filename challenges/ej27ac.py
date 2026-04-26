from sys import exit

def start():
  print("  CÁLCULADORA")
  print("Escribe \"1\" para hacer una suma o una resta")
  print("Escribe \"2\" para hacer una multiplicación o división")
  print("Escribe \"3\" para elevar un número a una potencia o sacar una raíz")
  print("Escribe \"4\" para salir")
  var1 = False
  var2 = True
  var3 = False

  while True:
    
    choice = input("> ")
    
    if choice == "4":
      exit()
    elif choice == "1" and not var1:
      print("Ahora elige la operación a realizar, ¿suma o resta?")
      var1 = True
    elif choice == "2" and var2:
      print("Ahora elige la operación a realizar, ¿multiplicación o división?")
      var2 = False
    elif choice == "3" and not var3:
      print("Ahora elige la operación a realizar, ¿potencia o raíz?")
      var3 = True
    elif choice == "suma" and var1:
      suma()
    elif choice == "resta" and var1:
      resta()
    elif choice == "multiplicacion" and not var2:
      mult()
    elif choice == "division" and not var2:
      div()
    elif choice == "potencia" and var3:
      potencia()
    elif choice == "raiz" and var3:
      raiz()
    else:
      print("Escribe una opción válida, vuelve a intentarlo")
      start()

def suma():
  num1 = int(input("Ingresa el primer número: "))
  num2 = int(input("Ingresa el segundo número: "))
  resultado = num1 + num2
  result(f"{num1} + {num2} = {resultado}")

def resta():
  num1 = int(input("Ingresa el primer número: "))
  num2 = int(input("Ingresa el segundo número: "))
  resultado = num1 - num2
  result(f"{num1} - {num2} = {resultado}")

def mult():
  num1 = int(input("Ingresa el primer número: "))
  num2 = int(input("Ingresa el segundo número: "))
  resultado = num1 * num2
  result(f"{num1} * {num2} = {resultado}") 

def div():
  num1 = int(input("Ingresa el primer número: "))
  num2 = int(input("Ingresa el segundo número: "))
  resultado = num1 / num2
  result(f"{num1} / {num2} = {resultado}")

def potencia():
  num = int(input("Ingrese el numero que quiere elevar: "))
  num2 = int(input("Ingrese la potencia: ")) 
  potencia = num ** num2
  result(f"{num} a la {num2}ᵃ potencia es igual a {potencia}")

def raiz():
  num = int(input("Ingrese el numero del que quiere obtener la raíz: "))
  num2 = int(input("Ingrese la magnitud de la raíz: ")) 
  raiz = num ** (1/num2)
  result(f"La raíz {num2}ᵃ de {num} es igual a {raiz}")

def result(fin):
  print("... ", fin, " ...")
  start()

start()