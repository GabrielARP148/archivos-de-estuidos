introducir_nombre=input("cual es tu nombre?: ")
print ("Hola, ", introducir_nombre, "veamos como te fue en tus calificaciones.")
examen1=float(input("examen 1: "))
examen2=float(input("examen 2: "))
examen3=float(input("examen 3: "))
promedio=(examen1+examen2+examen3)//3
if promedio==float(10) or promedio==float(9) or promedio==float(8):
    print("felicidades aprobaste la materia: ", promedio)
elif promedio==float(7) or promedio==float(6):
    print("promocionas la materia: ", promedio)
elif promedio>10:
    print("error, nota inexistente")
else:
    print("no aprobaste la materia, suerte la proxima: ", promedio)