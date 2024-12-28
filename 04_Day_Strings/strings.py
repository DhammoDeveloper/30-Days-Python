# Strings

cadena = '¡Soy una cadena de texto!'

print(cadena)
print(len(cadena)) #Len es para saber la longitud de nuestro String

# Cadenas multilinea

cadena_multilinea = '''
¡Hola! Soy una cadena multilinea.
Suelo usar triple comillas tanto simples como dobles.
¡Saludos!
'''
print(cadena_multilinea)


#Concatenación de cadenas

saludo = '¡Hola! Mí nombre es'
nombre = 'Facundo'
apellido = 'Caballero'
cadena_completa = saludo + ' ' + nombre + ' ' + apellido

print(cadena_completa)

# str.format 

calle = 'Jujuy'
numero = 348

direccion = 'Mí dirección es {} {}'.format(calle, numero)
print(direccion)

# Primero declaramos las variables y luego lo imprimimos en una nueva varible usando {} y el .format al final.
# Después colocamos las variables según el orden en que queramos que se impriman entre () y separados por ,.

numero2 = 33
numero1 = 22

print('{} + {} = {}'.format(numero1, numero2, numero1 + numero2))

# Interpolación de cadenas f-strings

print(f'{numero1} * {numero2} = {numero1 * numero2}')

#Métodos de cadenas

# .capitalize()

# Convierte el primer carácter en mayúscula

ejemplo = 'casa'
print(ejemplo.capitalize())

