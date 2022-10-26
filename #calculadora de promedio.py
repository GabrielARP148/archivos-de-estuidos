#calculadora de promedio
#inicio clase 10
introducir_nombre=input("cual es tu nombre?: ")
print ("Hola, ", introducir_nombre, "veamos como te fue en tus calificaciones.")
examen1=float(input("examen 1: "))
examen2=float(input("examen 2: "))
examen3=float(input("examen 3: "))
promedio=(examen1+examen2+examen3)/3
if promedio==10 or promedio==9 or promedio==8:
    print("felicidades ", introducir_nombre, "aprobaste la materia: ", round(promedio,2))
    if promedio>10:
        print("nota inexistente")
elif promedio==7 or promedio==6:
    print("promocionastes la materia: ", round(promedio,2))
else:
    print(introducir_nombre, "no aprobaste la materia, suerte la promoxima: ", round(promedio,2))