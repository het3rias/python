
#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}
#stock = {modelo: [precio, stock], ...]

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 
}



def stock_marca(marca):
    for j,datos in productos.items(): 
        if marca==productos[j][datos]:
            for i in range(len(stock)):
                print(f" el stock es {stock[i]}  ")

def mustra_modelos():
    for  datos in productos.items():
        
        print(f" Marca: {datos['marca']}, Modelo: {datos['modelo']}")

def busqueda_por_precio(p_min, p_max):

    if stock() > p_min and stock() < p_max:
        print(f"los notebooks entre los precios consultas son{stock}")
        
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo,p):
    if modelo in stock():
        stock[p][1]=p
        modelo=True
    else:
        modelo=False 
    





while True:
    op=int(input('''
    *** MENU PRINCIPAL ***
    1. Stock marca.
    2. Búsqueda por precio.
    3. Actualizar precio.
    4. Salir.

    '''))
    match op:
        case 1:
            marca=str(input("ingresa el nombre de la marca "))
            stock_marca(marca)
        case 2:
                while True:
                    try:
                        p_min=int(input("ingrese el primer rango de precio"))
                        break
                    except Exception:
                        print("Debe ingresar valores enteros")

                while True:
                    try:
                        p_max=int(input("ingrese el primer rango de precio"))
                        break
                    except Exception:
                        print("Debe ingresar valores enteros")
                    busqueda_por_precio(p_min,p_max)
        case 3:
            
            modelo=input("ingrese el modelo")
            p=int(input("ingrese el precio"))
            actualizar_precio(modelo,p)
        case 4:
            print("Programa finalizado")
            break
        case _:
            print("Debe seleccionar una opción válida!!")