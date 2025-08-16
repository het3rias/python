
# # bono=0
# # pago=0
# # total=0
# # sueldo=5000
# # posicion=int(input("ingrese en que posicion quedo el equipo:"))
# # if posicion <=3:
# #     pago=3000
# # elif posicion<=8:
# #     pago=2000
# # elif posicion>=9:
# #     pago=1000

# # goles=int(input("ingrese cuantos goles marco:"))
# # if goles<=3:
# #     bono+=4
# # elif goles<=6:
# #     bono+=6
# # elif goles>=7:
# #     bono+=8

# # var=sueldo*bono/100
# # total=sueldo+pago+var
# # print(f"el bono es de %{bono}")
# # print(f"el pago es de ${total}")



# # valicaciones de datos

# # email=input("Ingrese su email: ")

# #verifico si el caracter @ existe en mi variable

# # if "@" in email:
# #     print("La variable tiene formato mail")
# # else:
# #     print("La variable NO tiene formato mail")

# #validar una clave solo de nuemros enteros
# # while True:
# #     try:
# #         clave=int(input("Ingrese su clave"))
# #         break
# #     except Exception:
# #         print("Error, solo ingrese numeros")

# # validar una clave por su largo , por lo menos 5
# # clave=input("Ingrese su clave: ")

# # verifico que tenga al menos 5 caracteres
# # la funcion len() verifica el largo de un objeto
# # en este caso la variabble clave    
# # if len(clave)>=5:
# #     print("La clave tiene el largo correcto")
# # else:
# #     print("La clave debe tener el menos 5 caracteres")

# # ahora verifica que tenga al menos 5 y menor o igual a 12
# # if len(clave)>=5 and len(clave)<=12:
# #     print("La clave tiene el largo correcto")
# # else:
# #     print("La clave debe tener el menos 5 caracteres y menos de 12")
  
# # verifico si tengo mayusclas y/o minisculas
# # y tiene por lo menos un numero

# tieneMayus=False
# tieneMinus=False
# tieneNumero=False

# #hacemos un recorrido de cada letra en mi clave
# # for letra in clave:
# #     # verifico si la letra es mayuscula
# #     if letra.isupper():
# #         tieneMayus=True
# #     # verifico que la letra es minuscula
# #     if letra.islower():
# #         tieneMinus=True
# #     # verifico si tiene por lo meno un numero
# #     if letra.isdigit():
# #         tieneNumero=True
        
        
# # if tieneMayus:
# #     print("Tiene por lo menos una mayuscula")
# # else:
# #     print("NO Tiene por lo menos una mayuscula")
# # if tieneMinus:
# #     print("Tiene por lo menos una minuscula")
# # else:
# #     print("NO Tiene por lo menos una miniscula")

# # if tieneMayus and tieneMinus and tieneNumero:
# #     print("La clave esta ok")
# # else:
# #     print("Debe intentar nuevamente")

# # specials="!#$%&/()=?*{}[]"
# # clave="visa#"

# # for caracter in clave:
# #     if caracter in specials:
# #         print("Si es un cracter especial")
  
# clave="Tredf99"      
# def valida_pass(clave):
#     Mayuscula=False
#     Minuscula=False
#     Numero=False
#     for palabra in clave:
#         if palabra.isupper():
#             Mayuscula=True
#         if palabra.islower():
#             Minuscula=True
#         if palabra.isdigit():
#             Numero=True
#     if Mayuscula and Minuscula and Numero and len(clave)==6:
#         print("la clave está bien escrita")
#         return True
#     else:
#         print("la clave está mal escrita")
#         return False

