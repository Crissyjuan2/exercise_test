#ejercicios de clases, combinando listas y diccionarios

#ejercicio 1
diccionario = {}
for i in range(2):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    diccionario.update({nombre:nota})
print(diccionario)

#ejercicio 2
#ejercicio de listas
lista = []
for i in range(2):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    lista.append(nombre)
    lista.append(nota)
print(lista)

#ejercicio de una clase combinando listas y diccionarios
#ejercicio 3
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return f"Nombre: {self.nombre}, Nota: {self.nota}"
    def __repr__(self):
        return str(self)
lista = []
for i in range(2):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    estudiante = Estudiante(nombre, nota)
    lista.append(estudiante)
print(lista)

#ejercicio de clase, que sume reste multiplique u divide 2 numeros
#ejercicio 4
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    def sumar(self):
        return self.numero1 + self.numero2
    def restar(self):
        return self.numero1 - self.numero2
    def multiplicar(self):
        return self.numero1 * self.numero2
    def dividir(self):
        return self.numero1 / self.numero2
    def __str__(self):
        return f"Numero 1: {self.numero1}, Numero 2: {self.numero2}"
    def __repr__(self):
        return str(self)
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
calculadora = Calculadora(numero1, numero2)
print(calculadora)
print("La suma de los numeros es: ", calculadora.sumar())
print("La resta de los numeros es: ", calculadora.restar())
print("La multiplicacion de los numeros es: ", calculadora.multiplicar())
print("La division de los numeros es: ", calculadora.dividir())

#ejercicios de clases combinando for y diccionarios
#ejercicio 5
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return f"Nombre: {self.nombre}, Nota: {self.nota}"
    def __repr__(self):
        return str(self)
diccionario = {}
for i in range(2):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    estudiante = Estudiante(nombre, nota)
    diccionario.update({nombre:nota})
print(diccionario)

#ejercicio combinado clases y whiles de numeros primos , pares e impares
#ejercicio 6
class Numeros:
    def __init__(self, numero):
        self.numero = numero
    def es_primo(self):
        contador = 0
        for i in range(1, self.numero + 1):
            if self.numero % i == 0:
                contador += 1
        if contador == 2:
            return True
        else:
            return False
    def es_par(self):
        if self.numero % 2 == 0:
            return True
        else:
            return False
    def es_impar(self):
        if self.numero % 2 != 0:
            return True
        else:
            return False
    def __str__(self):
        return f"Numero: {self.numero}"
    def __repr__(self):
        return str(self)
numero = int(input("Ingrese un numero: "))
numeros = Numeros(numero)
print(numeros)
print("El numero es primo: ", numeros.es_primo())
print("El numero es par: ", numeros.es_par())
print("El numero es impar: ", numeros.es_impar())


#ejercicios de funciones, de numeros divisibles para 2 4 y 5
#ejercicio 7
def numeros_divisibles():
    lista = []
    for i in range(1, 101):
        if i % 2 == 0 or i % 4 == 0 or i % 5 == 0:
            lista.append(i)
    return lista
print(numeros_divisibles())

#ejercicios de funciones con la serie de fibonacci
#ejercicio 8
def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)
numero = int(input("Ingrese un numero: "))
print(fibonacci(numero))

#ejercicios de clase contando vocales de una frase
#ejercicio 9
class Frase:
    def __init__(self, frase):
        self.frase = frase
    def contar_vocales(self):
        contador = 0
        vocales = "aeiou"
        for i in self.frase:
            if i in vocales:
                contador += 1
        return contador
    def __str__(self):
        return f"Frase: {self.frase}"
    def __repr__(self):
        return str(self)
frase = input("Ingrese una frase: ")
frase = Frase(frase)
print(frase)
print("El numero de vocales en la frase es: ", frase.contar_vocales())

#funcion que cuenta las vocales de una frase
#ejercicio 10
def contar_vocales(frase):
    contador = 0
    vocales = "aeiou"
    for i in frase:
        if i in vocales:
            contador += 1
    return contador
frase = input("Ingrese una frase: ")
print("El numero de vocales en la frase es: ", contar_vocales(frase))

#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1.
# Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
#ejercicio 11
def suma_digitos(numero):
    suma = 0
    while numero != 0:
        suma += numero % 10
        numero = numero // 10
    return suma
contador = 0
while True:
    numero = int(input("Ingrese un numero: "))
    if numero == -1:
        break
    print("La suma de los digitos del numero es: ", suma_digitos(numero))
    if numero % 2 == 0:
        contador += 1
print("La cantidad de numeros pares ingresados es: ", contador)

#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
#ejercicio 12
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
for i in range(len(frase)):
    if frase[i] == letra:
        print("La letra se encuentra en la posicion: ", i)
        break
    else:
        print("No hay coincidencia en la posicion: ", i)

#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
#Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
#ejercicio 13
total = 0
while True:
    monto = float(input("Ingrese el monto de la compra: "))
    if monto == 0:
        break
    elif monto < 0:
        print("El monto ingresado es negativo, intente nuevamente")
    else:
        total += monto
if total > 1000:
    total = total - (total * 0.10)
print("El total a pagar es: ", total)

#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
#ejercicio 14
contador_pares = 0
contador_impares = 0
while True:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break
    else:
        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
print("La cantidad de numeros pares ingresados es: ", contador_pares)
print("La cantidad de numeros impares ingresados es: ", contador_impares)

Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra ("/") se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.
#ejercicio 15
contador_lineas = 0
while True:
    contador_digitos = 0
    libro = input("Ingrese el titulo del libro: ")
    if libro == "*":
        break
    else:
        for i in libro:
            if i.isdigit():
                contador_digitos += 1
        if "/" in libro:
            contador_lineas += 1
            print("Linea completa. Aparecen ", contador_digitos, " digitos numericos")
print("Fin. Se leyeron ", contador_lineas, " lineas completas")

#Escribir una clase en python que encuentre los 3 elementos que sumen 0 a partir de números reales
#Entrada: [-25, -10, -7, -3, 2, 4, 8, 10]
#Salida: [[-10, 2, 8], [-7, -3, 10]]
#ejercicio 16
class Suma:
    def __init__(self, lista):
        self.lista = lista
    def suma_cero(self):
        lista_final = []
        for i in range(len(self.lista)):
            for j in range(i + 1, len(self.lista)):
                for k in range(j + 1, len(self.lista)):
                    if self.lista[i] + self.lista[j] + self.lista[k] == 0:
                        lista_final.append([self.lista[i], self.lista[j], self.lista[k]])
        return lista_final
    def __str__(self):
        return f"Lista: {self.lista}"
    def __repr__(self):
        return str(self)
lista = [-25, -10, -7, -3, 2, 4, 8, 10]
suma = Suma(lista)
print(suma)
print("Los 3 elementos que suman 0 son: ", suma.suma_cero())

