# import random
# import time

# numAzar=random.randint(1,50)
# print(numAzar)


# if numAzar>=20:
#     print("puede pasar")
# else:
#     print("no puede pasar")



# num=int(input("ingresar un numero "))

# while num!=numAzar:
    
#     if num>numAzar:
#         print("el numero a adivinar es menor")
#     elif num<numAzar:
#         print("el numero a adivinar es mayor")
#     num=int(input("ingresar un numero "))    
# print("numero adivinado")
#Ludo
# import random
# import time
# meta=30
# turno=1
# j1=0
# j2=0
# while  j1<meta and j2<meta:
#     if turno % 2==0:
#         print("turno J1")
#         time.sleep(1)
#         dado=random.randint(1,6)
#         j1+=dado
#         print("El J1 saco ",dado)
#         print("Avanaza a la casilla ", j1)
#     else:
#         print("turno J2")
#         time.sleep(1)
#         dado=random.randint(1,6)
#         j2+=dado
#         print("El J2 saco ",dado)
#         print("Avanaza a la casilla ", j2)
#     turno+=1
# if j1>=meta:
#     print("ganador J1")
# else:
#     print("ganador J2")


#Grupo familiar
# arancel=200000
# descuento=0
# var=0
# total=0
# print('''
#     1.- La florida 20%
#     2.- La pintana 30%
#     3.- Puente alto 25%
#     4.- San joaquin 15%
#       ''')

# comuna=int(input("seleccione una comuna: "))
# grupoF=int(input("ingrese su grupo familiar(numero entero usted incluido):"))


# if comuna==1:
#     descuento=20
# elif comuna==2:
#     descuento=30
# elif comuna==3:
#     descuento=25
# elif comuna==4:
#     descuento=15

# if grupoF == 1:
#     descuento+=2
# elif grupoF>=2 or grupoF>=4:
#     descuento+=3
# elif grupoF>=5:
#     descuento+=4

# var=arancel*descuento
# total=var/100
# arancel-=total
# print("el total del descuento es",descuento)
# print("el total a pagar es ", arancel)

# clave1=1111
# clave2=2222
# clave3=3333
# retiro=0

# op=0
# op2=0
# bille5000=30
# bille10000=30
# bille20000=30




# while op!=4:
#     op2=0
    
#     if op==1:
#         bille5000=30
#         bille10000=30
#         bille20000=30
#         contraseña=int(input("ingrese contraseña"))
#         while clave1!=contraseña:
#             print("contraeña invalida; intente nuevamente")
#             contraseña=int(input("ingrese contraseña"))
#         while op2!=4:     
#             print(f'''
#             billetes disponibles (para retirar marcar numero del billete)
#             1.-$5000 = {bille5000}
#             2.-$10000 = {bille10000}
#             3.-$20000 = {bille20000}
#             4.-salir
#             opciones de retiro
            
#               ''')
#             op2=int(input("ingrese opcion:"))
#             if op2==1:
#                 retiro=int(input("ingresar numero de billetes a retirar "))
#                 if bille5000>=retiro:
#                     bille5000-=retiro
#                     print(f"usted retiro {retiro} billetes de $5000 ")
#                 else:
#                     print("saldo no disponible")
                
#             elif op2==2:
#                 retiro=int(input("ingresar numero de billetes a retirar "))
#                 if bille10000>=retiro:
#                     bille10000-=retiro
#                     print(f"usted retiro {retiro} billetes de 10000 ")
#                 else:
#                     print("saldo no disponible")
#             elif op2==3:
#                 retiro=int(input("ingresar numero de billetes a retirar "))
#                 if bille20000>=retiro:
#                     bille20000-=retiro
#                     print(f"usted retiro {retiro} billetes de $20000 ")
#                 else:
#                     print("saldo no disponible")
#             elif op2==4:
#                 print("saliendo...")
#     elif op==2:
#         bille5000=30
#         bille10000=30
#         bille20000=30
#         contraseña=int(input("ingrese contraseña"))
#         while clave2!=contraseña:
#             print("contraeña invalida; intente nuevamente")
#             contraseña=int(input("ingrese contraseña"))
#         while op2!=4:     
#             print(f'''
#             billetes disponibles (para retirar marcar numero del billete)
#             1.-$5000 = {bille5000}
#             2.-$10000 = {bille10000}
#             3.-$20000 = {bille20000}
#             4.-salir
#             opciones de retiro
            
#               ''')
#             op2=int(input("ingrese opcion:"))
#             if op2==1:
#                 retiro=int(input("ingresar numero de billetes a retirar "))
#                 if bille5000>=retiro:
#                     bille5000-=retiro
#                     print(f"usted retiro {retiro} billetes de $5000 ")
#                 else:
#                     print("saldo no disponible")
                
