class cancion(object):
  
  def __init__(self, letras):
    self.letras = letras

  def cantame(self):
    for linea in self.letras:
      print(linea)

feliz_cumpleanos = cancion(["Feliz cumpleaños ti",
                            "¡Feliz cumpleaños a ti!",
                            "Feliz Feliz Feliz"])

bulls_parade = cancion(["They rally around the family",
                        "With pockets full of shells"])         

feliz_cumpleanos.cantame()
bulls_parade.cantame()