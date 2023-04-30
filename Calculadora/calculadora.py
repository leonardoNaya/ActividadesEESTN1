#python 3
def introducirDatos(respuesta):
    n1=int(input("Introduzca el primer número"))
    n2=int(input("Introduzca el segundo número"))
    if respuesta==1:
        Suma(n1,n2)
        return 0
    if respuesta==2:
        Resta(n1,n2)
        return 0
    if respuesta==3:
        Multiplicacion(n1,n2)
        return 0
    if respuesta==4:
        Division(n1,n2)
        return 0
    if respuesta==5:
        Exponenciacion(n1,n2)
        return 0
    if respuesta==6:
        return 1
def Suma(n1, n2):
    res=n1+n2
    print(res)
def Resta(n1, n2):
    res=n1-n2
    print(res)
def Multiplicacion(n1, n2):
    res=n1*n2
    print(res)
def Division(n1, n2):
    res=n1/n2
    print(res)
def Exponenciacion(n1, n2):
    res=n1**n2
    print(res)
aux=0
while aux==0:
    print("----------------")
    print("Menú")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicación")
    print("4- División")
    print("5- Exponenciación")
    print("6- Salir")
    print("----------------")
    menuRespuesta=int(input("Introduzca el número para acceder a la operación"))
    aux = introducirDatos(menuRespuesta)