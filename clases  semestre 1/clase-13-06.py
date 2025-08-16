# notas=[7.0,5.0,6.0]
# def IngresarNotas():
#     # global notas
#     # try:
#     #     notanueva=float(input("ingresar nota:"))
#     #     notas.append(notanueva)
#     #     if len(notanueva)>2:
#     #         print("La nota que ingreso supera los caracteres de una nota")
            
#     #     else:
#     #         print("La nota ha sido ingresada")
#     #         notas.append(notanueva)
#     # except Exception:
#     #     print("Ingresar solo numeros")
#     global notas
#     try:
#         while True: 
#             notanueva_str = input("Ingrese nota (entre 1.0 y 7.0): ")
#             try:
#                 notanueva = float(notanueva_str)
                
#                 if 1.0 <= notanueva <= 7.0:
#                     notas.append(notanueva)
#                     print(f"La nota {notanueva} ha sido ingresada.")
#                     break 
#                 else:
#                     print("Error: La nota debe estar entre 1.0 y 7.0.")
#             except ValueError:
#                 print("Error: Ingrese solo números para la nota.")
#     except Exception as e:
        
#         print(f"Ocurrió un error inesperado al ingresar la nota: {e}")

# def BorrarNota():
#     global notas
#     for i in range(len(notas)):
#         print(f"{i+1}.-{notas[i]} ")
#     indice=int(input("ingrese la nota que quiere borrar:"))
#     if 1<=indice<=len(notas):
#         borrarnota= notas.pop(indice-1)
#         print(f"La nota {borrarnota} ha sido borrada")
#     else:
#         print("la nota esta fuera de rango")

# def SacarPromedio():
#     global notas
#     if notas:
#         promedio= sum(notas)/ len(notas)
#         mayor=max(notas)
#         menor=min(notas)
#         print(f"el promedio de notas es {promedio}")
#         print(f"la nota mayor es {mayor}")
#         print(f"la nota menor es {menor}")
#     else:
#         print("No existen notas")
        
        

# def LimpiarNotas():
#     global notas
#     notas.clear()
#     print("las notas han sido borradas exitosamente")

# while True:
#     try:
#         op=int(input('''
#             1.- Ingresar nota
#             2.- Borrar nota
#             3.- Mostrar nota
#             4.- Sacar promedio, nota mayor y nota menor
#             5.- Limpiar todas las notas
#             6.- Salir
                    
#     '''))
#         match op:
#             case 1:
#                 IngresarNotas()
#             case 2:
#                 BorrarNota()
#             case 3:
#                 for i in range(len(notas)):
#                      print(f"{i+1}.-{notas[i]} ")
#             case 4:
#                 SacarPromedio()
#             case 5:
#                 LimpiarNotas()
#             case 6:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("ingrese una opcion valida")
#     except Exception:
#         print("ingresar solo numeros enteros")


# Diccionarios 
# dic={
#     "nombre":"Mel Broks",
#     "numero": 979780927,
#     "casado": True

# }


# # print(dic["numero"])


# dic["ciudad"]="Talca"
# for key,value in dic.items():
#     print(key,value)

# dic["casado"]=False


# print(dic["casado"])

frutas={
    "sandia": 3000,
    "manzana": 1500,
    "naranja": 1000
}
def IngresarFruta():
    global frutas
    print(frutas)
    fruta=input("ingrese una fruta:")
    precio=int(input("ingrese el precio:"))

    frutas[fruta]=precio
    print(f"fruta {fruta} ingresada y precio {precio} ingresado")


def Comprar():
    total=0
    while True:
        fruta=input("ingrese la fruta a comprar(o escriba fin para salir)")
        if fruta== "fin":
            break
        elif fruta in frutas:
            try:
                cantidad=float(input(f"Ingrese la cantidad de {fruta} en kg: "))
            except Exception:
                print("ingresar solo numeros")
    
            subtotal= frutas[fruta]*cantidad
            total +=subtotal
            print(f"Fruta {fruta} x {cantidad} kg = {subtotal}")
        else:
            print(f"La fruta {fruta} no esta ")
        print(f"El total a pagar es {total}")


while True:
    try:
        op=int(input('''
        1.- Ingresar fruta y precio
        2.- Actualizar precio
        3.- Borrar fruta y precio
        4.- mostrar todas las frutas y precios
        5.- Comprar
        6,. Salir
                    
    '''))
        match op:
            case 1:
                IngresarFruta()
            case 2:
                frutasactualizar=input("ingrese el nombre de la fruta a actualizar:")
                if frutasactualizar in frutas:
                    precio=int(input("ingrese el precio que desea"))
                    frutas[fruta]=precio
                    print(f"el precio de la {frutasactualizar} se actualizo a {precio}")
                else:
                    print(f"La fruta {frutasactualizar} no esta en la fruteria")
            case 3:
                fruta=input("ingrese el nombre de la fruta que desea borrar:")
                if fruta in frutas:
                    del frutas[fruta]
                    print(f"La fruta {fruta} ha sido eliminanda")
            case 4:
                for fruta,precio in frutas.items():
                    print(fruta,"$",precio)
            case 5:
                Comprar()
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("solo ingrese numeros enteros")