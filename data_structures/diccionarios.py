organos = {
  'Cerebro': 'CER',
  'Corazon': 'COR',
  'Higado': 'HIG',
  'Pancreas': 'PAN',
  'Estomago': 'EST'
}

partes = {
  'CER': 'Bulbo raquídeo',
  'COR': 'Septo',
  'HIG': 'Lóbulo caudado',
  'PAN': 'Conducto pancreático',
  'EST': 'Esófago'
}

print('-' * 10)
for clave, valor in list(organos.items()):
  print(f"{clave} esta representado con la letras {valor}")

print('-' * 10)
for clave, valor in list(partes.items()):
  print(f"{clave} contiene al {valor}")

print('-' * 10)
for clave, valor in list(organos.items()):
  print(f"La abreviatura {valor} representa al {clave}")
  print(f"Una parte del {clave} es el {partes[valor]}")

print('-' * 10)
introducir_organo = input("""Introduce un órgano para agregarlo al diccionario y verlo impreso
(utiliza mayúscula inicial y no utilices tildes): """)
organo = organos.get(introducir_organo)

if not organo or False:
    abbrev = input("Introduce una abreviatura para identificarlo: ")
    organos[introducir_organo] = abbrev
    parte = input("Introduce el nombre de una parte del órgano: ")
    partes[abbrev] = parte

    print(f"""\nSe ha agregado al diccionario:
    {introducir_organo} esta representado mediante las letras {abbrev} y {partes[abbrev]} es una de sus partes.""")

else:
  print("Ese órgano ya está en el diccionario, intentalo de nuevo...")