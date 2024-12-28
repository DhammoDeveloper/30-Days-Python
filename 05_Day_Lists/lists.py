# Lists

# Es una colección de distintos tipos de datos que está ordenada y es modificable (mutable).

lst = list()

lst2 = []

# Por ejemplo:

frutas = ['banana', 'manzana', 'pera', 'naranja']

print('Las frutas disponibles son: ',frutas)

print('La cantidad de frutas que hay son : ', len(frutas))

# Modificar lista

frutas[0]= 'Sandia'
print(frutas)

# Agregar elementos a una lista

frutas.append('banana')
print(frutas)

# Agregar elementos según el índice

frutas.insert(5, 'limones')
print(frutas)

# Eliminar elementos de una lista

frutas.remove('banana')
print(frutas)

frutas.pop(2)
print(frutas)

del frutas[1]
print(frutas)

# Para vaciar las listas, se usa el elemento clear(). Ejemplo: frutas.clear()
# Para copiar listas, se usa .copy(). Ejemplo: frutas.copy()
# Y para unas listas, se puede usar la concatenación con el signo '+'. E incluso usando el método .extended()

# Pueden obtener diferentes tipos de datos

cliente = ['Facundo', 26, {'frutas_compradas:' '23' }]

print(cliente)

# Acceder a los elementos de una lista

nombre_del_cliente = cliente[0]
compra_del_cliente = cliente[2]

print(nombre_del_cliente)
print(compra_del_cliente)

# Desempaquetar elementos de una lista

lista = ['casa', 'perro', 'gato']

primer_elemento, *rest = lista

print(primer_elemento)

# Quitar elementos

list_cortada = frutas[1:2]

print(list_cortada)

# Contar elementos de una lista

edades = [22, 23, 23, 23, 25]
print(edades.count(23))

# Encontrar el índice

print(edades.index(22))

# Invertit listas 

edades.reverse
print(edades)


''' Ejercicios: Día 5 '''



