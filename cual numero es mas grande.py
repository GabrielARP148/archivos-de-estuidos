#dectecto de numeros 
print("que numero es el mas grande? \n")
print("por favor introduce los datos")
numero1=int(input("numero 1: "))
numero2=int(input("numero 2: "))
numero3=int(input("numero 3: "))
if numero1>numero2 and numero1>numero3:
    print("el numero ", numero1, " es mayor")
elif numero2>numero1 and numero2>numero3:
    print("el numero ", numero2, " es mayor")
elif numero3>numero1 and numero3>numero2:
    print("el numero ", numero3, " es mayor")
    