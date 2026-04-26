from sys import argv
script, usuario1, usuario2 = argv

entrada = '- '

print(f"Hola {usuario1} y {usuario2}, yo soy el {script} script.")
print("Quisiera hacerles algunas preguntas")
print(f"¿Te agrado {usuario1}?")
agradar1 = input(entrada)

print(f"¿Te agrado {usuario2}?")
agradar2 = input(entrada)

print(f"¿Qué tipo de computadora tienes {usuario1}?")
computadora1 = input(entrada)

print(f"¿Qué tipo de computadora tienes {usuario2}?")
computadora2 = input(entrada)


print(f"""
Buenas respuestas, al parecer {agradar1} le agrado a {usuario1} y {agradar2} le agrado a {usuario2}.
{usuario1} dice que usa una {computadora1} y {usuario2} usa una {computadora2}, ¡genial!
""")