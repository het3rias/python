cant=0
total=0
op=0

cant=int(input("cuantos producots llevara: "))

for i in range(cant):

    print("que producto llevara: ")
    print("1-diazepam $9000")
    print("2-metametazona $13000")
    print("3.-superocho $3000")
    op=int(input("seleccione una opcion"))

    if op == 1:
        print("usted llevara diazepam")
        total+=9000
    elif op==2:
        print("usted llevara metametazona")
        total+=13000
    elif op==3:
        print("usted llevara superocho")
        total+=3000
    else:
        print("selecione 1,2 o 3")

print("el total es ",total)

