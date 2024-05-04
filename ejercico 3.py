def juego_aventura():
    print("Bienvenido a La gran aventura")
    print("Puedes moverte a la derecha 'd', a la izquierda 'a' o hacia adelante 'w'")
    print("Inicia la aventura")

    decision = input("Corres hacia la montaña nevada. Un ruido te detiene. ¿Te mueves hacia algún lado? (a/d/w): ")

    if decision == 'a':
        print("Ves un gran oso que comienza a avanzar hacia ti. Te quedas muy quieto.")
        print("Después de un momento, te comienzas a deslizar hacia un lado.")
        print("Te mueves hacia la izquierda y encuentras una planta carnívora de conejo.")
        print("Fin de la partida. Muchas gracias por jugar.")
    elif decision == 'd':
        print("Te desvías hacia la derecha y encuentras una cueva oscura.")
        print("Decides entrar en la cueva y encuentras un tesoro perdido.")
        print("¡Felicidades, has ganado el juego!")
    elif decision == 'w':
        print("Decides avanzar hacia adelante y descubres un camino hacia un valle tranquilo.")
        print("Te sientes seguro y continúas explorando el valle.")
        print("¡Felicidades, has ganado el juego!")
    else:
        print("Comando inválido. Por favor, ingresa 'a', 'd' o 'w'.")
        juego_aventura()

juego_aventura()