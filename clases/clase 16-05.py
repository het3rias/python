
# while True:
#     try:
#         num=int(input("ingrese un numero mayor que 3:"))
#         if num>3:
#             break
#     except Exception:
#         print("solo debe ingresar numeros")
# total=0
# articulos=0
# nombre=""
# def compras():
#     global total,articulos
#     try:
#         while True:
#             op1=int(input('''ingrese opciones
#                         1.-coca cola $1000
#                         2.-papas $500
#                         3.-agua $700
#                         4.-salir
#                         '''))
#             match op1:
#                 case 1:
#                     print("coca cola ")
#                     total+=1000
#                     articulos+=1

#                 case 2:
#                     print("papas")
#                     total+=500
#                     articulos+=1
                    
#                 case 3:
#                     print("agua")
#                     total+=700
#                     articulos+=1
                    
#                 case 4:
#                     print("Saliendo...")
#                     break
#                 case _:
#                     print("Opcion invalida") 
#     except Exception:
#         print("solo ingrese numeros enteros mostrados en el menu")    
# def boleta():
#     global nombre,total,articulos
#     nombre=str(input("ingrese su nombre nuevamente"))
#     print(f'''
#         saludos {nombre}
#         precio total {total}
#         precio total mas IVA {total*1.19}
#         articulos comprados {articulos}
#           ''')
# def menu():
#     global nombre
#     while True:
#         try:
#             op=int(input(''' seleccione su opcion
#                     1.-ingresar nombre
#                     2.-comprar productos
#                     3.-sacar boleta
#                     4.-salir    
#                     '''))
#             match op:
#                 case 1:
#                     print("nombre")
#                     nombre=str(input("ingrese su nombre"))
#                     if nombre == "":
#                         print("El nombre no puede estar vacío.")
#                 case 2: 
#                     if nombre=="":
#                         print("debe ingresar nombre primero")
#                         return
#                     else:
#                         print("compras")
#                         compras()
#                 case 3:
#                     if nombre=="":
#                         print("debe ingresar nombre primero")
#                         return
#                     else:  
#                         print("boleta")
#                         boleta()
#                 case 4:
#                     print("Saliendo...")
#                     break
#                 case _:
#                     print("Opcion invalida")    
#         except Exception:
#             print("solo ingrese numeros enteros mostrados en el menu")  
# menu()        


def alumnos():
    global alumno,cantidadn,notas,promedio,prom,suma_promedios,promedio_curso

    alumno=int(input("ingresar numero de alumnos:"))
    suma_promedios = 0 
    for i in range(alumno):
        cantidadn=int(input(f"ingresar cantidad de notas del alumno {i+1}:"))
        prom=0
        for e in range(cantidadn):
            notas=int(input(f"ingresar nota {e+1} de alumno {i+1}:"))
            prom+=notas
            promedio=prom/cantidadn
            promedio=round(promedio,2)
        suma_promedios +=promedio
        if promedio>=4.0:
            print(f"aprobaste con {promedio}")
        else:
            print(f"reprobaste con {promedio} ")
        
    promedio_curso=round(suma_promedios/alumno,2)
    print(f"\n--- Promedio general del curso: {promedio_curso} ---")
    
alumnos()