#se declara y se pide las variables
seginicio=int(input("Ingrese los segundos\n"))
minu = 0
if seginicio <0 :
    print("la hora ingresada no es correcta")
if seginicio > 0 :
    minu = (int(seginicio/60))
    seg = seginicio%60
    if seg > 1:
        print ("{0} segundos es igual a {1} minuto y {2} segundos \n".format(seginicio, minu, seg))
    else:
        print ("{0} segundos es igual a {1} minutos y {2} segundos \n".format(seginicio, minu, seg))
