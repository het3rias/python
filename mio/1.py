# nombre = input("Por favor, ingrese su nombre: ")

# print("Hola,", nombre, "! Bienvenido a Python")

# edad = int(input("Ingrese su edad: "))

# print("Su edad es", edad)
total=0
autos=0
Full=0
Standard=0
basico=0
def MenuPago():
    global total, autos, Full, Standard, basico 
    while True:
        try:
            op=int(input('''
            Seleccione opcion
            1.Full $15.000
            2.Standard $10.000
            3.Basico $7.000
            4.salir
                        '''))
            match op:
                case 1:
                    total+=15000
                    autos+=1
                    Full+=1
                case 2:
                    total+=10000
                    autos+=1
                    Standard+=1
                case 3:
                    total+=7000
                    autos+=1
                    basico+=1
                case 4:
                    print("saliendo...")
                    break
                case _:
                    print("opcion invalida")
        except Exception():
            print("solo ingrese un numero entero")
def VentasDiarias():
    
    print(f'''
    Ventas Diarias
    Autos {autos}
    Total de ventas ${total}
    Full {Full}
    Standard {Standard}
    Basico {basico}
        ''')

while True:
        try:
            opciones=int(input('''
            Seleccione opcion
            1.Cursar pago del lavado
            2.Ventas diarias
            3.Salir
                                '''))
            match opciones:
                case 1:
                    MenuPago()
                case 2:
                    VentasDiarias()
                case 3:
                    print("saliendo...")
                    break
                case _:
                    print("Opcion invalida")
        except Exception:
            print("solo ingrese numeros enteros")

