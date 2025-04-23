total = 0
op = 0

while op != 3:
    print("Seleccione una opción")
    print("1.- Comprar ticket")
    print("2.- Terminar compra")
    print("3.- Salir")
    
    try:
        op = int(input("Ingrese una opción: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue

    if op == 1:
        try:
            edad = int(input("Ingrese la edad: "))
        except ValueError:
            print("Edad inválida.")
            continue
        
        if edad < 10:
            print("Entra gratis")
        elif 10 <= edad < 18:
            print("El ticket cuesta $1000")
            total += 1000
        elif 18 <= edad < 65:
            print("El ticket cuesta $2000")
            total += 2000
        else:
            print("El ticket cuesta $1500")
            total += 1500

    elif op == 2:
        print("Total de compra")
        print("El total de la compra es $", round(total * 1.19, 2))

    elif op == 3:
        print("Salir")

    else:
        print("Seleccione una opción válida")




