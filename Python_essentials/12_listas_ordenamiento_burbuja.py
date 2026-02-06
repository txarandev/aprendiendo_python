#Ordenamiento burbuja:
"""
Ahora que puedes hacer malabarismos con los elementos de las listas, es hora de aprender como ordenarlos. 
Se han inventado muchos algoritmos de clasificación, que difieren mucho en velocidad, así como en complejidad. 
Vamos a mostrar un algoritmo muy simple, fácil de entender, pero desafortunadamente, tampoco es muy eficiente. 
Se usa muy raramente, y ciertamente no para listas extensas.

Digamos que una lista se puede ordenar de dos maneras:

ascendente (o más precisamente - no descendente) - si en cada par de elementos adyacentes, el primer elemento no es mayor que el segundo;
descendente (o más precisamente - no ascendente) - si en cada par de elementos adyacentes, el primer elemento no es menor que el segundo.
"""

#Ordenando una lista:

# my_list = [8, 10, 6, 2, 4]  # lista a ordenar

# for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
#     if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.

# my_list = [8, 10, 6, 2, 4]  # lista a ordenar
# swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

# while swapped:
#     swapped = False  # no hay intercambios hasta ahora
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print(my_list)

#version final interactiva de ordenamiento burbuja.
# my_list = [8, 10, 6, 2, 4]
# swapped = True
# num = int(input("¿Cuántos elementos deseas ordenar?: "))

# for i in range(num):
#     val = float(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list)

#Si quieres que python ordene la lista puedes hacerlo de la siguiente manera.
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#Y tambien puede hacerlos de forma inversa.
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # output: [4, 2, 1, 3, 5]



