#usuario y contraseña
from ctypes import HRESULT
from weakref import ref


print("por favor cree un usuario")
usuario=()
print ("por favor inserte una contraseña")
contraseña=input()
print("verificar contraseña")
verificación=input()
if contraseña==verificación:
    print("la contrseña es la misma")
else:
    print("la contraseña no es la misma")
print("su usuario y contraseña fueron creado con exito")
print("por favor inserte usuario y contraseña")
login=input("usuario: ")
code=input("contraseña: ")
if usuario==login and code==contraseña:
    print("acceso consedido:")
    ref
elif usuario!=login:
    print ("el usuario es invalido")
elif contraseña!=code:
    print("la contraseña es incorrecta")
else:
    print("usario y contraseña falso")
range