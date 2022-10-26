#conversor de numeros
from sqlite3 import enable_shared_cache


print("--------------------------------------------")
print("presione 1 para convertir de numero a letras")
print("---------------------------------------------")
print("presione 2 para convertir de letras a numeros")
print("---------------------------------------------")
opciones=int(input("inserte opción: "))
if opciones==1:
    print("----------------------------------")
    print("convertir numeros a letras abierto")
    print("----------------------------------")
    numero=int(input("inserte numero a convertir: "))
    if numero==1:
        print("el numero ingresado es ´uno´")
    elif numero==2:
        print("el numero ingresado es ´dos´")
    elif numero==3:
        print("el numero ingresado es ´tres´")
    elif numero==4:
        print("el numero ingresado es ´cuatro´")
    elif numero==5:
        print("el numero ingresado es ´cinco´")
    elif numero==0:
        print("el numero es ´cero´")
    else:
        print("el valor ingresado no existe aún")
elif opciones==2:
    print("---------------------------------------")
    print("convertidor de letras a numeros abierto")
    print("---------------------------------------")
    letras=input("escriba el numero en letras: ")
    letras=letras.lower()
    if letras=="uno":
        print("la palabra escrita es ´1´")
    elif letras=="dos":
        print("la palabra escrita es ´2´")
    elif letras=="tres":
        print("la palabra escrita es ´3´")
    elif letras=="cuatro":
        print("la palabra escrita es ´4´")
    elif letras=="cinco":
        print("la palabra escrita es ´5´")
    else:
        print("el valor insertado no existe")
else:
    print("opción inexistente")
