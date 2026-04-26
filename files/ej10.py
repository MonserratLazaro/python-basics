from sys import argv 
cero, primera, segunda, tercera, cuarta = argv

print("Nombre del script:", cero)
print(f"Variable 1:{primera}, variable 2:{segunda}, variable 3:{tercera}, variable 4:{cuarta}")
print(primera + cuarta)
print(primera, segunda, tercera)
print(f"Mariana tiene {primera} y {segunda}")
print(f"¿Te gustan los {primera}?", end='')
cuarta = input()
print(f"Entonces {cuarta} te gustan los {primera}")