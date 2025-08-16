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

# mio 
# pago=0
# total=0
# deuda=100000
# def PagoCupo():
#     global deuda,pago
#     try:
#         pago=int(input("ingrese un monto a pagar:"))
#         if pago >= 0:
#             print("monto exitoso")
#             if pago<=deuda:
#                 print("monto adecuado")
#                 deuda-=pago
#                 saldo+=pago
#                 print(f"pago exitoso deuda restante ${deuda} ")
#             else:
#                 print(f"el monto no debe superar el saldo actual ${deuda}")
#         else:
#             print("debe ser mayor o igual a cero")        
#     except Exception:
#         print("debe ingresar solo numeros enteros")
# def SimulacionDeCompra():
#     global deuda,total,pago
    
#     try:
#         compras_a_realizar=int(input("ingrese cuantas compras realizara:"))
#         for i in range(compras_a_realizar):
#             monto=int(input("ingrese el monto de la compra:"))
#             if monto>=0:
#                 total+=monto
#                 saldo=pago-monto
#             else:
#                 print("el monto debe ser mayor o igual a cero")
            
#             print(f"el saldo de la tarjeta es ${saldo}")
#     except Exception:
#         print("debe ingresar solo numeros enteros")

# while True:
#     try:
#         op=int(input('''
#         1. Pago de tarjeta de credito
#         2. Simulación de compras
#         3. salir 
#                     '''))
#         match op:
#             case 1:
#                 PagoCupo()
#             case 2:
#                 SimulacionDeCompra()
#             case 3:
#                 print("saliendo...")
#                 break
#             case _:
#                 print("opcion invalida, debe ingresar solo opciones que esten en el menu")
#     except Exception:
#         print("debe ingresar solo numeros enteros")

#coregido suspuestamente 
# deuda = 100000  # Deuda inicial
# total = 0       # Total gastado

# def PagoCupo():
#     global deuda
#     try:
#         pago = int(input("Ingrese un monto a pagar: "))
#         if pago < 0:
#             print("❌ El monto debe ser mayor o igual a cero.")
#         elif pago > deuda:
#             print(f"❌ El monto no debe superar la deuda actual (${deuda}).")
#         else:
#             deuda -= pago
#             print(f"✅ Pago exitoso. Deuda restante: ${deuda}")
#     except ValueError:
#         print("❌ Debe ingresar solo números enteros.")

# def SimulacionDeCompra():
#     global deuda, total
#     try:
#         compras_a_realizar = int(input("Ingrese cuántas compras realizará: "))
#         for i in range(compras_a_realizar):
#             monto = int(input(f"Ingrese el monto de la compra #{i+1}: "))
#             if monto < 0:
#                 print("❌ El monto debe ser mayor o igual a cero.")
#                 continue
#             if monto > deuda:
#                 print(f"❌ Saldo insuficiente. Deuda restante: ${deuda}")
#                 continue
#             deuda -= monto
#             total += monto
#             print(f"✅ Compra realizada por ${monto}. Saldo restante: ${deuda}")
#     except ValueError:
#         print("❌ Debe ingresar solo números enteros.")

# # Menú principal
# while True:
#     try:
#         op = int(input('''
#         ===== MENÚ PRINCIPAL =====
#         1. Pago de tarjeta de crédito
#         2. Simulación de compras
#         3. Salir
#         Seleccione una opción: '''))

#         match op:
#             case 1:
#                 PagoCupo()
#             case 2:
#                 SimulacionDeCompra()
#             case 3:
#                 print("👋 Saliendo del programa...")
#                 break
#             case _:
#                 print("❌ Opción inválida. Ingrese solo las opciones del menú.")
#     except ValueError:
#         print("❌ Error: Debe ingresar solo números enteros.")
         
        

#menu de usuarios
# usuario1=None
# usuario2=None
# usuario3=None
# contraseña1=None
# contraseña2=None
# contraseña3=None

# def Usuarios():
#     global  usuario1,usuario2,usuario3,contraseña1,contraseña2,contraseña3

#     while True:
#         try:
#             opcion=int(input('''
#                     Resgistro de usuarios
#                 1. Usuario 1
#                 2. Usuario 2
#                 3. Usuario 3
#                 4. Salir                    
#                             '''))
#             match opcion:
#                 case 1:
#                     try:
#                         usuario1=str(input("ingresar nombre de usuario "))
#                         contraseña1=int(input("ingresar contarseña (solo numeros enteros)"))
#                     except Exception:
#                         print("ingresar valores validos")
#                     print(f"nombre de usuario registrado {usuario1}")
#                 case 2:
#                     try:
#                         usuario2=str(input("ingresar nombre de usuario "))
#                         contraseña2=int(input("ingresar contarseña (solo numeros enteros)"))
#                     except Exception:
#                         print("ingresar valores validos")
#                     print(f"nombre de usuario registrado {usuario2}")
#                 case 3:
#                     try:
#                         usuario3=str(input("ingresar nombre de usuario "))
#                         contraseña3=int(input("ingresar contarseña (solo numeros enteros)"))
#                     except Exception:
#                         print("ingresar valores validos")
#                     print(f"nombre de usuario registrado {usuario3}")
#                 case 4:
#                     print("Volviendo al menú principal...")
#                     break
#                 case _:
#                     print("ingrese opcion valida")
#         except Exception:
#             print("ingrese solo numeros enteros")

