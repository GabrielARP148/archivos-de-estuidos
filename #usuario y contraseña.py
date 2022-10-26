#usuario y contraseña
from __future__ import barry_as_FLUFL


print("por favor cree un usuario")
usuario=input()
print ("por favor inserte una contraseña")
contraseña=input()
print("verificar contraseña")
contador=0
contador2=0
while contador<=3:
    contador+=1
    verificador=input()
    if verificador==contraseña:
        print("la contrseña es la misma")
        print("su cuenta se creo con exito")
        print("redireccionando")
        while contador2<=3:
            contador2+=1
            login=input("inserte usuario: \n")
            code=input("inserte contraseña: \n")
            if login==usuario and code==contraseña:
                print("acceso completado")
                break
            elif contador==3:
                print("su cuenta está suspendida")
                break
            else:
                print("usuario o contraseña incorrecto")
                continue
    elif contador==3:
        print("se ha quedado sin intentos")
        break
    else:
        print("la contraseña no es la misma")
        print("vuelva a insertar la contraseña: ")
        continue
print("fin de ejecución")