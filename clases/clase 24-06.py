def Muestra_Juegos(dict):
    for j, datos in dict.items():
        print(j,datos)
def AgregarJuego(dict):
    while True:
        nombre=input("ingrese le nombre del juego:")
        if validanombre(nombre):
            break
        else:
            print("deben ser al menos 2 palabras")
    while True:
        precio=int(input("ingrese precio(8.000,100.000)"))
        if validaprecio(precio):
            break
        else:
            print("error")
    while True:
        code=input("ingrese nuevamente:")
        if valida_code(code):
            largo=list(dict.keys())[-1]
            dict[largo+1]={"nombre":nombre,"precio":precio,"code":code}
            break
            
        else:
            print("juego no ingresado")
            

def Borrar(dict):
    Muestra_Juegos(dict)
    Borrar=int(input("seleccione le juego a borrar:"))
    del dict[Borrar]

     
def valida_code(clave):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4 and len(clave)==8:
        print("la clave está bien escrita")
        return True
    else:
        print("la clave está mal escrita")
        return False

def validaprecio(precio):
    
    if precio>8000 and precio<=100000:
        return True
    else:
        return False
def validanombre(nombre):
    
    if nombre[-1]!=" " and nombre[0]!=" ":
        for n in nombre:
            if n==" ":
                return True
    else:
        return False
    
def act_perros(dict):
    Muestra_Juegos(dict)
    act=int(input("Seleccione el juego a actulizar?: "))
    while True:
        print('''1.- Nombre
                2.- precio
                3.- Codigo
                4.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre")
                if validanombre(n):
                    dict[act]["nombre"]=n
                else:
                    print("nombre no valido")
            case 2:
                n=int(input("ingrese la nueva precio"))
                if validaprecio(n):
                    dict[act]["precio"]=n
                else:
                    print("precio no valido")
            case 3:
                n=input("ingrese el nuevo codigo")
                if valida_code(n):
                    dict[act]["code"]=n
                else:
                    print("el paramatro del codigo no es correcto")

            case 4:
                break
            case _:
                    print("Opcion invalida")

juegos={
    1:{"nombre":"Metroid dread",
       "precio":65000,
       "code":"MTdr2023"},
    2:{"nombre":"Mario",
       "precio":80000,
       "code":"MR2020"}
}




while True:
    op=int(input('''
    1.agregar juego
    2.mostrar juegos
    3.borrar juego
    4.actualizar juego
    5.salir
        '''))
    match op:
        case 1:
            AgregarJuego(juegos)
        case 2:
            Muestra_Juegos(juegos)
        case 3:
            Borrar(juegos)
        case 4:
            print("")
        case 5:
            print("saliendo..")
            break
        case _:
            print("ingrese opcion valida")