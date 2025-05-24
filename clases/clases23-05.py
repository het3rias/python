# total=0

# descuento=0

# productot=0
# producto1=0
# producto2=0
# producto3=0
# producto4=0
# respuesta=""
# def menucompra():
#     global total,productot,producto1,producto2,producto3,producto4

#     while True:
#         try:
#             op=int(input('''
#             "tipos de sushi"
#             1. Pokachu Roll $4500
#             2. Otaku Roll $5000
#             3. Pulpo Venenoso Roll $5200
#             4. Anguila Eléctrica Roll $4800 
#             5. Volver
#             '''))
#             match op:
#                 case 1:
#                     total+=4500
#                     productot+=1
#                     producto1+=1
#                 case 2:
#                     total+=5000
#                     productot+=1
#                     producto2+=1
#                 case 3:
#                     total+=5200
#                     productot+=1
#                     producto3+=1
#                 case 4:
#                     total+=4800
#                     productot+=1
#                     producto4+=1
#                 case 5:
#                     break
#                 case _:
#                     print("Opcion invalida")
#         except Exception:
#             print("ingresar solo numeros enteros que salgan en el menu")

# def boleta():
#                 global respuesta, descuento
#                 try:
#                     while True:
#                         respuesta=str(input("ingresar codigo:"))
#                         if respuesta =="soyotaku":
#                             descuento=total*10/100
#                             break
#                         elif respuesta == "x":
#                             break
#                         else:
#                             print("opcion invalida")
#                 except Exception:
#                     print("ingresar solo palabras")
#                 print(f'''
#                     ******************************
#                 TOTAL PRODUCTOS:{productot}
#                 ******************************

#                 Pikachu Roll : {producto1}
#                 Otaku Roll : {producto2}
#                 Pulpo Venenoso Roll: {producto3}
#                 Anguila Eléctrica Roll: {producto4}
#                 ******************************
#                 Subtotal por pagar: ${total}
#                 Descuento por código: ${descuento}
#                 TOTAL: ${total-descuento}

#                     ''')

# while True:
#     try:
#         op1=int(input('''
#             menu de opciones
#         1. menu de rolls
#         2. boleta
#         3. salir           
#         '''))
#         match op1:
#             case 1:
#                 menucompra()
#             case 2:
#                 boleta()
#             case 3:
#                 print("saliendo...")
#                 break
#             case _:
#                 print("opcion invalida")
#     except Exception:
#         print("ingrese solo numeros enteros que salgan en el menu")    


deuda=100000
def PagoCupo():

    pago=int(input("ingrese un monto a pagar(debe ser mayor o igual a cero)"))
    if pago >= 0:

