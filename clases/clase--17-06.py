# def Suma():
#     n1=int(input("ingrese un numero:"))
#     n2=int(input("ingrese otro numero:"))
    

#     print(n1+n2)


# Suma()

# def SumaRET():
#     n1=int(input("ingrese un numero:"))
#     n2=int(input("ingrese otro numero:"))
    
#     return n1+n2


# print(SumaRET()*5)

# def SumaArg(n1,n2):
#     print(n1+n2)

# num1=int(input("ingrese un numero:"))
# num2=int(input("ingrese un numero:"))
# SumaArg(8,10)

# def SumaArgRetunr(n1,n2):
#     return n1+n2

# num1=int(input("ingrese un numero:"))
# num2=int(input("ingrese un numero:"))

# print(SumaArgRetunr(num1,num2)*2)


# def IVA(n1,):
#     return n1*1.19
    
# print(IVA(1000))

# def Descuento(n1,n2):
    
#     return n1*n2/100

# num1=int(input("ingrese el precio:"))
# num2=int(input("ingrese el descuento:"))
# print("el descuento es:",Descuento(num1,num2))


productos=[
    {"nombre":"lapiz","precio":400},
    {"nombre":"goma","precio":500},
    {"nombre":"estuche","precio":1500}
]

# print(productos[1]["precio"])

# for item in productos:
#     print(f"el articulo {item["nombre"]} tiene un precio de {item["precio"]}")


def IngresarProducto():
    
    nombre=input("ingresar nombre del producto a agregar:")
    precio=int(input("ingresar precio del producto:"))
    nuevo={"nombre":nombre,"precio":precio}
    productos.append(nuevo)
    print(f"el producto {nombre} se agrego correctamente")

def BorarProducto():
    
    for item in range(len(productos)):
            print(f" {item+1} {productos[item]}  ")
    eliminar=int(input("ingresar la opcion:"))
    borrarnota= productos.pop(eliminar-1)
    print(f"el articulo{borrarnota} ha sido eliminado")

def ActualizarPrecio(act,nombre,precio):

    # nombre=input("ingrese el nombre:")
    # if item["nombre"]==nombre:
    #     precio=int(input("ingresa precio nuevo"))
    #     item["precio"]==precio
    #     print(f"el articulo {nombre} se actualizo {precio}")
    # else:
    #     print("no se encontro ")
    for n,producto in enumerate(productos):
        print(n+1, producto["nombre"],producto["precio"])

    productos[act-1]["nombre"]=nombre
    productos[act-1]["precio"]=precio        

while True:
    op=int(input('''
    1.- Agregar articulo
    2.- Borrar articulo
    3.- Actualizar artiulo
    4.- Mostrar listado de articulos
    5.- Salir
'''))
    
    match op:
        case 1:
            IngresarProducto()
        case 2:
            BorarProducto()
        case 3:
            for n,producto in enumerate(productos):
             print(n+1, producto["nombre"],producto["precio"])
            act=int(input("que articulo desea actualizar"))
            nombre=input("ingrese nombre ")
            precio=int(input("ingrese el precio:"))
            ActualizarPrecio(act,nombre,precio)
        case 4:
            for item in productos:
                print(f"el articulo {item["nombre"]} tiene un precio de {item["precio"]}")
        case 5:
            print("Saliendo...")
            break
        case _:
            print("ingresar opcion valida")