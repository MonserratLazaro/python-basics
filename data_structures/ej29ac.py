diez_cosas = "Manzanas Naranjas Cuervos Celular Luz Azúcar"

print("Espera, no hay diez cosas en esa lista. Arreglemoslo")

cosas = diez_cosas.split(' ')
mas_cosas = ["Día", "Noche", "Rola", "Disco", "Maíz", "Banana", "Chica", "Chico"]

while len(cosas) != 10: #len: medir en bits
  siguiente = mas_cosas.pop()
  print("Añadiendo: ", siguiente)
  cosas.append(siguiente)
  print(f"Hay {len(cosas)} elementos ahora")
  
print("Aquí vamos: ", cosas)

print("Hagamos algo con 'cosas'.")

print(diez_cosas)
print(mas_cosas)
print(cosas[0])
print(cosas[3])
print(cosas[-2])
print(cosas.pop(1))
#print(cosas)
print(cosas.pop(7))
#print(cosas)
print(' '.join(cosas))
print('#'.join(cosas[2:6]))