nombre = 'Jane'
edad = 20
altura = 1.65  #metros
cabello = 'castaño'
ojos = 'cafés'
año_de_nacimiento = 2000
peso = 60  #kilos

print("Mi nombre es", nombre, ", tengo", edad, "años")
print(f"Hablemos de {nombre}.")
print(f"Ella tiene {edad} de edad.")
print(f"Mide {altura} metros de altura.")

total = edad + altura + año_de_nacimiento
print(f"Si sumo {edad}, {altura} y {año_de_nacimiento} se obtienen la cantidad de {total}")

resultado = nombre + cabello + ojos
print(f"Suma de strings: {resultado}")

altura_pies = altura * 3.281
print(f"Mi altura es {altura_pies} pies")

peso_libras = peso * 2.205
print(f"70 kilos equivale a {peso_libras} libras")
