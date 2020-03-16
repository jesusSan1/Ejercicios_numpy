#1. Importar numpy
import numpy as np

#2. Crear un arreglo de 10 "0"
arreglo = np.zeros(10) #zeros es para generar numero 0
print("2. Arreglo de 10 ceros")
print (arreglo, "\n")

#3. Crear un arreglo de 10 "1"
arr = np.ones(10) #ones es para generar 1
print("3. Arreglo de 10 unos")
print(arr)
print("\n")

#4. Crear un arreglo de 10 "5"
uno = np.ones(10)*5 #multiplicas 1 * 5
print("4. Arreglo de 10 cincos") 
print(uno)
print("\n")

#5. Crear un arreglos de enteros del 10 al 50
enteros = np.arange(10, 51) #arange es para definir un rango
print("5. Arreglo de numeros enteros del 10 al 50")
print(enteros)
print("\n")

#6. crear un arreglo con los pares comprendidos del 10 al 50
pares = np.arange(10, 51, 2) #al pasarle el num 2 significa que solo tomará numeros pares
print("6. Arreglo de pares comprendidos del 10 al 50")
print(pares)
print("\n")

#7. Crear un matriz de 3x3 del 0 al 8 llenados por filas

matriz = np.arange(0,9).reshape((3,3)) #reshape es el tamaño de la matriz 
print("7. Matriz de 3x3 del 0 al 8")
print(matriz)
print("\n")

#Otra forma de llenar la matriz
print("Otra forma de llenar la matriz")
filas = 3
columnas= 3
ma = []
elem = 0
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(elem)
        elem += 1
    ma.append(fila)
print(ma)
print("\n")

#8. Crear una matriz identidad de 3x3
identidad = np.identity(3) #identity es para crear un matriz identidad y le pasamos como parametro el tamaño de la matriz
print("8. Crear una matriz identidad de 3x3")
print(identidad)
print("\n")


#9. Generar un numero aleatorio entre el 0 y 1
aleatorio = np.random.random() #la propiedad random tiene otra funcion random() que genera numeros aleatorios entre 0 y 1
print("9. Numero aleatorio entre 0 y 1")
print(round(aleatorio,2))
print("\n")

#10. Generar un arreglo de 25 de numeros aleatorios
import random
A = []
for i in range (25):
    A.append(random.randint(1, 25))
print("10. Arreglo de 25 numeros aleatorios")
print (A)
print("\n")

#11. Generar una matriz del 0.1 al 1
lleno = np.arange(.01,1.01,.01).reshape((10,10))#linspace es parecido a reshape
#el primer parametro es de donde empieza
#El segundo parametro es hasta donde termina
#El ultimo parametro es cuantos numeros va a generar
print("11. Generar matriz del 0.1 al 1")
print(lleno)
print("\n")

#12. Generar una matriz del 1 al 25
matriz = np.arange(1,26).reshape((5,5)) #reshape es el tamaño de la matriz 
print("12. Generar una matriz 1 al 25")
print(matriz)
print("\n")

#13. de la matriz anterior obtener los numeros:
#12, 13, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25
a = np.arange(1,26).reshape((5,5))

print("13. De la matriz anterior obtener los numeros")
print("12, 13, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25")
print(a[2:,1:])     
print("\n")

print("14. de la matriz anterior extraer el numero 20")
numero20 = np.arange(1,26).reshape((5,5))
print("[",numero20[3,4],"]") #Aqui se indica la fila y la columna donde se encuentra el numero
print("\n")

print("15. de la matriz anterior extraer los numeros 2, 7, 12. #pendiente")
numerosExtraidos = np.arange(1,26).reshape((5,5))
print(numerosExtraidos[0:,1])
print("\n")

print("16. de la matriz anterior extraer la ultima fila")
ultima = np.arange(1,26).reshape((5,5))
print(ultima[4:,0:])
print("\n")

print("17. De la matriz anterior extraer las ultimas 2 filas")
ultimas2Filas = np.arange(1,26).reshape((5,5))
print(ultimas2Filas[3:5])
print("\n")

print("18. Sumar todos los elementos de la matriz")
suma = np.arange(1,26).reshape((5,5))
suma2 =sum(suma)
segundo = np.sum(suma2, axis=0)
print(segundo)
print("\n")

print("19. Obtener la desviacion estandar.")
suma = np.arange(1,26).reshape((5,5))
desviacion = np.std(suma)
print(desviacion)
print("\n")

print("20. Obtener la suma de cada una de las columnas y generar un arreglo correspondiente")
suma = np.arange(1,26).reshape((5,5))
suma2 =sum(suma)
print(suma2)
print("\n")