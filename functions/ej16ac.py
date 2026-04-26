def autos_motos_bicis(autos, motos, bicis): 
  print(f"Tenemos {autos} autos disponibles")
  print(f"También tenemos {motos} motos disponibles")
  print(f"Y {bicis} bicis disponibles")
  print("¡Suficientes para todos ustedes!")

print("> Números asignados directamente a la función:")
autos_motos_bicis(7, 13, 20)

print("> Variables del script:")
autos_disponibles = 5
motos_disponibles = 8
bicis_disponibles = 10

autos_motos_bicis(motos_disponibles, bicis_disponibles, bicis_disponibles)

print("> Operaciones matemáticas:")
autos_motos_bicis(10/2, 5*3, 6+7)

print("> Variables y matemáticas:")
autos_motos_bicis(autos_disponibles + 8, motos_disponibles -1 , bicis_disponibles/2)

print("> Y con input()")
autos_motos_bicis(int(input("Número de autos: ")), int(input("Número de motos: ")), int(input("Número de bicis: ")))
