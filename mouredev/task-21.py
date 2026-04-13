 #
 # EJERCICIO:
 # Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 # una petición a la web que tú quieras, verifica que dicha petición
 # fue exitosa y muestra por consola el contenido de la web.
 #
 # DIFICULTAD EXTRA (opcional):
 # Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 # terminal al que le puedas solicitar información de un Pokémon concreto
 # utilizando su nombre o número.
 # - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 # - Muestra el nombre de su cadena de evoluciones
 # - Muestra los juegos en los que aparece
 # - Controla posibles errores
 #/


import requests
from rich import print
from rich.json import JSON

urlTry = 'https://jsonplaceholder.typicode.com/todos'

response = requests.get(urlTry, timeout=5)

if response.status_code == 200:
  response_json = response.json()
  
  print("\n[bold green]JSON formateado (jsonplaceholder):[/bold green]")
  print(JSON.from_data(response_json))
  
else:
  print(f'[bold red]Error: {response.status_code}[/bold red]')
  

# DIFICULTAD EXTRA:

urlBase = 'https://pokeapi.co/api/v2'

def pokemonNames():
  urlPokemons = f'{urlBase}/pokemon'
  
  response = requests.get(urlPokemons, timeout=5)
  
  if response.status_code == 200:
    response_json = response.json()
    pokemons = response_json["results"]
  
    print("\n[bold cyan]Lista de Pokémons:[/bold cyan]")
    for pokemon in pokemons:
      print(f"- {pokemon['name']}")
    
  else:
    print(f'[bold red]Error: {response.status_code}[/bold red]')


def pokemonInformation(pokemonName):
  urlPokemon = f'{urlBase}/pokemon/{pokemonName}'
  response = requests.get(urlPokemon)
  
  if response.ok:
    data = response.json()
    
    nombre = data["name"]
    pokemon_id = data["id"]
    altura = data["height"]
    peso = data["weight"]
    tipos = [t["type"]["name"] for t in data["types"]]
      
    print("\n[bold yellow]--- INFO DEL POKÉMON ---[/bold yellow]")
    print(f"[bold]Nombre:[/bold] {nombre}")
    print(f"[bold]ID:[/bold] {pokemon_id}")
    print(f"[bold]Altura:[/bold] {altura}")
    print(f"[bold]Peso:[/bold] {peso}")
    print(f"[bold]Tipos:[/bold] {', '.join(tipos)}")
    
    print("\n[bold green]JSON completo formateado:[/bold green]")
    print(JSON.from_data(data))
  
  elif response.status_code == 404:
    print("Ese Pokémon no existe")
    
  else:
    print(f'[bold red]Error: {response.status_code}[/bold red]')
  

def preguntarUsuarioPokemon():
  pokemonNames()
  while True:
    question = input('Sobre que pokemon queres informarte?, salir para salir').strip().lower()
    
    if question == 'salir':
      print('Saliendo del programa....')
      break 
    else:
      pokemonInformation(question)
    
 

preguntarUsuarioPokemon()    


