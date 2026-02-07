#para definir una funcion usamos la palabra reservada 'DEF' seguido del nombre de la funcion,
#seguido de parentesis y dos puntos.
def hola_mundo():
    print("Holaa python!!!!!!")

#para poder usar la funcion debemos invocarla si no no sucedera nada.
print("Inicia aqui...")
hola_mundo()
print("termina aqui....")

#Como funcionan las funciones...
"""
Intenta mostrarte el proceso completo:

cuando se invoca una función, Python recuerda el lugar donde esto ocurre y salta hacia dentro de la función invocada;
el cuerpo de la función es entonces ejecutado;
al llegar al final de la función, Python regresa al lugar inmediato después de donde ocurrió la invocación.
"""

#Existen dos consideraciones a tener en cuenta con las funciones:
"""
La primera de ella es:

No se debe invocar una función antes de que se haya definido.

La segunda consideración es más sencilla:

Una función y una variable no pueden compartir el mismo nombre.
"""

#se puede llamar a la funcion tantas veces se necesite:
def message():
    print("Ingresar valor: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

print("aqui acaba la funcion....")

#otra funcion:
def hi():
    print(str("hi!!!\n" * 5))

hi()

