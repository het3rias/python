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

clave1=1111
clave2=2222
clave3=3333

contraseña=0

bille5000=30
bille10000=30
bille20000=30

print('''
    1.-user 1
    2.-user 2
    3.-user 3
      ''')

op=int(input("ingrese usuario"))

if op==1:
    contraseña()
    while clave1!=contraseña:
        print("ingreso user 1")





