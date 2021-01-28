def salir():
    print("(End of the story)")
    input()


print("Es una fria noche en nignt city eres un detective investigando la desaparicion de una chica de la alta sociedad ella es hija de ")
print("el comisario Dupont el cual te a ordenado la investigacion (a pesar que tu te negaste varias veces) asi que seguiste una pista")
print("la cual te llevo a un club nocturno de mala muerte llamado LA CAJA donde te encontrarias con un informante el cual te podria dar mas informacion acerca de la chica")
print(". Ahora toca la parte dificil pasar al guardia de segurida (Te acercas al guardia)")
print("Hola, quieres entrar a LA CAJA /si/no")
answer_1 = input()

if answer_1 == "si":
    print("Cual es tu nombre")
else:
    print("entonces largate")
    salir()
    exit()

name = input()

print("Bueno "+name+" cual es el codigo")

code = input()

if code == "edameme":
    print("Ok bienvenido")
    print("(Entras a LA CAJA)")
else:
    print("Ese no es el codigo")
    print("Largo de aqui")
    salir()



input()

