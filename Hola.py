# # declaracion de variables
# nombre="Link"
# edad=21
# # ejemplo de concatenacion
# print("Hello,",nombre,"su edad es ",edad )
# ingreso de variables para concadenar
# print("ingrese su nombre")
# nombre=input()
# print("ingrese su edad")
# edad=input()
# print("Hola,",nombre,"su edad es ",edad )

# ingreso de variables para sumar int
# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# print(n1+n2)

# multiplicacion de dos numeros
# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# print("la multiplicacion es ",(n1*n2))

# promdedio de tres numeros 
# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# n3=int(input("ingrese un numero "))


# promedio=(n1+n2+n3)/3
# print("el promedio es ",promedio)

# if promedio>=4.0:
#     print("el alumno aprobo")
# else:
#      print("el alumno reprobo")

# edad=int(input("ingrese su edad "))
# if edad>=18:
#     print("es mayor de edad")
# else:
#     print("es menor de edad")



edad=int(input("ingrese su edad "))

if edad<12:
    print("es usted un niño")
elif edad>=12 and edad<18: # else if
 print("es usted un adolecente")
elif edad>=18 and edad<65:
   print("es usted un adulto")
else:
   print("es usted un adulto mayor ")

