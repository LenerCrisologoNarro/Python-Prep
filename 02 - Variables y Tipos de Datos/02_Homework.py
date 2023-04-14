# ##1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
# variable=5

# if variable<0:
#     print('Menor que cero')
# else :
#     print('mayor que cero')

# ## 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato


# var1= 123
# var2=123
# if type(var1)==type(var2):
#     print('Variables son del tipo: ', type(var1))
# else:
#     print('Var1:', type(var1),'\n','Var2:', type(var2) )

# # #3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
# par=[]
# imp=[]
# for n in range(1,21):
#     if n%2==0:
#         par+=[n]
#     else:
#         imp+=[n] 
# print('Pares', par) 
# print('imp',imp)
# x=0
# cad=[]
# var= 'LENERCRISOLOGONARRO'
# for letra in var:
#     cad+=[letra]
#     x+=1
# print(cad, x)

# #4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
# for n in range(1,6):
#     print(n, '^ 3= ', (n**3))

# #5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# var=10
# for n in range(1, var):
#     print(n)


#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# factorial=8
# i=0
# c=1
# if factorial >0:
#     while i<factorial:
#         i+=1
#         c*=i
#     print(c)
# else:
#     print('Numero debe ser positivo')


# #7Crear un ciclo for dentro de un ciclo while
# i=0
# while i<3:
#     i+=1
#     for n in range(1, i+1):
#        True
#     print(n)

#8) Crear un ciclo while dentro de un ciclo for
# i=0
# for n in range (1, 6):
#     while i<n:
#         i+=1
#         print(i)

# #9) Imprimir los números primos existentes entre 0 y 30

# for nro in range(0,30):
#     primo=True
#     for n in range(2, nro):
#         if(nro%n==0):
#             primo=False
#             break
#     if primo==False:
#          print(nro,'No primo')
#     else: 
#         print(nro,'primo')


#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# #13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# for n in range(100, 301):
#     if n%12==0:
#         print(n, 'es divisible por 12 =',n/12)

# #14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
# nro= input('Ingrese Numero: ')
# pri=True
# while nro!= "salir":
#     nro=int(nro)
#     for n in range(2, nro):
#         if (nro%n==0):
#             pri=False
#             break
#     if pri==False:
#         print('NO primo')
#     else:
#         print('primo')
#     nro= input('Ingrese Numero: ')
#     print("Ha salido del programa.")


#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
n=100
limit=150
while n<limit:
    n+=1
    if(n%6==0):
        if n%3==0:
            print(n,'\n/3',n/3,'\n6*',n/6)
            break

limit = 150
encontrado = False
for n in range(100, limit):
    if n % 6 == 0 and n % 3 == 0:
        print(n, '\n/3', n/3, '\n6*', n/6)
        encontrado = True
        break
        
if not encontrado:
    print("No se encontró ningún número que cumpla los criterios en el rango dado.")