#             elif op2==2:
#                 retiro=int(input("ingresar numero de billetes a retirar "))
#                 if bille10000>=retiro:
#                     bille10000-=retiro
#                     print(f"usted retiro {retiro} billetes de $10000 ")
#                 else:
#                     print("saldo no disponible")
#             elif op2==3:
#                 retiro=int(input("ingresar numero de billetes a retirar "))
#                 if bille20000>=retiro:
#                     bille20000-=retiro
#                     print(f"usted retiro {retiro} billetes de $20000 ")
#                 else:
#                     print("saldo no disponible")
#             elif op2==4:
#                 print("saliendo...")   
#     elif op==3:
#         bille5000=30
#         bille10000=30
#         bille20000=30
#         contraseña=int(input("ingrese contraseña"))
#         while clave3!=contraseña:
#             print("contraeña invalida; intente nuevamente")
#             contraseña=int(input("ingrese contraseña"))
#         while op2!=4:     
#             print(f'''
#             billetes disponibles (para retirar marcar numero del billete)
#             1.-$5000 = {bille5000}
#             2.-$10000 = {bille10000}
#             3.-$20000 = {bille20000}
#             4.-salir
#             opciones de retiro
            
#               ''')
#             op2=int(input("ingrese opcion:"))
#             if op2==1:
#                 retiro=int(input("ingresar numero de billetes a retirar "))
#                 if bille5000>=retiro:
#                     bille5000-=retiro
#                     print(f"usted retiro {retiro} billetes de $5000 ")
#                 else:
#                     print("saldo no disponible")
                
#             elif op2==2:
#                 retiro=int(input("ingresar numero de billetes a retirar "))
#                 if bille10000>=retiro:
#                     bille10000-=retiro
#                     print(f"usted retiro {retiro} billetes de $10000 ")
#                 else:
#                     print("saldo no disponible")
#             elif op2==3:
#                 retiro=int(input("ingresar numero de billetes a retirar "))
#                 if bille20000>=retiro:
#                     bille20000-=retiro
#                     print(f"usted retiro {retiro} billetes de $20000 ")
#                 else:
#                     print("saldo no disponible")
#             elif op2==4:
#                 print("saliendo...")
#     elif op==4:
#         print("saliendo del cajero...")
#     print('''
#     1.-user 1
#     2.-user 2
#     3.-user 3
#     4.-salir
#       ''')
#     op=int(input("ingrese opcion:"))


# claves = {
#     1: 1111,
#     2: 2222,
#     3: 3333
# }


# bille5000 = 30
# bille10000 = 30
# bille20000 = 30

# def menu_retiro():
#     global bille5000, bille10000, bille20000
#     op2 = 0
#     while op2 != 4:
#         print(f'''
#         Billetes disponibles (para retirar marque el número del billete):
#         1.- $5000   = {bille5000}
#         2.- $10000  = {bille10000}
#         3.- $20000  = {bille20000}
#         4.- Salir
#         ''')
#         op2 = int(input("Ingrese opción: "))
#         if op2 == 1:
#             retiro = int(input("Ingrese número de billetes a retirar: "))
#             if bille5000 >= retiro:
#                 bille5000 -= retiro
#                 print(f"Usted retiró {retiro} billetes de $5000")
#             else:
#                 print("Saldo no disponible")
#         elif op2 == 2:
#             retiro = int(input("Ingrese número de billetes a retirar: "))
#             if bille10000 >= retiro:
#                 bille10000 -= retiro
#                 print(f"Usted retiró {retiro} billetes de $10000")
#             else:
#                 print("Saldo no disponible")
#         elif op2 == 3:
#             retiro = int(input("Ingrese número de billetes a retirar: "))
#             if bille20000 >= retiro:
#                 bille20000 -= retiro
#                 print(f"Usted retiró {retiro} billetes de $20000")
#             else:
#                 print("Saldo no disponible")
#         elif op2 == 4:
#             print("Saliendo del menú de retiro...")
#         else:
#             print("Opción inválida")


# op = 0
# while op != 4:
#     print('''
#     === MENÚ PRINCIPAL ===
#     1.- Usuario 1
#     2.- Usuario 2
#     3.- Usuario 3
#     4.- Salir
#     ''')
#     op = int(input("Ingrese opción: "))

#     if op in [1, 2, 3]:
#         contraseña = int(input("Ingrese contraseña: "))
#         while contraseña != claves[op]:
#             print("Contraseña inválida; intente nuevamente.")
#             contraseña = int(input("Ingrese contraseña: "))
#         menu_retiro()
#     elif op == 4:
#         print("Saliendo del cajero...")
#     else:
#         print("Opción inválida")


