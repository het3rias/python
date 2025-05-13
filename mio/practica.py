### Ejercicios varios
# Nivel 2

#1 Pida al usuario un numero y clasifíquelo como par o impar, 
# muestre los pares e impares de el uno hasta ese numero
#ejercicio 1

# num = int(input("ingrese un numero: "))
# if num%2==0:
#     print("par")
# else:
#     print("impar")

# print("mostrar numeros pares")
# for i in range(1,num+1):
#     if i % 2 == 0:
#         print(i)

# print("mostrar numeros impares")
# for i in range(1,num+1):
#     if i % 2 != 0:
#         print(i)


# #2 Pida al usuario ingresar números, al final debe mostrar cuántos números
# #  se ingresaron y mostrar la suma de todos ellos, para terminar, debe poner
# #  la palabra salir
# cont = 0
# total = 0
# opc = 0
# while opc != 2:
#     print("1-Agregar nuevo numero")
#     print("2-Salir")
#     opc = int(input(":"))
#     if(opc == 1):
#         num = int(input("ingrese un numero: "))
#         cont+=1
#         total+=num
# print(f"la cantidad de numeros ingresados son {cont}")
# print(f"la suma de cada uno de ellos es {total}")



# #3 Pida al usuario ingresar un número y multiplícalo por un número al 
# # azar entre 2 y 8. Si 
# # el número es mayor que 50, logró la meta, si no, intente nuevamente
# from random import randint
# a = 0
# b = 0
# r = a*b
# while r < 50:
#     a = int(input("ingrese el valor de a : "))
#     b = randint(2,8)
#     r = a*b
#     print(f"el numero aleatorio es {b}")
#     print(f"la multiplicacion entre {a} x {b} = {r}")
#     if r < 50:
#         print("intente nuevamente!")
# print("LOGRO LA META!")


# #4 Ingresar un número positivo, multiplicarlo por 5, restarle 8, 
# # sumarle 3 y dividirlo por 2

# num = -1
# while (num < 0):
#     num = int(input("ingrese un número positivo: "))
#     if (num < 0):
#         print("Error, ingreso un número menor a 0, vuelva a intentarlo")
# print("numero ingresado exitosamente!")
# num = num*5  #num *= 5
# num = num-8  #num -= 8
# num = num+3  #num += 3
# num = num/2  #num /= 2
# print(f"el valor resultante es {num}")
# # 5 ADIVIDAR EL NUMERO#

# # Genere un numero Aleatoreo entre 1 y 50
# # Pida al usuario ingresar un numero
# # Si el numero ingresado es mayor muestre "El numero a adivinar es mayor"
# # de forma contraria escriba "El numero a adivinar es menor"
# # Hacer 2 versiones, una de intentos infinitos y otra con solo 5

# Pedir dia y mes de nacimiento y mostrar el signo zodiacal

dia=int(input("ingrese su dia de nacimiento"))
mes=int(input('''
ingrese su mes de nacimineto(ingrese numero)
1.-enero
2.-febrero
3.-marzo
4.-abril
5.-mayo
6.-junio
7.-julio
8.-agosto
9.-septiembre
10.-octubre
11.-noviembre
12.-diciembre
 '''))
if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "Piscis"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "Capricornio"
else:
    signo = "Fecha inválida"

print(f"Tu signo zodiacal es: {signo}")
