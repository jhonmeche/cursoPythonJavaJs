from types import prepare_class


planetas = {'marte', 'jupiter', 'venus'}
print(planetas)

#conocer el largo de los elementtos
print(len(planetas))

# revisar si un objeto esta presente en un set
print('marte' in planetas)

#agregar un elemento 
planetas.add('tierra')
print(planetas)

# no se pueden duplicar elementos
planetas.add('tierra')
print(planetas)

# eliminar un elemento posiblemente arrojando un error
planetas.remove('tierra')
print(planetas)

# eliminar un elemento sin arrojar error
planetas.discard('jupiter')
print(planetas)

# limpiar set
planetas.clear()
print(planetas)

# eliminar completamente un set
del planetas
print(planetas)

