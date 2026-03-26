def FizzBuzz():
  numberoneofonehundred = [i for i in range(0,101)]

  for i in numberoneofonehundred: # O podemos usar mas directo for i in range(0, 101)
    if i % 3 == 0 and i % 5 == 0: # O directamente podemos hacer if i % 15 == 0 >D
      print('fizzbuzz')
    elif i % 5 == 0:
      print("buzz")
    elif i % 3 == 0:
      print('fizz')
    else:
      print(i)
    

FizzBuzz()

def esAnagrama(p1, p2):
  if not isinstance(p1, str) or not isinstance(p2, str):
    print("Error: Ambos parámetros deben ser strings")
    return False
     
  if p1.lower() == p2.lower():
    print('che son dos palabras iguales, imposibles que sean analgramas')
    return False 
  # sorted devuelve una nueva lista con las letras ordenadas, 
  # mientras que sort (de listas) modifica la lista en el lugar y no funciona directamente con strings   
  elif sorted(p1.lower()) == sorted(p2.lower()): #Sorted devuelve 
    print(f'si es un anagrama la palabra 1: {p1}, y la palabra 2: {p2}')
    return True
  else:
    print('esto no es un analgrama') 
    return False

esAnagrama('roma', 'amor')


# Fibonacci
def fibonacci():
  prev = 0
  next = 1
  
  for _ in range(0, 50):
    fib = prev + next # 0 1, seria prev + next por donde empieza el fibonacci 0, 1
    prev = next # ahora tenemos que almacenar el numero next en el prev, porque next pasa a ser prev, PREV PASA A SER 1
    next = fib # y el fib pasa a ser igual a la suma de prev y next NEXT PASA A SER EL FIB 1 EN ESTE CASO 
     
     
fibonacci()


# Fibonacci recurisva
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Imprimir los primeros 10 números de Fibonacci
for i in range(10):
    print(fibonacci(i))
    
    
# Es mi prima?
def isPrimeNumber():
  for number in range(1,101):
    if number <= 2:
      is_divisible = False 
      
      for index in range(2, number):
        if number % index == 0:
          is_divisible = True 
          break 
        
      if not is_divisible:
        print(f'el numero {number} es primo')    

isPrimeNumber()


def isPrimeNumberUser(number):
  if number < 2:
    return False 

  for index in range(2, number):
    if number % index == 0:
      return False
    
  print(f'{number} es primo')
  return True

isPrimeNumberUser(4)



def reverse(text):
  text_len = len(text)
  reversedText = ""
  
  for i in range(0, text_len):
    reversedText += text[text_len - i - 1]
  
  return reversedText
  
reverse("Hola Mundo")


def calcular_area():
    # Preguntamos el tipo de polígono
    while True:
        poligono = input("Qué polígono querés calcular? Elegí cuadrado, triángulo o rectángulo: ").lower()
        if poligono in ['cuadrado', 'triangulo', 'rectangulo']:
            break
        print("Elegí una opción correcta 😎")

    # Pedimos solo los valores necesarios según el polígono
    if poligono == 'cuadrado':
        lado = float(input("Cuánto mide el lado? "))
        area = lado ** 2

    elif poligono == 'rectangulo':
        base = float(input("Cuánto mide la base? "))
        altura = float(input("Cuánto mide la altura? "))
        area = base * altura

    elif poligono == 'triangulo':
        base = float(input("Cuánto mide la base? "))
        altura = float(input("Cuánto mide la altura? "))
        area = (base * altura) / 2

    return area, poligono  # devolvemos área y tipo de polígono

# Uso
area, pol = calcular_area()
print(f"El área del {pol} es: {area}")