# def ValidarSesion(usuario,contraseña):
#     return(
#         (usuario==usuario1 and contraseña==contraseña1)or
#         (usuario==usuario2 and contraseña==contraseña2)or
#         (usuario==usuario3 and contraseña==contraseña3)
#            )
        
# def InicioSesion():
#     global  usuario1,usuario2,usuario3,contraseña1,contraseña2,contraseña3


#     while True:
#         try:                    
#             if usuario1==None and usuario2==None and usuario3==None: 
#                 print("debe registrar un usuario")
#                 break
#             else:
#                 usuario=str(input("ingrese usuario:"))
#                 contraseña=int(input("ingrese contraseña"))
#                 if ValidarSesion(usuario,contraseña):
#                     print(f"bienvenido {usuario}")
#                     break
#                 else:
#                     print("usuario o contraseña incorrectos")

#         except Exception:
#             print("ingresar valores correctamente")

# def MenuDeUsuario():
#     InicioSesion()
#     while True:
#         try:

#                     op=int(input('''
#                             1. Realizar llamada
#                             2. Enviar correo electronico
#                             3. salir 
#                                     '''))
#                     match op:
#                         case 1:
#                                 celular = input("Ingrese número de celular (debe comenzar con 9 y tener 9 dígitos): ")
#                                 if celular.startswith("9") and len(celular) == 9 and celular.isdigit():
#                                     print("Llamada realizada con éxito.")
#                                 else:
#                                     print("Número inválido.")
#                         case 2:
#                             while True:
#                                 correo=input("ingrese correo:")
#                                 if "@" in correo:
#                                     break
#                                 else:
#                                     print("el correo debe tener @ , intente nuevamente")
#                             mensaje=input("Ingrese mensaje a enviar:")
#                             print(f"Correo enviado a {correo} con mensaje: {mensaje}")
                            
#                         case 3:
#                             print("cerrando sesion... ")
#                             break
#                         case _:
#                             input("debe ingresar opcion valida")


#         except Exception:
#                 print("ingresar solo numeros enteros")

# def menu():
#     global  usuario1,usuario2,usuario3,contraseña1,contraseña2,contraseña3
#     while True:
#         try:
            
#                 opciones=int(input('''
#                             1. Iniciar sesion
#                             2. registrar usuario
#                             3. salir
#                                     '''))
#                 match opciones:
#                     case 1:
#                         MenuDeUsuario()
#                     case 2:
#                         Usuarios()
#                     case 3:
#                         print("saliendo...")
#                         break
#                     case _:
#                         print("ingresar opcion valida")
#         except Exception:
#             print("debe ingresar solo numeros enteros")

# menu()


usuarios = []
contraseñas = []

def Usuarios():
    while True:
        try:
            print("\nRegistro de usuario:")
            usuario = input("Ingresar nombre de usuario: ")
            
            # Verificamos que no se repita el usuario
            if usuario in usuarios:
                print("Ese nombre de usuario ya está registrado. Intenta con otro.")
                continue

            contraseña = int(input("Ingresar contraseña (solo números enteros): "))
            
            usuarios.append(usuario)
            contraseñas.append(contraseña)
            print(f"Nombre de usuario registrado: {usuario}")
        except ValueError:
            print("Ingresar valores válidos (contraseña numérica)")
        
        opcion = input("¿Deseas registrar otro usuario? (s/n): ").lower()
        if opcion != "s":
            break



def ValidarSesion(usuario, contraseña):
    for i in range(len(usuarios)):
        if usuarios[i] == usuario and contraseñas[i] == contraseña:
            return True
    return False


def InicioSesion():
    if not usuarios:
        print("Debe registrar un usuario primero.")
        return False

    while True:
        try:
            usuario = input("Ingrese usuario: ")
            contraseña = int(input("Ingrese contraseña: "))
            if ValidarSesion(usuario, contraseña):
                print(f"Bienvenido {usuario}")
                return True
            else:
                print("Usuario o contraseña incorrectos.")
        except ValueError:
            print("Ingresar valores válidos")


def MenuDeUsuario():
    if not InicioSesion():
        return

    while True:
        try:
            op = int(input('''
                    1. Realizar llamada
                    2. Enviar correo electrónico
                    3. Salir
            '''))

            match op:
                case 1:
                    celular = input("Ingrese número de celular (debe comenzar con 9 y tener 9 dígitos): ")
                    if celular.startswith("9") and len(celular) == 9 and celular.isdigit():
                        print("Llamada realizada con éxito.")
                    else:
                        print("Número inválido.")
                case 2:
                    while True:
                        correo = input("Ingrese correo: ")
                        if "@" in correo:
                            break
                        else:
                            print("El correo debe contener '@', intente nuevamente.")
                    mensaje = input("Ingrese mensaje a enviar: ")
                    print(f"Correo enviado a {correo} con mensaje: {mensaje}")
                case 3:
                    print("Cerrando sesión...")
                    break
                case _:
                    print("Debe ingresar una opción válida.")
        except ValueError:
            print("Debe ingresar solo números enteros.")


def menu():
    while True:
        try:
            opciones = int(input('''
                1. Iniciar sesión
                2. Registrar usuario
                3. Salir
            '''))

            match opciones:
                case 1:
                    MenuDeUsuario()
                case 2:
                    Usuarios()
                case 3:
                    print("Saliendo...")
                    break
                case _:
                    print("Ingrese una opción válida.")
        except ValueError:
            print("Debe ingresar solo números enteros.")

menu()        