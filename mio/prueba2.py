total=0

edad=0
op=0



while op !=3:
 print("bievenido ")
 print("1.comprar ticket")
 print("2.terminar compra")
 print("3.salir")

 op=int(input("ingrese opcion:"))

 if op == 1:
    edad=int(input("ingrese edad:"))

    if edad<10:
        print("ticket gratis")
    elif 10<=edad<18:
        print("el ticket cuesta $1000")
        total+=1000
    elif 18<=edad<65:
        print("el ticket cuesta $2000")
        total+=2000
    else:
        print("el ticket cuesta $1500")
        total+=1500 
 elif op==2:   
    print("el total de la compra")   
    print("el total es $",(total*1.19))  
 elif op==3:
    print("salir")
 else:
    print("ingrese opcion valida")

    

       




