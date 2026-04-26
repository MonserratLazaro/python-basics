import random #se importa el módulo random.
from urllib.request import urlopen #del módulo urllib.request se importa la función urlopen.
import sys #se importa el módulo sys.

URL_PALABRAS = "http://learncodethehardway.org/words.txt" #se define la variable URL_PALABRAS con un enlace dentro de ella.
PALABRAS = [] #se define PALABRAS como una lista vacía.

FRASES = { #se define un diccionario llamado FRASES que contiene una serie de strings cuyos símbolos serán reemplazados más adelante.
  "class %%%(%%%):": #clave
    "Haz una class llamada %%% que is-a %%%", #valor
  "class %%%(object):\n\tdef __init__(self, ***)": #clave
    "class %%% has-a __init__ que toma self y *** como parámetros", #valor
  "class %%%(object):\n\tdef ***(self, @@@)": #clave
    "class %%% has-a función *** que toma self y @@@ como parámetros.", #valor
  "*** = %%%()": #clave
    "Pon *** a una instance de class %%%.", #valor
  "***.***(@@@)": #clave
    "Desde *** toma la función ***, llámala con los parámetros self, @@@.", #valor
  "***.*** = '***'": #clave
    "Desde *** toma el attribute *** y pónlo en '***'." #valor
}

#len(sys.argv) == 2, comprueba si los argumentos ingresados al llamar al script son 2.
#sys.argv[1] == "inglés", comprueba si el segundo argumento ingresado al llamar al script es igual a "inglés".
if len(sys.argv) == 2 and sys.argv[1] == "inglés": 
  FRASE_PRIMERO = True #si es verdadero, FRASE_PRIMERO es igual a True
else: #si no, FRASE_PRIMERO es igual a False.
  FRASE_PRIMERO = False #como solo se ingresa un argumento, la variable toma el valor de False.

for palabra in urlopen(URL_PALABRAS).readlines(): #el contenido del url se lee línea por línea y se procesa en el loop
  PALABRAS.append(str(palabra.strip(), encoding="utf-8")) #se eliminan caracteres en blanco de las palabras se convierten en un string con formato utf-8 y se agregan a la lista PALABRAS.

def convierte(snippet, frase): #se define la función convierte que acepta dos parámetros
  class_names = [w.capitalize() for w in 
               random.sample(PALABRAS, snippet.count("%%%"))]  
#se le aplica la función capitalize a una muestra aleatoria de la lista PALABRAS cuyo número de elementos es igual al número de veces que se repite "%%%" en snippet, lo cuál se determina mediante la función count. Los elementos de la muestra guardan en la lista class_names.
  otros_nombres = random.sample(PALABRAS, snippet.count("***")) #se guarda en una variable una muestra aleatoria de elementos de la lista PALABRAS, cuyo numero de elementos es igual al número de veces que se repite "***" en snippet.
  resultados = [] #se define 'resultados' como una lista vacía.
  nombres_parametros = [] #se define 'nombres_parametros' como una lista vacía.

  for i in range(0, snippet.count("@@@")): #for loop que opera en un rango que va desde 0 hasta el número de veces que aparece "@@@" en snippet.
    cuenta_parametros = random.randint(1,3) #se genera un número aleatorio entre 1 y 3 (ambos incluidos) y lo asigna a la variable cuenta_parametros.
    nombres_parametros.append(', '.join(
      random.sample(PALABRAS, cuenta_parametros))) #se utiliza la función random.sample para obtener una muestra de elementos de la lista PALABRAS, el número de elementos se determina por el número que se guardo en la variable cuenta_parametros. Los elementos se agregan a la lista nombres_parametros unidos mediante una coma y un espacio.

  for enunciado in snippet,  frase: #for loop que itera sobre los elementos de snippet y frase
    #Esta es la forma de duplicar una lista o un string
    resultado = enunciado[:] #se le asigna una copia superficial del contenido de 'enunciado' a la variable 'resultado'; copia los elementos, pero no los objetos a los que estos se refieren.

    #nombres de clase falsos
    for palabra in class_names: #para cada palabra en la lista class_name
      resultado = resultado.replace("%%%", palabra, 1) #se reemplaza la primera aparición del string "%%%" por una palabra de la lista y se guarda en la variable resultado

    #otros nombres falsos
    for palabra in otros_nombres: #para cada palabra en otros_nombres
      resultado = resultado.replace("***", palabra, 1) #se reemplaza la primera aparición del string "***" por una palabra de la lista y se guarda en la variable resultado.

    #listas de parámetros falsas
    for palabra in nombres_parametros: #para cada palabra en la lista nombres_parametros
      resultado = resultado.replace("@@@", palabra, 1) #se reemplaza la primera aparición del string "@@@" por una palabra de la lista y se guarda en la variable resultado.

    resultados.append(resultado) #se agregan a la lista "resultados" las palabras que reemplazaron a los símbolos

  return resultados #devuelve la lista de palabras 

#Sigue iterando hasta que presionen CRTL-D
try: #ejecuta el bloque; si hay una excepción, salta a except
  while True: #bucle while que opera mientras sea verdadero
    snippets = list(FRASES.keys()) #se crea una variable llamada snippets que contiene la lista con las claves del diccionario FRASES.
    random.shuffle(snippets) #se mezclan de manera aleatoria los elementos de la lista 

    for snippet in snippets: #para cada clave en la lista 'snippets'
      frase = FRASES[snippet] #guarda en la variable 'frase' el valor asociado a la clave
      pregunta, respuesta = convierte(snippet, frase) #llama a la función 'convierte' con los argumentos 'snippet' (clave) y 'frase' (valor). La función devuelve dos valores, que se asignan a las variables 'pregunta' y 'respuesta'.
      if FRASE_PRIMERO: #si la variable FRASE_PRIMERO es verdadera
        pregunta, respuesta = respuesta, pregunta #se intercambian los valores de las variables 'pregunta' y 'respuesta'

      print(pregunta) #se imprime 'pregunta' = 'snippet' = clave

      input("> ") #se espera la entrada del usuario
      print(f"RESPUESTA: {respuesta}\n\n") #se imprime 'respuesta' = 'frase' = valor. Y se agregan dos saltos de línea

#Al preionar Ctrl + D se envía una señal de fin de archivo, input() detecta el final del archivo y se genera un EOFError.
except EOFError: #si se llega al final del archivo antes de tiempo, se interrumpe el bucle while
  print("\Bye") #se imprime "\Bye" y sale del programa