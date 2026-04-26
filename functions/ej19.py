print("Vamos a practicar de todo")
print('Necesitamos saber \'crca de escapes y \\ lo que hacen:')
print("\nnuevas líneas y \t tabs")

poema = """
\t Oh México tan dividido
tan corrupto. Tan lejos de Dios
tan lejos de Estados Unidos.
\n\t Y luego está esta línea.
"""

print("----------------------")
print(poema)
print("----------------------")

cinco = 10 - 2 + 3 -6
print(f"Esto debería ser {cinco}")

def formula_secreta(inicio):
  pollos = inicio + 500
  aguas = pollos / 1000
  tortas = aguas / 100
  return pollos, aguas, tortas

punto_inicial = 10000
frijoles, jarras, cajas = formula_secreta(punto_inicial) 

#Esta es otra forma de formatear strings
print("Con el inicio en: {}".format(punto_inicial))
#Es tal como un f"" string
print(f"Tenemos{frijoles} frijiles, {jarras} jarras y {cajas} cajas")

punto_inicial = punto_inicial / 10

print("También lo podemo hacer de esta forma:")
formula = formula_secreta(punto_inicial)
#Esta es una forma fácil de aplicar una lista a un string con formato
print("Tendriamos {} chocolates, {} jarras y {} cajas.".format(*formula))