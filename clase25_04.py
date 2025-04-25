

# Votos   
# num=0
# num=int(input("ingrese el numero de votantes "))

# kaiser=0
# nose=0

# for i in range(num):

#     print("1. kaiser\n2.nose ")
#     voto=int(input("ingrese su voto: "))
#     if voto==1:
#         kaiser+=1
#     elif voto==2:
#         nose+=1
#     else:
#         print("ingrese opcion valida")
# print("los votos de kaiser son: ",kaiser)
# print("los votos de nose: ",nose)

# if kaiser>nose:
#     print("kaiser gana")
# elif nose>kaiser:
#     print("nose gana")
# else:
#     print("empate ")
# contar caracteres
# palabra=input("ingrese una palabra: ")
# cararct=0
# for i in palabra:
#     print(i)
#     cararct+=1
# print("los carateres son ",len{cararct})    

# time es para que el programa espere time.sleep(1)
 
# import time
# num=10
# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

# resp="no"
# while resp!="si":
#     resp=input("desea salir del programa: ")
#     break

# intentos=3
# clave=3344
# contraseña=int(input("ingrese su contraseña:"))

# while clave!=contraseña:
#     print("ERROR;clave invalida")
#     contraseña=int(input("ingrese su contraseña:"))
#     if intentos==1:
#         break
#     intentos-=1
#     print(f"quedan {intentos} 3intentos")
# if clave==contraseña:
#     print("clave aceptada\nbienvenido ")
# else:
#     print("bloqueado")
#tienda
# cant=0
# total=0
# op=0
# while op!=4: 
#     print("1-diazepam $9000")
#     print("2-metametazona $13000")
#     print("3-superocho $3000")
#     print("4-salir")
#     op=int(input("que producto llevara: "))

#     if op == 1:
#         print("usted llevara diazepam")
#         total+=9000
#     elif op==2:
#         print("usted llevara metametazona")
#         total+=13000
#     elif op==3:
#         print("usted llevara superocho")
#         total+=3000
#     else:
#         print("selecione 1,2,3 o 4")

# print("el total es ",total)


#pida al usuario numeros infinitamente y muestre si son par o impar

# num=5
# while num!=0:
#     num=int(input("ingrese un numero: "))
#     if num % 2==0:
#         print(f"el numero {num} es par")
#     else:
#         print(f"el numero {num} es impar")

# suma=0
# num=5
# while num!=0:
#     num=int(input("ingrese un numero: "))

#     suma+=num
# print("la suma es ",suma)
# sumaimpar=0
# sumapar=0
# num=5
# while num!=0:
#     num=int(input("ingrese un numero: "))
#     if num % 2==0:
#         print(f"el numero {num} es par")
#         sumapar+=1
#     else:
#         print(f"el numero {num} es impar")
#         sumaimpar+=1
# sumapar=sumapar-1
# print("el total de pares es ",sumapar)
# print("el total de impares es ",sumaimpar)


# print("/"*100)


#street figther
#peleas por turno daño entre 2 y 10
import random

# randy=random.randint(1,10)

# print(randy)
turno=random.randint(1,2)

combatientes=str
vida1=50
vida2=50

while vida1==0 or vida2==0:
    daño=random.randint(2,10)
    





