from gc import garbage
from unicodedata import numeric


namber=1
two=2
result=namber+two
print (namber + two)
print ("tu resultado es: " + str (result))

print ("busqueda de subcadena↓")

Mesanje = "hola Gabriel"
buscar_subcadena = Mesanje.find ("Gabriel")

print(buscar_subcadena)

print ("extracción ↓")

mensaje= ("Hola Gabriel")

extraer_subcadena=mensaje[1:8]

print(extraer_subcadena)

print ("ejemplo de extracción ↓")

prueba_uno = "extracción de uno"
prueba_dos = "extracción de uno"
print (prueba_uno == prueba_dos)

print ("sesta parte ↓")

print ("operadores aritmeticos ↓")

Numero_uno=1434
exponente=2
numero_dos=5123

resultado_suma=Numero_uno+numero_dos
resultado_resta=Numero_uno-numero_dos
resultado_división=numero_dos/Numero_uno
resultado_potencia=numero_dos**exponente
resultado_mulplicación=numero_dos*exponente
División_entera=numero_dos//Numero_uno


print ("suma ↓")

print ("el resultado de la suma es: " + str (resultado_suma))

print ("restando ↓")

print ("el resultado de la resta ↓" + str (resultado_resta))

print ("diviendo ↓")

print("el resultadod e la división es: " + str (resultado_división))

print ("potencia")

print ("el resultado de la potencia es: " + str (resultado_potencia))

print ("multiplicación ↓")

print ("El resutlado de la multiplicación es: " + str (resultado_mulplicación))

print ("división entera")

print ("el resultado de la división entera es: " + str (División_entera))

"clase numero 7"

#esto es parte del comentario

#comentario multilinea↓

#fin parte 7

# comienzo clase 8

# tipo de datos enteros o largos

tipe=15
print (tipe, type(tipe))

#datos flotantes ↓

numero_flotante=1223.443
print(numero_flotante, type (numero_flotante))

numero_complejos= 2 - 3j
print (numero_complejos, type(numero_complejos))

#tipo de datos print 
nombre = "base de datos."
print (nombre, type(nombre))

#tipo de datos booleano

verdadero_falso= 3 == 4
verdad_Falso= 3==3 
print(verdadero_falso, type(verdadero_falso))

print(verdad_Falso, type(verdad_Falso))

#Clase 9

#introducción de datos

palabra=input("introduce una palabra: ")
num_int= int(input("introduce un numero entero: "))
num_float= float(input("introduce un numero flotante: "))
num_complex= complex(input("introduce un numero complejo: "))
print ("string: ", palabra)
print ("entero: ", num_int)
print ("numero flotante: ", num_float)
print ("numero complejo: ", num_complex)

#entrada de datos 2 (parte 2 de clase 9)

nombre_=input("¿cual es tu nombre? ")
print ("Hola " + nombre_ + ", bienvenido, vamos a realizar una suma")
num_un=int(input("instriduce un nuemro entero: "))
num_2=int(input("introduce otro numero entero: " ))
resultado=(num_un+num_2)
print ("el resultado de la suma es: ", resultado)

#inicio clase 10
#sentencia condicionales simples

introducir_nombre=input("cual es tu nombre?: ")
print ("Hola, ", introducir_nombre, "veamos como te fue en tus calificaciones.")
examen1=float(input("examen 1: "))
examen2=float(input("examen 2: "))
examen3=float(input("examen 3: "))
promedio=(examen1+examen2+examen3)/3
if promedio==float(10) or promedio==float(9) or promedio==float(8):
    print("felicidades aprobaste la materia: ", promedio)
elif promedio==float(7) or promedio==float(6):
    print("promocionas la materia: ", promedio)
elif promedio>10:
    print("error, nota inexistente")
else:
    print("no aprobaste la materia, suerte la proxima: ", promedio)


#setencia condicionales anidadas, clase nº13
#conversor
print("presione 1 si desea convertir un numero en letras")
print("presione 2 si desea converitr letras en numeros")
