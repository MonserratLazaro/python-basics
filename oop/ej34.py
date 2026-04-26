#is-a y has-a
#reemplazar cada ##??

#Animal is-a object
class Animal(object):
  pass

## Perro is-a Animal
class Perro(Animal):
  
  def __init__(self, name):
    ## Perro has-a name
    self.name = name 


## Gato is-a Animal
class Gato(Animal):
  
  def __init__(self, name):
    ## Gato has-a name 
    self.name = name

## Persona is-a object
class Persona(object):
  
  def __init__(self, name):
    ## Persona has-a name
    self.name = name
    
    #Persona has-a mascota de algún tipo
    self.pet = None

## Empleado is-a Persona
class Empleado(Persona):

  def __init__(self, name, salario):
    ## Empleado has-a name, llamada al constructur de la clase padre (Persona) usando super()
    super(Empleado, self).__init__(name)
    ## Empleado has-a salario
    self.salario = salario 

## Pez is-a object
class Pez(object):
  pass

## Salmon is-a Pez
class Salmon(Pez):
  pass

## Mojarra is-a Pez
class Mojarra(Pez):
  pass


## pug is-a Perro
pug = Perro("Pug")

## persa is-a Gato
persa = Gato("Persa")

## maria is-a Persona
maria = Persona("María")

## maria has-a mascota que es un Gato (Persa)
maria.mascota = persa

## juan is-a Empleado
juan = Empleado("Juan", 120000)

## juan has-a mascota que es un Perro (Pug)
juan.mascota = pug

## flipper is-a Pez
flipper = Pez()

## gallo is-a Salmon
gallo = Salmon()

## toby is-a Mojarra
toby = Mojarra()