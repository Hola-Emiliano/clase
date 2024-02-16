diccionario = {
              "lootear": "es un término de origen anglosajón que podríamos traducir como saquear. En el mundo gaming, se trata de una acción que consiste en abrir un cofre, una caja o simplemente recoger objetos del suelo que ya estaban ahí o ha soltado un enemigo al ser golpeado o vencido.",
              "parangaricutirimicuaro":"es parte de un trabalenguas cuyo origen se encuentra en la historia de San Juan de Parangaricutiro, en Michoacán, cuando el nacimiento de un volcán dio fin a todo un pueblo.",
              "paracetamol": "es uno de los medicamentos más utilizados frente al dolor y la fiebre",
              "weon": "“weón” es una variante corta y expresiva de “huevón”, no significa lo mismo para los mexicanos, que la relacionan con una “persona perezosa”. En Honduras y Nicaragua, por ejemplo, hacen referencia a una persona “valiente”.",
              "comunismo": "Movimiento y sistema político, desarrollados desde el siglo XIX, basados en la lucha de clases y en la supresión de la propiedad privada de los medios de producción.",
              }
word = input("Escribe una palabra que no tenga ninguna mayúscula")
if word in diccionario.keys():
    print(diccionario[word])
else:
    print("no lo se rick, no lo se")
