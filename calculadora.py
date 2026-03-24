import math

class Calculadora:

    def __init__(self):
        self.historial = []

    def sumar(self, *args):
        resultado = sum(args)
        self.historial.append(f"Suma {args} = {resultado}")
        return resultado

    def restar(self, *args):
        resultado = args[0]
        for n in args[1:]:
            resultado -= n
            self.historial.append(f"Resta {args} = {resultado}")
        return resultado

    def multiplicar(self, *args):
        resultado = 1
        for n in args:
            resultado *= n
            self.historial.append(f"Multiplicacion {args} = {resultado}")
        return resultado

    def dividir(self, *args):
        resultado = args[0]
        for n in args[1:]:
            if n == 0:
                raise ValueError("No se puede dividir por cero")
            resultado /= n
            self.historial.append(f"division {args} = {resultado}")
        return resultado

    def potencia(self, base, exponente):
        resultado = base ** exponente
        self.historial.append(f"division {base} ** {exponente} = {resultado}")
        return resultado 

    def modulo(self, x, y):
        if y == 0:
            raise ZeroDivisionError("No se puede calcular módulo con divisor 0")
        resultado = x % y 
        self.historial.append(f"modulo de {x} % {y} = {resultado}")
        return resultado

    def raiz(self, x):
        if x < 0:
            raise ValueError("No se puede calcular la raíz de un número negativo")
        resultado = math.sqrt(x)
        self.historial.append(f"raiz {x} = {resultado}")
        return resultado

    def factorial(self, x):
        if not isinstance(x, int) or x < 0:
            raise ValueError("Factorial solo de enteros ≥ 0")
        resultado = math.factorial(x)
        self.historial.append(f"factorial {x} = {resultado}")
        return resultado
      
    def historial(self):
      if not self.historial:
        return 'No hay operaciones todavia'
      return "\n".join(self.historial)
      
      
def main():
  calc = Calculadora()
  
  while True:
    print("\n--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Raíz cuadrada")
    print("8. Factorial")
    print("9. Ver historial")
    print("0. Salir")
    
    opcion = input('Elige una opcion numerica')
    
    try:
      if(opcion == 1):
        nums = input('Ingresa un numeros separados por coma: ')
        nums_split = nums.split(",")
        nums = []
        for n in nums_split:
          nums.append(float(n))
        print('Resultado:', calc.sumar(*nums))
      elif(opcion == 2):
        nums = input('Ingresa un numeros separados por coma: ')
        nums_split = nums.split(",")
        nums = []
        for n in nums_split:
          nums.append(float(n))
        print('Resultado:', calc.restar(*nums))
      elif(opcion == 3):
        nums = input('Ingresa un numeros separados por coma: ')
        nums_split = nums.split(",")
        nums = []
        for n in nums_split:
          nums.append(float(n))
        print('Resultado:', calc.multiplicar(*nums))
      elif(opcion == 4):
        nums = input('Ingresa un numeros separados por coma: ')
        nums_split = nums.split(",")
        nums = []
        for n in nums_split:
          nums.append(float(n))
        print('Resultado:', calc.dividir(*nums))
      elif(opcion == 5):
        base = float(input('Base :'))
        exponente = float(input('Exponente :'))
        print('Resultado :', calc.potencia(base, exponente))
      elif(opcion == 6):
        x = float(input('Numero :'))
        y = float(input('Divisor :'))
        print('Resultado :', calc.modulo(x, y))
      elif(opcion == 7):
        x = float(input('Numero Entero >=0 :'))
        print('Resultado :', calc.raiz(x))
      elif(opcion == 8):
        x = float(input('Numero Entero >=0 :'))
        print('Resultado :', calc.factorial(x))
      elif(opcion == 9):
        print(calc.historial())
    except Exception as e:
      print('Error', e)  


if __name__ == "__main__":
    main()