# definir una tupla
frutas= ('naranja', 'platano', 'guayaba')
print(frutas)

# saber el largo de una tupla
print(len(frutas))

# acceder a un elemento
print(frutas[0])

# navegacion inversa
print(frutas[-1])

# acceder a un rango de valores
print(frutas[0:1]) #el ultimo indice no se incluye

# recorrer elementos de una tupla
for fruta in frutas:
  print(fruta, end=' ')

#cambiar un valor de una tupla * no se puede cambaiar dado que un tupla es inmutable
#frutas[0] = 'pera'

# covertir tupla a lista para poder modificar sus elementos y luego cambiar de lista a tupla

frutasLista = list(frutas)
frutasLista[0] = 'pera'
frutas = tuple(frutasLista)
print('\n',frutas) #no es una buena practica a menos que sea muy necesario su uso

# eliminar la tupla por completo
del frutas 
print(frutas)