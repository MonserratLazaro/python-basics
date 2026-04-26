#VARIABLES Y NOMBRES
carros = 100
espacio_en_carro = 5.0
conductores = 30
pasajeros = 90
carros_sin_manejar = carros - conductores
carros_manejados = conductores
capacidad = carros_manejados * espacio_en_carro
promedio_pasajeros = pasajeros / carros_manejados
posibles_pasajeros = carros_sin_manejar * promedio_pasajeros

print("Hay una cantidad de", carros, "disponibles")
print("Hay una cantidad de", conductores, "con conductor")
print("Hay una cantidad de", pasajeros, "pasajeros")
print("Se necesitan", carros_sin_manejar, "conductores más")
print("Se tiene una capacidad de",capacidad,"en este momento")
print("Se traslada un promedio de",promedio_pasajeros,"pasajeros en cada carro")
print("Con 100 carros en uso se trasladan", pasajeros/carros_manejados*carros, "pasajeros")
print("En los autos sin conductor se prodrían trasladar",posibles_pasajeros,"pasajeros")