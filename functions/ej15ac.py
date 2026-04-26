def imprime_dos(*argumentos): 
  var1, var2 = argumentos
  print(f"Variable Uno: {var1}, Variable Dos: {var2}")

def imprime_dos_denuevo(var1,var2):
  print(f"Variable Uno: {var1}, Variable Dos: {var2}") 

def imprime_uno(var1):
  print(f"Variable Uno: {var1}") 

def imprime_ninguna():
  print("No tengo nada.")

var1 = input("Introduce una variable: ")
var2 = input("Introduce otra variable: ")
imprime_dos(var1,var2)

var1 = input("Introduce una variable: ")
var2 = input("Introduce otra variable: ")
imprime_dos_denuevo(var1,var2)

var1 = input("Introduce una variable: ")
imprime_uno(var1)

imprime_ninguna()