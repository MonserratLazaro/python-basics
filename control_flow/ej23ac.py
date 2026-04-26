labradores = 50
pastor_aleman = 30
beagles = 20

if labradores == 60 and beagles!= 40:
  print("Hay más labradores que beagles")
elif labradores == pastor_aleman or beagles == 20:
  print("Hay menos beagles que labradores")
else:
  print("Hay la misma cantidad de beagles y labradores")

if pastor_aleman == 10 and not(beagles == labradores):
  print("Hay menos labradores que pastores alemanes")
elif not(labradores != 30) or not(pastor_aleman == 30):
  print("Hay la misma cantidad de labradores que de pastores alemanes")
else:
  print("Hay menos pastores alemanes que labradores")