estados = { 
  'Veracruz': 'VER',
  'Yucatan': 'YUC',
  'Oaxaca': 'OAX',
  'Tamaulipas': 'TAM',
  'Chiapas': 'CHI',
  'Coahuila': 'COA',
  'Sonora' : 'SON'
}

ciudades = {
  'CAN': 'Cancun',
  'PBC': 'Puebla',
  'MTY': 'Monterrey',
  'AGS': 'Aguascalientes',
  'HGO': 'Hidalgo',
  'COL': 'Colima'
}

estados['Estado de México'] = 'EDOMEX'
ciudades['GDL'] = 'Guadalajara'
ciudades['CDMX'] = 'Ciudad de México' 

print('-' * 10)
print("El estado Chiapas es/tiene: ", estados['Chiapas'])
print("El estado Veracruz es/tiene: ", estados['Veracruz'])
print("El estado Sonora es/tiene: ", estados['Sonora'])

print('-' * 10)
print(estados)
print('-' * 10)
print(estados['Oaxaca'])
print('-' * 10)
print(estados.pop('Coahuila'))
print('-' * 10)
print(', '.join(estados))

print('-' * 10)
print(ciudades)
print('-' * 10)
print(ciudades['PBC'])
print('-' * 10)
print(ciudades.pop('HGO'))
print('-' * 10)
print(', '.join(ciudades))

print('-' * 10)
for estados, abbrev in list(estados.items()):
  print(f"{estados} se abrevia como {abbrev}")

print('-' * 10)
for ciudades, abbrev in list(ciudades.items()):
  print(f"{ciudades} se abrevia como {abbrev}")