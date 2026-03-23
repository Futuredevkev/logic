import random

def numberRandom():
 randomNumber = random.randint(1, 100)
 return randomNumber


def pedirIntentoNumero():
  try:
    numberUser = input('numero random del 1 al 100, si le embocas te ganas un pase a la puta que te pario')
    numberUser = int(numberUser)
    return numberUser
  except ValueError:
    print('vuelve a escribir un  numero valido')
    return pedirIntentoNumero() # Recursion funcion que se llama dentro de la misma funcion

def comparar(numeroUsuario, numeroSecreto):
  if numeroUsuario > numeroSecreto:
    return 'Es Menor'
  elif numeroUsuario < numeroSecreto:
    return 'Es Mayor'
  else:
    return 'Has Acertado'



def jugar():
    numeroRandom = numberRandom()
    resultado = ''
    intentos = 0

    while resultado != 'Has Acertado':
      numeroUsuario  = pedirIntentoNumero()
      resultadoComparado = comparar(numeroUsuario, numeroRandom)
      intentos +=1
      if intentos >= 5:
        print('ya muchos intentos')
        break
      print(resultadoComparado)


jugar()

