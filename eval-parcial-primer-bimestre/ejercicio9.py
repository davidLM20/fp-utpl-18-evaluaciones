#angulos y lados del primer triangulo 
angulo1=float(input("Ingrese el angulo A del primer triangulo\n"))
angulo2=float(input("Ingrese el angulo B del primer triangulo\n"))
angulo3=float(input("Ingrese el angulo C del primer triangulo\n"))
lado1=float(input("Ingrese el lado a del pirmer triangulo\n"))
lado2=float(input("Ingrese el lado b del pirmer triangulo\n"))
lado3=float(input("Ingrese el lado c del pirmer triangulo\n"))
# angulos y lados del segundo triangulo 
angulo4=float(input("Ingrese el angulo A del primer triangulo\n"))         
angulo5=float(input("Ingrese el angulo B del primer triangulo\n"))
angulo6=float(input("Ingrese el angulo C del primer triangulo\n"))
lado4=float(input("Ingrese el lado a del pirmer triangulo\n"))
lado5=float(input("Ingrese el lado b del pirmer triangulo\n"))
lado6=float(input("Ingrese el lado c del pirmer triangulo\n"))

if (angulo1==angulo4 and angulo2==angulo5 and angulo3==angulo6):
    pirnt("Los tiangulos son congruentes")
else:
    if(lado1==lado4 and lado2==lado5 and lado3==lado6):
        print("Los triangulos son congruentes")
    else:
        print("Los triangulos no son congruentes")

