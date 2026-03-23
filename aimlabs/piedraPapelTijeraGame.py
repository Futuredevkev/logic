import random

def randomChoice():
  resultPC = random.choice(['piedra', 'papel', 'tijera'])
  return resultPC


def pedirIntentoChoice():
 
    userChoice = input('Elige piedra, papel o tijera')
    while userChoice not in ["piedra", "papel", "tijera"]:
      print('eleccion invalida, intenta de nuevo')
      userChoice = input("Elige piedra, papel o tijera: ")
    return userChoice


def comprarChoice(pcChoice, userChoice):
  if pcChoice == userChoice:
    return 'empate'
  elif pcChoice == 'papel' and userChoice =='piedra':
    return 'gana la pc'
  elif pcChoice == 'tijera' and userChoice =='papel':
    return 'gana la  pc'
  elif pcChoice == 'piedra' and userChoice =='tijera':
    return 'gana la pc'
  else:
    return 'gana el jugador!!'


def jugar():
  limite = 5
  jugadas = 0
  historial = []

  print("¡Bienvenido a Piedra, Papel o Tijera!")

  while jugadas < limite:
    pcChoice = randomChoice()
    userElection = pedirIntentoChoice()
    comparacion = comprarChoice(pcChoice, userElection)
    jugadas += 1

    historial.append({
      'jugador': userElection,
      'pc': pcChoice,
      'resultado' : comparacion
    })
  
    print(f"Ronda {jugadas}: Jugador: {userElection} | PC: {pcChoice} → {comparacion}")

  print("Historial completo del juego:")
  for ronda in historial:
      print(f"Ronda {ronda['ronda']}: Jugador: {ronda['jugador']} | PC: {ronda['pc']} → {ronda['resultado']}")

jugar()




