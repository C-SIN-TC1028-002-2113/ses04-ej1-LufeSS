def main():
    #escribe tu código abajo de esta línea
    pass

    edad = int(input("Ingresa tu edad: "))
    if 0 < edad < 18:
        print("No cumples requisitos")
    elif edad <= 0:
        print("Respuesta incorrecta")
    else:
        ine = input("¿Tienes identificación oficial? (s/n): ")
        if ine == "s":
            print("Trámite de licencia concedido")
        elif ine == "n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")

if __name__ == '__main__':
    main()
