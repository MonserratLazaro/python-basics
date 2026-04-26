#Este es como los scripts con argv
def imprime_dos(*argumentos): #definir función
  var1, var2 = argumentos
  print(f"Variable Uno: {var1}, Variable Dos: {var2}")

#El uso de *ALGO no tiene mucho caso, podemos hacer esto
def imprime_dos_denuevo(var1,var2):
  print(f"Variable Uno: {var1}, Variable Dos: {var2}") 

#Esta toma solamente un argumento
def imprime_uno(var1):
  print(f"Variable Uno: {var1}")

#Esta NO toma argumentos
def imprime_ninguna():
  print("No tengo nada.")

imprime_dos("MONSE","16")
imprime_dos_denuevo("LÁZARO", "SALINAS")
imprime_uno("¡HOLA!")
imprime_ninguna()