#prueba de agregar lista
from contextlib import redirect_stderr
from timeit import repeat
from turtle import clear


mi_lista=[1, 2, 3, 4]
print ("tu lista actuales es: ", mi_lista)
mi_lista.append(int(input("inserte un numero entero para agregar a la lista: ")))
print("tu lista actualizada ahora es: ", mi_lista)

#usuario y contraseña
print ("bienvenido, vamos a crear un usuario y contraseña")
usuario=input("inserte un usurio: ")
contraseña=input("cree una contraseña por favor: ")
comparación=input("repita la contraseña: ")
if contraseña==comparación:
    print("la contraseña es correcta")
    if usuario==input("inserte Usuario: ") and contraseña==input("inserte contraseña: "):
        print("accedo concedido")
    else:
        print("usuario o contraseña no es valido")
else:
    print("la contraseña no son iguales")