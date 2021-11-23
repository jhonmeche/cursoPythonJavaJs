# Ejecrcicio valor dentro de rango\

#valor = int(input('Escribe el valor: '))
#valorMinimo = 0
#valorMaximo = 5

#dentroRango = valor >= valorMinimo and valor <= valorMaximo

#if dentroRango :
#  print(f'El valor {valor} esta dentro de rango')
#else:
#  print(f'el valor {valor} esta fuera de rango')

# Ejercicio operador or

#vacaciones = False
#diaDescanso =  False

#asistencia = vacaciones or diaDescanso

#if asistencia:
#  print(f'Puede asistir al juego')
#else:
#  print(f'No puede asistir al juego')

edad = int(input('Por favor ingresa tu edad'))

veintes = edad >= 20 and edad <30
print(veintes)
treintas = edad >=30 and edad <40
print(treintas)
if veintes or treintas:
  print('dentro de rango (20\'s) o (30\'s)')
  if veintes:
    print('dentro de rango (20\'s)')
  elif treintas:
    print('dentro de rango (30\'s)')
else: 
  print("no esta dentro de los (20\'s) o (30\'s)")