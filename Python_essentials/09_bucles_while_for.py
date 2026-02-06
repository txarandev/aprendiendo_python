#Bucles while:
counter = 10
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#La sentencia 'break' usada junto a un bucle while con if y else.
largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

#La sentencia 'continue' usada junto a un bucle while con if y else.
number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

#Bucles 'while' y 'else':
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#Bucles for:
#El primer 'for' imprime los valores del 0 al 9.
for i in range(10):
    print("El valor de i es", i)

#El segundo 'for' imprime los valores del 1 al 9.
for a in range(1, 10):
    print("El valor de i es", a)

#El tercer 'for': el tercer argumento indica el paso, 
# que en realidad significa la diferencia entre cada número en la secuencia de números generados por la función.
for i in range(2, 8, 3):
    print("El valor de i es", i)

#este bucle imprime algunas potencias de 2.
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

#Bucles 'for' y 'else':
for i in range(5):
    print(i)
else:
    print("else:", i)


#Sentencia break: sale del bucle inmediatamente.
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

#Sentencia continue: se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; 
# el siguiente turno se inicia y la expresión de condición se prueba de inmediato.
print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
