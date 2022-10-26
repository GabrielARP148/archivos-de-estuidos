#practica de operadores
print("========================")
print("introduce los datos")
print("======================== \n")
dato1=int(input("instroduce un numero: "))
dato2=int(input("introduce el segundo numero: "))
comparación=dato1==dato2
mayor=dato1>dato2
menor=dato1<dato2
igualo=dato1>=dato2
oigual=dato1<=dato2
diferente=dato1!=dato2
print ("los numeros son iguales?", type(comparación))
print("es mayor ", mayor)
print ("es menor ", menor)
print("es mayor o igual ", igualo)
print ("es menor o igual ", oigual)
print ("es diferente a ", diferente)