# valida_pass(clave)
'''
Crear gestion de vehiculos
Crear programa para un parking de autos
se debe ingresar
Marca, año, patente, Tipo

Marca: tipo string, se debe tipear la marca
año: tipo int , solo de 4 digitos enteros
patente: debe tener 4 letras minusculas y 2 digitos
tipo: S= sedan, C= Camioneta, M= moto

Se deve validar cada aspecto y tener un mantenedor para 
todos los vehiculos motorizados

1.- Ingresar Vehiculo
2.- Mostrar Vehiculos
3.- Actualizar Vehiculo
4.- Marcar salida de Vehiculo con hora*
5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
6.- Salir

Usar dunciones con argumentos para poder validar
y para poder llamar las acciones dentro del menu
'''
from datetime import datetime
autos={
     1:{"marca":"toyota","año":2020,"patente":"afbg12","tipo":"camioneta","salida":None},   
     2:{"marca":"chebrolet","año":2025,"patente":"gayy69","tipo":"moto","salida":None},   
     3:{"marca":"ferrari","año":2017,"patente":"free07","tipo":"sedan","salida":None},   

}
def Ingresar(dict):
    while True:
        try:
            marca=str(input("ingrese la marca del vehiculo:"))
            if validanmarca(marca):
                break
            else:
                print("ERROR")
        except Exception:
            print("solo ingresar letras")
                

    while True:
        try:
            año=int(input("ingrese el año del vehiculo:"))
            if validaaño(año):
                break
            else:
                print("ERROR")
        except Exception:
            print("solo  4 digitos enteros ")
    while True:
        patente=input("ingrese la patente")
        if validaPatente(patente):
            break
        else:
            print("ERROR")
    while True:        
        tipo=input("ingrese el tipo(sedan,camioneta,moto) ")
        if tipo in ["sedan", "camioneta", "moto"]:
            largo=list(dict.keys())[-1]
            dict[largo+1]={"marca":marca,"año":año,"patente":patente,"tipo":tipo,"salida":None}
            break
        else:
            print("ERROR")


# def Muestra(dict):
#     for j, datos in dict.items():
#         print(j,datos)
def Muestra(dict):
    for id, datos in dict.items():
        salida = datos["salida"] if datos["salida"] else "En garaje"
        print(f"{id}: Marca: {datos['marca']}, Año: {datos['año']}, Patente: {datos['patente']}, Tipo: {datos['tipo']}, Salida: {salida}")


def validaaño(año):
    return isinstance(año, int) and 1000 <= año <= 9999

def validaPatente(patente):
    Minuscula=0
    Numero=0
    for palabra in patente:
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            Numero+=1
    if  Minuscula== 4 and Numero==2 and len(patente)==6:
        print("la patente está bien escrita")
        return True
    else:
        print("la patente está mal escrita(debe tener 4 letras minusculas y 2 digitos)")
        return False

def validanmarca(marca):
    return marca.isalpha()


def actualizar(dict):
    Muestra(dict)
    act=int(input("Seleccione el auto que va a  actualizar?: "))
    while True:
        print('''
                1.- Marca
                2.- Año 
                3.- Patente
                4.- Tipo
                5.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese la nueva marca")
                if validanmarca(n):
                    dict[act]["marca"]=n
                else:
                    print("marca no valido")
            case 2:
                n=int(input("ingresa el nuevo año"))
                if validaaño(n):
                    dict[act]["año"]=n
                else:
                    print("año no valido")
            case 3:
                n=input("ingrese la nueva patente")
                if validaPatente(n):
                    dict[act]["patente"]=n
                else:
                    print("patente no valida")
            case 4:
                n=input("ingrese el tipo(sedan,camioneta,moto) ")
                if n in ["sedan", "camioneta", "moto"]:
                    dict[act]["tipo"]=n
                else:
                    print("Tipo no válido.")
            case 5:
                break
            case _:
                    print("Opcion invalida")

def MarcarSalida(dict):
    try:
        id = int(input("Ingrese el ID del vehículo que sale: "))
        if id in dict and dict[id]["salida"] is None:
            dict[id]["salida"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Salida registrada a las {dict[id]['salida']}")
        else:
            print("ID no válido o el vehículo ya salió.")
    except:
        print("Error al registrar salida.")

def Estadisticas(dict):
    if not dict:
        print("No hay vehículos registrados.")
        return

    ultimo = max(dict.items(), key=lambda x: x[0])
    total_en_garage = sum(1 for datos in dict.values() if datos["salida"] is None)

    print("\n--- Estadísticas ---")
    print(f"Último vehículo ingresado: ID {ultimo[0]} - {ultimo[1]}")
    print(f"Total vehículos en garaje: {total_en_garage}")
    print("---------------------\n")

while True:
    op=int(input('''
    1.- Ingresar Vehiculo
    2.- Mostrar Vehiculos
    3.- Actualizar Vehiculo
    4.- Marcar salida de Vehiculo con hora*
    5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
    6.- Salir

'''))
    match op:
        case 1:
            Ingresar(autos)
        case 2:
            Muestra(autos)
        case 3:
            actualizar(autos)
        case 4:
            MarcarSalida(autos)
        case 5:
            Estadisticas(autos)
        case 6:
            print("saliendo...")
            break
        case _:
            print("debe ingresar una opcion valida")