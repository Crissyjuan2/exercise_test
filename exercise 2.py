#Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
class circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio**2
    def perimetro(self):
        return 2 * 3.1416 * self.radio
circulo1 = circulo(5)
print("El area del circulo es:", circulo1.area())
print("El perimetro del circulo es:", circulo1.perimetro())
#Escribir una clase en python llamada rectángulo que contenga una base y una altura, con un método que calcule el área y otro que calcule el perímetro del rectángulo.
class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * self.base + 2 * self.altura
rectangulo1 = rectangulo(5, 10)
print("El area del rectangulo es:", rectangulo1.area())
print("El perimetro del rectangulo es:", rectangulo1.perimetro())

Escribir una clase en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi"
class cadena:
    def __init__(self, frase):
        self.frase = frase
    def invertir(self):
        return " ".join(self.frase.split()[::-1])
cadena1 = cadena("Mi Diario Python")
print(cadena1.invertir())
#Escribir una clase en python que calcule el factorial de un número
class factorial:
    def __init__(self, numero):
        self.numero = numero
    def calcular(self):
        factorial = 1
        for i in range(1, self.numero + 1):
            factorial *= i
        return factorial
factorial1 = factorial(5)
print(factorial1.calcular())
#Escribir una clase en python que calcule el área de un triángulo
class triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura)/2
triangulo1 = triangulo(5, 10)
print("El area del triangulo es:", triangulo1.area())

#Escribir una clase en python con 2 métodos: get_string y print_string. get_string acepta una cadena ingresada por el usuario y print_string imprime la cadena en mayúsculas.
class cadena:
    def __init__(self):
        self.cadena = ""
    def get_string(self):
        self.cadena = input("Ingrese una cadena: ")
    def print_string(self):
        print(self.cadena.upper())
cadena1 = cadena()
cadena1.get_string()
cadena1.print_string()

#Escribir una clase en python que encuentre un par de elementos (índice de los números) de una matriz dada cuya suma es igual a un número de destino especifico.
#Entrada: numeros = [10,20,10,40,50,60,70], objetivo=50
#Salida: 3, 4
class matriz:
    def __init__(self, numeros, objetivo):
        self.numeros = numeros
        self.objetivo = objetivo
    def encontrar(self):
        for i in range(len(self.numeros)):
            for j in range(i + 1, len(self.numeros)):
                if self.numeros[i] + self.numeros[j] == self.objetivo:
                    return i, j
matriz1 = matriz([10,20,10,40,50,60,70], 50)
print(matriz1.encontrar())

#Escribir una clase en python que convierta un número entero a número romano
class romano:
    def __init__(self, numero):
        self.numero = numero
    def convertir(self):
        if self.numero < 1 or self.numero > 3999:
            return "El numero esta fuera del rango"
        else:
            unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
            decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
            millares = ["", "M", "MM", "MMM"]
            u = unidades[self.numero % 10]
            d = decenas[self.numero % 100 // 10]
            c = centenas[self.numero % 1000 // 100]
            m = millares[self.numero // 1000]
            return m + c + d + u
romano1 = romano(3999)
print(romano1.convertir())

