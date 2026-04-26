estados = { # 'nombre del elemento' : 'elemento'
  'Veracruz': 'VER',
  'Yucatan': 'YUC',
  'Oaxaca': 'OAX',
  'Tamaulipas': 'TAM',
  'Chiapas': 'CHI'
}

ciudades ={
  'CAN': 'Cancun',
  'PBC': 'Puebla',
  'MTY': 'Monterrey'
}

ciudades['GDL'] = 'Guadalajara'
ciudades['CDMX'] = 'Ciudad de México' 

print('-' * 10)
print("El estado Chiapas es/tiene: ", estados['Chiapas'])
print("El estado Veracruz es/tiene: ", estados['Veracruz'])

print('-' * 10)
for estados, abbrev in list(estados.items()):
  print(f"{estados} se abrevia como {abbrev}")

print('-' * 10)
for ciudades, abbrev in list(ciudades.items()):
  print(f"{ciudades} se abrevia como {abbrev}")

#print('-' * 10)
#for abbrev, ciudad in list(ciudades.items()):
#  print(f"La abreviación {ciudades} significa {ciudad}") 