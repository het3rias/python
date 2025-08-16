# uso  y ejemplo de lista
# numeros=[7,5,33,24,1]
#      0 1 2  3  4 

# print(numeros[4])

# for numero in numeros:
#     print(numero)

# print(numeros)

# numeros.append(64)

# print(numeros)

# numeros.insert(3,100)
# print(numeros)
# frutas=["Manzana","Mango","Membrillo"]


# for fruta in frutas:
#     print (fruta)

# nombres=[]
# apellidos=[]
# while True:
#     op=int(input('''
#         1.- Insertar nombre y apellido
#         2.- Mostrar nombres y apellidos
#         3.- Buscar nombres
#         4.- Salir
#         '''))
#     match op:
#         case 1:
#                 nom=input("ingrese un nombre:")
#                 nombres.append(nom)
#                 ape=input("ingresar apellidos:")
#                 apellidos.append(ape)
#         case 2:
#               for nombre,apellido in zip (nombres,apellidos):
                   
                   
#                    print(nombre+" "+apellido)
                   
#         case 3:
#               nom=input("ingrese nombre:")
#               if nom in nombres:
#                    print(f"el nombre {nom} existe")
#               else:
#                    print("el nombre no existe")
#                 # contador=0
#                 # for nombree in nombres:
#                 #      contador+=1
#                 #      print(f"{contador} ",nombree)

#         case 4:
#             print("Saliendo...")
#             break
#         case _:
#             print("opcion invalida")


# Carrito 3.0

productos=["Pan","Leche","Platano"]
precios=[150,900,250]
carrito=[]

def MostrarProductos():
    print("Productos disponibles")
    for i in range(len(productos)):
        print(f"{i+1}.-{productos[i]} - ${precios[i]} ")

def IngresarProducto():
    producto=input("ingresar nombre del producto")
    precio=int(input("ingresar precio del producto"))
    productos.append(producto)
    precios.append(precio)
    print(f"el producto {producto} fue ingresado con exito")


def Compra():
    MostrarProductos()
    opcion=int(input("ingese el numero del prodcuto que desea:"))
    if 1 <= opcion <= len(productos):
        carrito.append(opcion-1)
        print(f"agregaste {productos[opcion-1]} al carrito")
    else:
        print("opcion fuera de rango")

def Boltea():
    if not carrito:
        print("El carrito esta vacio")
        return
    print((" BOLETA"))
    total=0
    for i in carrito:
        print(f"{productos[i]} - ${precios[i]}")
        total +=precios[i]
    print(f"Total a pagar: ${total}")
    print("Gracias por su compra")


while True:
    op=int(input('''
        1.- Ingresar productos
        2.- Comprar
        3.- Crear boleta
        4.- Salir
                 
            '''))
    match op:
        case 1:
            IngresarProducto()
        case 2:
            Compra()
        case 3:
            Boltea()
        case 4:
            print("Saliendo...")
            break
        case _:
            print("opcion invalida")



