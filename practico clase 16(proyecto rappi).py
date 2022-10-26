#proyecto rappi
print("=============================================")
print("cuantos tiempo de vacaciones te corresponden")
print("============================================= \n")
print("por favor escriba area y clave")
nombre=input("instroduce tu nombre \n")
departamento=input("area: \n")
departamento=departamento.lower()
clave=int(input("contraseña: \n"))

print("=======================================")
if departamento=="atencion al cliente" and clave==123:
    print("===============================")
    print("beinvenido", nombre,  "de ", departamento)
    print("introduce los años de trabajos")
    años=float(input())
    print("=================================")
    if años==1:
        print("tienes ´6´ dias de vacaiones")
    elif años==2 or años<=6:
        print("tienes ´14´ días de vaciones")
    elif años>=7:
        print("tienes ´20´ días de vacaciones")
    else:
        print("no te corresponde vacaciones")
elif departamento=="logistica" and clave==321:
    print("bienvendio, ", nombre, "del ", departamento)
    print("introduce los años de trabajos")
    añosl=float(input())
    if añosl==1:
        print("te correpsonden ´7´ días de vacaciones")
    elif añosl==2 or añosl<=6:
        print("tienes ´15´ días de vacaicones")
    elif añosl>=7:
        print(" tienes ´22´ años de vacaciones")
    else:
        print("no te corresponde vacaciones")
elif departamento=="gerencia" and clave==4:
    print("=================================")
    print("Bievenidos, ", nombre, "del area de ", departamento)
    print("================================== \n")
    print("Por favor, introduce tus años de servicio")
    añosg=float(input())
    if añosg==1:
        print("tienes 10 dias de vacaciones")
    elif añosg==2 or añosg<=6:
        print("tienes 20 días de vacaciones")
    elif añosg>=7:
        print("tienes 30 días de vacaciones")
    else:
        print("no te corresponde vacaciones")
else:
    print("la clave o usuario son incorrectos ingresada es incorrecta")