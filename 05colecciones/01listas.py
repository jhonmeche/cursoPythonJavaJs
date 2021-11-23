# Definir una lista de tipo str
nombres = ['juan','Karla', 'Ricardo', 'Maria',]

# imprimir la lsita de nombres
print(nombres)

# Accder a los elementos de una lista
print(nombres[0])

# Acceder a los elementos de forma inversa
print(nombres[-1])
print(nombres[-2])

# imprimir un rango
print(nombres[0:2]) # no se incluye el indice 2

# ir del inicio de la lista al indice sin incluirlo
print(nombres[ : 3])

# desde el indice indicado hasta el final 
print(nombres[1:])

# cambiar un valor de la lista 
nombres[3] = 'Ivone'
print(nombres)

#iterar una lista
for nombre in nombres:
  print(nombre)
else: 
  print('No existen mas nombres en la lista') 

# preguntar el largo de una lista
print(len(nombres))

# agregar un elemento 
nombres.append('lorenzo')
print(nombres)

#insertar un elemento en un indice en especifico
nombres.insert(1, 'octavio')
print(nombres)

# remover un elemento de una lista por valor
nombres.remove('octavio')
print(nombres)

# remover el ultimo valor agregado
nombres.pop()
print(nombres)

# eliminar un valor con un indice indicado 
del nombres [0]
print(nombres)

# limpiar todos los elementos de una lista
nombres.clear()
print(nombres)

#borrar la lista por completo
del nombres
print(nombres)