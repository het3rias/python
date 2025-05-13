#MATCH

def suma():
    n1=int(input("Ingrese un numero:"))
    n2=int(input("Ingrese otro numero:"))
    print("el resultado de la suma es ",n1+n2)
def resta():
    n1=int(input("Ingrese un numero:"))
    n2=int(input("Ingrese otro numero:"))
    print("el resultado de la resta es ",n1-n2)    
def multiplicacion():
    n1=int(input("Ingrese un numero:"))
    n2=int(input("Ingrese otro numero:"))
    print("el resultado de la multiplicacion es ",n1*n2)   
def division():   
    try:
        n1=int(input("Ingrese un numero:"))
        n2=int(input("Ingrese otro numero:"))
        print("el resultado de la division es ",n1/n2)  
    except ZeroDivisionError:
        print("Se produjo un error")
def calcu():
    while True:
        op=int(input(''' seleccione su opcion
                1.-Suma
                2.-Resta
                3.-Multiplicacion
                4.-Division
                5.-Salir        
                '''))
        match op:
            case 1:
                print("Suma")
                suma()
            case 2:  
                print("Resta")
                resta()
            case 3:    
                print("Multiplicacion")
                multiplicacion()
            case 4:    
                print("division")
                division()
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")     
       
# _(funciona por si el usuario pone otro numero )

def peleas ():
    import random

    randy=random.randint(1,10)

    print(randy)
    import random
    turno=random.randint(1,2)

    vida1=50
    vida2=50
    combat1=str(input("ingrese su nombre:"))
    combat2=str(input("ingrese su nombre:"))

    while vida1>=0 or vida2>=0:
        daño=random.randint(2,10)
        if turno % 2==0:   
            print("turno de ",combat1)
            vida2-=daño
            print(f"vida {vida1} de:{combat1} ")
            print("daño ",daño)
        else:
            print("turno de ",combat2)
            vida1-=daño
            print(f"vida {vida2} de:{combat2} ")
            print("daño ",daño)
        turno+=1
def grupofamiliar():
    arancel=200000
    descuento=0
    var=0
    total=0
    print('''
        1.- La florida 20%
        2.- La pintana 30%
        3.- Puente alto 25%
        4.- San joaquin 15%
        ''')

    comuna=int(input("seleccione una comuna: "))
    grupoF=int(input("ingrese su grupo familiar(numero entero usted incluido):"))


    if comuna==1:
        descuento=20
    elif comuna==2:
        descuento=30
    elif comuna==3:
        descuento=25
    elif comuna==4:
        descuento=15

    if grupoF == 1:
        descuento+=2
    elif grupoF>=2 or grupoF>=4:
        descuento+=3
    elif grupoF>=5:
        descuento+=4

    var=arancel*descuento
    total=var/100
    arancel-=total
    print("el total del descuento es",descuento)
    print("el total a pagar es ", arancel)
def programas():
    while True:
        op=int(input(''' seleccione su opcion
                1.-calculadora
                2.-grupo familiar
                3.-peleas
                4.-Salir        
                '''))
        match op:
            case 1:
                print("calculadora")
                calcu()
            case 2:  
                print("grupo familiar")
                grupofamiliar()
            case 3:    
                print("pelas")
                peleas()
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")   
programas()  