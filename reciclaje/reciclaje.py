import os
from openai import OpenAI


residuos = {
    "botella de plástico": "reciclable - contenedor amarillo",
    "pila": "no reciclable - punto limpio",
    "cartón": "reciclable - contenedor azul"
}

def openAI(objeto):
  client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

  response = client.responses.create(
    model="gpt-5.2",
    instructions="Actua como un profesional del reciclaje y contesta en qué contenedor debería "
            "ir cada producto de reciclaje, y dale consejos al usuario sobre cómo hacerlo. "
            "Responde corto y directo.",
    input= objeto,
  )

  return response.output_text


def BusquedaRespuesta(objeto):
  for clave, valor in residuos.items():
      if clave in objeto:
           return f"✅ {valor}"
    # Si no encontró nada, devolvemos None
  return None

def preguntarResponderUsuario():
  while True:
    objeto = input('que quieres reciclar?, si queres salir y no preguntar mas pone exit').lower().strip()
    if objeto == 'exit':
      print('chau')
      break  


    respuesta = BusquedaRespuesta(objeto)

    if respuesta:
      print(respuesta)
    else:
      respuestaIa = openAI(objeto)
      print(respuestaIa)


preguntarResponderUsuario()