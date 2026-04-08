import re
 
 #
 # EJERCICIO:
 # Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 # creando una que sea capaz de encontrar y extraer todos los números
 # de un texto.
 #
 # DIFICULTAD EXTRA (opcional):
 # Crea 3 expresiones regulares (a tu criterio) capaces de:
 # - Validar un email.
 # - Validar un número de teléfono.
 # - Validar una url.
 #/
 
 
texto = """
Hola! Podés visitar nuestras webs:
https://www.ejemplo.com
http://test-site.org/path?query=123
www.otrodominio.net
sub.dominio.com/path/to/resource

También tenemos enlaces más raros:
https://mi-web.com.uy/productos?id=45&ref=abc
http://localhost:3000/test

Contactanos a estos números:
+59891234567
59892345678
91234567
+598 91 234 567
(091) 234-567
091 234 567
+54 9 11 2345-6789

Otros textos mezclados:
"Mi número es 099123456 pero no siempre está disponible"
"Llamar al +1-202-555-0147 urgente"
"Visitar https://sub.domain.co.uk/path?arg=value#anchor ahora"

Texto random para ruido:
abc123, test@test.com, dirección falsa 1234, etc.
"""

print(texto)

pattern_digts = r"\d+"
patternEmail = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
patternUrl = r"^(https?:\/\/)?([\w\-]+\.)+[\w\-]+(\/[\w\-._~:/?#[\]@!$&'()*+,;=]*)?$"
patternTel = r"^\+?\d{1,3}?[\s.-]?\(?\d{2,3}\)?[\s.-]?\d{3,4}[\s.-]?\d{4}$"

def findNumers(text: str):
  return re.findall(pattern_digts, text)
  

def findEmail(email: str):
  return bool(re.match(patternEmail, email))

def findPhone(phone: str):
  return bool(re.match(patternTel, phone))

def findUrl(url:str):
  return bool(re.match(patternUrl, url))


print(findNumers(texto)) 
print(findEmail("hackapa55@outlook.com"))
