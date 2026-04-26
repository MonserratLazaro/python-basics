def rompe_palabras(cosas):
  """Esta función rompe palabras"""
  palabras = cosas.split(' ') 
  return palabras

def ordena_palabras(palabras):
  """Ordena las palabras"""
  return sorted(palabras)

def imprime_primer_palabra(palabras):
  """Imprime la primer palabra después de sacarla"""
  palabra = palabras.pop(0)
  print(palabra)

def imprime_ultima_palabra(palabras):
  """Imprime la última de las palabras despúes de sacarla"""
  palabra = palabras.pop(-1)
  print(palabra)

def ordena_frase(frase):
  """Toma una frase entera y regresa las palabras ordenadas"""
  palabras = rompe_palabras(frase)
  return ordena_palabras(palabras)

def imprime_primera_y_ultima(frase):
  """Imprime la primera y última palabra de la frase"""
  palabras = rompe_palabras(frase)
  imprime_primer_palabra(palabras)
  imprime_ultima_palabra(palabras)

def imprime_primera_y_ultima_ordenada(frase):
  """Ordena las palabras y luego imprime la primera y la última"""
  palabras = ordena_frase(frase)
  imprime_primer_palabra(palabras)
  imprime_ultima_palabra(palabras)

var1 = "Mucho gusto en conocerte"
var2 = rompe_palabras(var1)
print(var2)
print(ordena_palabras(var2))
imprime_primer_palabra(var2)
#print(var2)
imprime_ultima_palabra(var2)
#print(var2)
print(ordena_frase(var1))
imprime_primera_y_ultima(var1)
imprime_primera_y_ultima_ordenada(var1)