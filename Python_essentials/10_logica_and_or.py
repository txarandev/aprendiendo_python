#Un operador de conjunción lógica en Python es la palabra 'and'.
counter = 0
value = 100

print(counter > 0 and value == 100) #Imprime False.
print(counter <= 0 and value ==100) #Imprime True.

#Operador 'or'. Es un operador binario con una prioridad más baja que 'and'.
print(counter > 0 or value == 100) #Imprime True.

#el Operador 'not' Es un operador unario que realiza una negación lógica. y su prioridad es muy alta.
#Su funcionamiento es simple: convierte la verdad en falso y lo falso en verdad.
print(not counter > 0) #Imprime True.
print(not value == 100) #Imprime False.

#expresiones logicas.
var = 1
var1 = 0

# Ejemplo 1:
print(var > 0) #Imprime True.
print(not (var1 <= 0)) #Imprime False.


# Ejemplo 2:
print(var != 0) #Imprime True.
print(not (var1 == 0)) #Imprime False.






