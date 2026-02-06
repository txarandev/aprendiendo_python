#Para crear una lista usamos corchetes '[]':
numeros =[1, 34, 6, 90]
#Imprimiendo la lista:
print("Imprimiendo el contenido de la lista: ", numeros)

#Asignamos un valor a un elemento de la lista:
numeros[0] = 9
print("añadiendo mas numeros a la lista: ", numeros)

#copiamos el valor de un elemento a otro:
numeros[1] = numeros[3]
print("copiamos el indice 1 al 3: ", numeros)

#Tambien podemos acceder a distintos valores de la lista:
print("Este numero es: ", numeros[0])

#La funcion 'len()' se usa para verificar la longitud de la lista:
print(len(numeros))

#tambien podemos eliminar datos de una lista:
del numeros[2]
print(len(numeros))
print(numeros)

#No se puede acceder a un elemento que no existe, ni asirnarle un valor,esto causara un error.
# print(numeros[4])
# numeros[4] = 8


#Podemos usar indices negativos y esto imprimira el ultimo elemento de la lista
print(numeros[-1])

#podemos agregar elementos al final de una lista usando:
numeros.append(34) #añade el numero 34 al final de la lista.
print(numeros)

#podemos tambien agregar en cualquier incide de la lista asi: list.insert(indice, valor)
numeros.insert(5, 7)
print(numeros)
numeros.insert(2, 23)
print(numeros)

#Podemos crear una lista vacia. Y llenarla usando una iteracion con 'for'
num = []
for i in range(5):
    num.append(i + 1)
print(num)

#podemos hacerlo tambien usando el metodo 'insert':
my_list = []  # Creando una lista vacía.
total = 0

for i in range(5):
    my_list.insert(0, i + 1) #si le indicamos un valor 0 la lista iterara del reves.

print(my_list) #Imprime (5,4,3,2,1)

#En este ejemplo sumamos todos los valores de la lista:
for i in range(len(my_list)):
    total += my_list[i]

print(total)

