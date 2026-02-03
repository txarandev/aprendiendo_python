#Python ofrece dos funciones para convertir datos y que no generen errores.
#Son 'int()' intenta convertir el a entero, 'float()' a datos flotantes, 'str()' intenta convertirlo a una cadena.

anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

#Mas ejemplos:
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

#Debido a que la funcion 'print' acepta una expresion como argumento podemos eliminar la varible hypo,
#Y pasar la expresion directamente en la funcion 'print'
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)

#con la funcion 'str()'
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))

#Tambien podemos usar concatenadores como el ejemplo siguiente:
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

#tambien podemos replicar cadenas y/o numeros, este programa dibuja un rectangulo:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

