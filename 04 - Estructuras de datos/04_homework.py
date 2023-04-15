# #1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
# ls=['México', 'Argentina', 'Colombia', 'perú', 'Chile']
# print(ls)

# # 2) Imprimir por pantalla el segundo elemento de la lista
# #3) Imprimir por pantalla del segundo al cuarto elemento
# # 4) Visualizar el tipo de dato de la lista

# print(ls[1])
# print(ls[1:4])
# print(type(ls))

# #5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
# print(ls[3:])

# #6) Visualizar los primeros 4 elementos de la lista
# print(ls[:4])

# # # 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
# # ls.append('peru', 'eeu')
# # print(ls)

# #8) Agregar otra ciudad, pero en la cuarta posición
# ls.insert(3,'ITALIA')
# print(ls)

# #9) Concatenar otra lista a la ya creada

# frutas = ["manzana", "naranja", "plátano", "fresa", "piña"]
# colores = ["rojo", "azul", "verde", "amarillo", "naranja"]

# frutas.extend(colores)
# print(frutas)
# # #10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
# # ls.index('peru')

# #11) ¿Qué pasa si se busca un elemento que no existe?
# print(frutas.index('verde'))

# #12) Eliminar un elemento de la lista
# frutas.remove('fresa')
# print(frutas)

# #14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
# a=frutas.pop()
# print(a)

# #15) Mostrar la lista multiplicada por 4
# perro = ["perro"]*4
# print(perro)


##tuplas
#16) Crear una tupla que contenga los números enteros del 1 al 20
tupla=tuple(range(1,21))
print(tupla)

#17) Imprimir desde el índice 10 al 15 de la tupla

print(tupla[10:15])

#18) Evaluar si los números 20 y 30 están dentro de la tupla
print(tupla.index(1),'***')

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
ls=['México', 'Argentina', 'Colombia', 'perú', 'Chile', 'México']
x='Paris'
if x in ls:
    print('si toy, poss: ', ls.index(x))
else:
    ls.append(x)
    print('Yo ya estoy',ls,'poss: ', ls.index(x))


#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista 

print(ls.count('México'))
print(tupla.count(5))
# 21) Convertir la tupla en una lista
lista_tupla=list(tupla)
print(lista_tupla)

#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
tupla=tuple(range(1,21))
x1,x2,x2=tupla[:3]
print(x1)

diccionario={
    'frutas': ["manzana", "naranja", "plátano", "fresa", "piña"],
    'paises':['México', 'Argentina', 'Colombia', 'perú', 'Chile', 'México']
}
print(diccionario['paises'])