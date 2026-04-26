print("""Estás en una habitación sol@ y empiezas a escuchar ruidos extraños provenientes
de algún lado.
Ves una puerta, una ventana y un armario, si quieres intentar escapar debes salir por la 
puerta o por la ventana, si quieres esconderte es mejor que entres en el armario.
Elige 1 para salir o 2 para esconderte""")

decision = input("> ")

if decision == "1":
  print("""Elegiste salir, ¡eres muy valiente!, pero primero debes decidir por dónde salir""")
  print("¿Qué eliges, puerta o ventana?")
  
  puerta = input("> ")
  
  if puerta == "puerta":
    print("""Muy bien, has salido por la puerta. Ahora puedes apreciar con claridad un 
patio vacío con sólo un árbol seco en medio. Sigues escuchando ruidos extraños
e identificas que provienen del árbol, ¿eres lo suficientemente valiente para acercarte a
inspeccionar?""")
    
    acercarse = input("> ")
    
    if acercarse == "si":
      print("""Te acercas al árbol y das una vuelta alrededor de él.
Los ruidos comienzan a hacerse más fuertes y ¡oh, no! una rama te cae encima y mueres, 
quizá los ruidos eran tan solo las ramas secas moviéndose con el viento.""")
    elif acercarse == "no":
      print("""Bueno, tal vez sea la mejor decisión. Ahora puedes salir corriendo por la 
puerta del jardín, bye.""")
    else:
      print("Debes escribir \"si\" o \"no\" para tomar una decisión")
      
  elif puerta == "ventana":
    print("""Antes de salir, asomas la cabeza para asegurarte de que no hay peligro y ¡oops!
Tal parece que un bumerán volador te ha cortado la cabeza""")
  
  else:
    print("""Ohh, veo que quisiste escoger otro camino, ¡malas noticias para ti! Ahora un 
asesino serial entra a la habitación y te apuñala.""") 

elif decision == "2":
  print("""Has decidido esconderte, una sabia decisión ¿o talvez no?
Abres el armario y te escabulles entre la ropa. Los extraños crujidos se intensifican 
poco a poco, por suerte a tu lado hay un bate de metal que puedeas usar como arma en caso
de necesitarlo, ¿quieres salir e intentar defenderte?""") 
  
  bate = input("> ")
  
  if bate == "si" or bate == "no":
    print("""¡Sin duda no eres buen@ para tomar decisiones! Antes de que te pudieras 
dar cuenta el armario se desploma encima de ti y mueres, resulta que los ruidos extraños
provenían de la madera vieja del armario.""") 

  else:
    print("Debes escribir \"si\" o \"no\" para tomar una decisión")
    
else:
  print(f"Lo siento, pero la opción {decision} no existe. Vuelve a intentarlo.")