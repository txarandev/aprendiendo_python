# Esta sentencia condicional consta de los siguientes elementos, estrictamente necesarios en este orden:

# La palabra clave reservada 'if';
# Uno o más espacios en blanco;
# Una expresión (una pregunta o una respuesta) cuyo valor se interpretar únicamente en términos de True (cuando su valor no sea cero) y False (cuando sea igual a cero);
# Unos dos puntos seguidos de una nuevalínea;
# Una instrucción con sangría o un conjunto de instrucciones (se requiere absolutamente al menos una instrucción); 
# la sangría se puede lograr de dos maneras: insertando un número particular de espacios (la recomendación es usar cuatro espacios de sangría), o usando el tabulador; 

# NOTA: si hay mas de una instrucción en la parte con sangría, 
# la sangría debe ser la misma en todas las líneas; aunque puede parecer lo mismo si se mezclan tabuladores con espacios, 
# es importante que todas las sangrías sean exactamente iguales Python 3 no permite mezclar espacios y tabuladores para la sangría.

#Sentencia 'if'
sheep_counter = 120

if sheep_counter >= 120: # Evaluar una expresión condicional
    print("Estoy durmiendo y soñando!!!!") # Ejecutar si la expresión condicional es verdadera

#Sentenvia 'if-else'
if sheep_counter == 120:
    print("Estoy durmiendo y soñando!!!!") 
else:
    print("sigo contando obejas!!!")

#Sentencia 'elif'
if sheep_counter == 120:
    print("Estoy durmiendo y soñando!!!!")
elif sheep_counter >= 60:
    print("sigo contando obejas!!!")
else:
    print("no puedo dormir!!!!!!!")


#ejemplo de programa....
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

#Otro ejemplo... aAhora con tres numeros:
# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)
