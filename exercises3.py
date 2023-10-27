# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
# Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia,
# indicar en qué posición se encontró y finalizar la ejecución., utiliZar la funcion While

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
posicion = 0
while posicion < len(frase):
    if frase[posicion] == letra:
        print(f"La letra {letra} se encuentra en la posicion {posicion}")
        break
    else:
        print(f"La letra {letra} no se encuentra en la posicion {posicion}")
        posicion += 1
else:
    print("No se encontro la letra")


#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
cantidad=0
n=int(input("Número: "))
while n!=0:
 primo=True
 for i in range(2,n):
   if n%i==0:
     primo=False
     break
 if primo:
   cantidad+=1
 n=int(input("Número: "))
print("primos: ", cantidad)

#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
mayor=-1
n=int(input("Número positivo:"))
while n>=0:
   if n>mayor:
       mayor=n
   n=int(input("Número positivo:"))
print("Mayor número ingresado:", mayor)

#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
facturas = {}
cobrado = 0
pendiente = 0
more = ''
while more != 'T':
    if more == 'A':
        clave = input('Introduce el número de la factura: ')
        coste = float(input('Introduce el coste de la factura: '))
        facturas[clave] = coste
        pendiente += coste
    if more == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste
    print('Recaudado:', cobrado)
    print('Pendiente de cobro: ', pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')

#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
def mas_repetida(frecuencia):
    max_repeticiones = 0
    mas_repetida = ''
    for palabra, repeticiones in frecuencia.items():
        if repeticiones > max_repeticiones:
            mas_repetida = palabra
            max_repeticiones = repeticiones
    return mas_repetida, max_repeticiones
frase = input('Introduce una frase: ')
frecuencia = contar_palabras(frase)
palabra, repeticiones = mas_repetida(frecuencia)
print('La palabra más repetida es', palabra, 'que se repite', repeticiones, 'veces')

#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def cuadrados(lista):
    cuadrados = []
    for i in lista:
        cuadrados.append(i ** 2)
    return cuadrados
print(cuadrados([1, 2, 3, 4, 5]))

#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def media(lista):
    return sum(lista) / len(lista)
print(media([1, 2, 3, 4, 5]))

#Escribir una función que reciba un número entero positivo y devuelva su factorial.
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
print(factorial(5))

#Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
def descuento(precio, descuento):
    return precio - precio * descuento / 100
def iva(precio, porcentaje):
    return precio + precio * porcentaje / 100
def precio_final(productos, funcion):
    total = 0
    for precio, porcentaje in productos.items():
        total += funcion(precio, porcentaje)
    return total
productos = {1000:10, 500:5, 100:1}
print('Precio final con descuentos:', precio_final(productos, descuento))
print('Precio final con IVA:', precio_final(productos, iva))

#Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.
def es_par(n):
    return n % 2 == 0
def filtrar(funcion, lista):
    lista_filtrada = []
    for e in lista:
        if funcion(e):
            lista_filtrada.append(e)
    return lista_filtrada
print(filtrar(es_par, [1, 2, 3, 4, 5, 6]))

#Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
def calificaciones(diccionario):
    calificaciones = {}
    for asignatura, nota in diccionario.items():
        calificaciones[asignatura.upper()] = nota
    return calificaciones
print(calificaciones({'Matemáticas': 10, 'Física': 9, 'Química': 8}))

#Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra.
def puntuacion_tipica(valor, media, desviacion_tipica):
    return (valor - media) / desviacion_tipica
def valores_atipicos(muestra):
    media_muestra = sum(muestra) / len(muestra)
    cuadrados = []
    for i in muestra:
        cuadrados.append((i - media_muestra) ** 2)
    desviacion_tipica_muestra = (sum(cuadrados) / len(muestra)) ** 0.5
    atipicos = []
    for i in muestra:
        puntuacion = puntuacion_tipica(i, media_muestra, desviacion_tipica_muestra)
        if puntuacion > 3 or puntuacion < -3:
            atipicos.append(i)
    return atipicos
print(valores_atipicos([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
vegetariana = input('¿Quiere una pizza vegetariana? (Si/No): ')
if vegetariana == 'Si':
    print('Los ingredientes de las pizzas vegetarianas son: Pimiento y Tofu')
    ingrediente = input('¿Qué ingrediente quiere? (Pimiento/Tofu): ')
    print('Su pizza vegetariana de mozzarella, tomate y', ingrediente)
else:
    print('Los ingredientes de las pizzas no vegetarianas son: Peperoni, Jamón y Salmón')
    ingrediente = input('¿Qué ingrediente quiere? (Peperoni/Jamón/Salmón): ')
    print('Su pizza no vegetariana de mozzarella, tomate y', ingrediente)

#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == 'Si'

#Quiero que te imagines un concesionario de motos. Esta clase será para representar sus motocicletas.

# Crea una clase vacía llamada "motocicleta".
# Todas las motocicletas del concesionario son nuevas. Por lo tanto, vamos a añadir un atributo de clase para especificar ese valor siempre en todas las motos.
# Ahora, crea el método __init__ vacío, con el que le daremos unos valores a las nuevas instancias.
# Añade los siguientes parámetros al __init__:
# color.
# matricula.
# combustible_litros.
# numero_ruedas.
# marca.
# modelo.
# fecha_fabricacion.
# velocidad_punta.
# peso.
# Opcionalmente, puedes añadir más atributos para describir cualquier cosa sobre las motocicletas, por ejemplo, cilindrada, tipo de transmisión y tantas otras cosas que podrían describir una motocicleta.
#
# Añade otro atributo de clase. Este va a ser "motor". Lo utilizaremos con un valor booleano para especificar si el motor está en marcha o detenido. True, en marcha. False, detenido. Por defecto, quiero que todos los motores vengan detenidos.
# Crea dos métodos inteligentes, arrancar y detener que representarán estas dos acciones con las motocicletas. Estos deben ser capaces de informar en la consola de las siguientes cosas.
# Método arrancar():
#
# Si el motor está detenido, se indica que el motor ha arrancado.
# Si el motor está ya en marcha y se intenta arrancar de nuevo, se indica que el motor ya estaba en marcha.
# Método detener():
#
# Si el motor está en marcha, se indica que el motor se ha detenido.
# Si el motor está ya detenido, y se intenta detener de nuevo, se indica que el motor ya estaba detenido.
# Instancia una motocicleta. La mayoría de argumentos son libres, pero quiero que algunos, tengan los siguientes valores:
# combustible litros = 10
# numero_ruedas = 2
# Crea otra instancia de Motocicleta. Esta vez, quiero que utilices los argumentos de clave en lugar de los posicionales. Vimos este tema con las funciones. Funciona igual en las instanciaciones que en las llamadas de función. Además, quiero que el orden no sea el mismo que necesitas para los argumentos posicionales. Esta nueva motocicleta tiene el depósito vacío.
# Prueba los dos métodos de arranque y detención con una o con las dos motocicletas. Haz las pruebas que quieras. El requisito es solo saber llamar a un método.
# El concesionario ya tiene precio para una de las motocicletas. Añade, desde fuera de la clase, este nuevo atributo con un valor para uno de los dos objetos. Soy consciente de que sería mejor añadir el atributo precio a la clase y que lo tuvieran ya todos los objetos, pero es para que practiques diferentes cosas. No borres en ningún momento de los otros ejercicios la asignación de este precio.
# Imprime el valor que acabas de añadir desde fuera de la clase con una frase como esta:
# "El precio de la motocicleta 'x (marca y modelo)' es de 'x_precio' $."
#
# Ahora, quiero que añadas una forma de consultar el precio desde la clase con un método (lo mismo, que en el ejercicio 11, pero con un método).
# Llama al nuevo método con las dos motocicletas. ¿Qué ocurre con una de ellas?
# Para finalizar, crea un nuevo método en la clase, que sea capaz de repostar las motocicletas. Para esto, necesitarás lo siguiente:
# Crea un método para comprobar la cantidad de combustible que tienen las motocicletas. Este servirá para informarnos del estado antes de iniciar el repostaje.
# En este método, se deberá indicar la cantidad de litros que tiene de combustible, la capacidad máxima del tanque de combustible y los litros que faltan para llenar el depósito.
# La salida de este método debe ser una especie de reporte. Pon todo lo anterior y añade un título personalizado con el nombre de la motocicleta que se consulta. Por ejemplo, --> Reporte del depósito de "marca x y modelo x de motocicleta" <--.
# Establecer un tope de depósito que indicaremos especialmente para cada motocicleta con un nuevo atributo. Por ejemplo, la primera tiene una capacidad máxima de 17 litros de combustible. La otra de 20.
# Crear un método que se utilice para poner la cantidad de litros que se quieren repostar. Esto se indicará en la consola por un input().
# Si la cantidad de litros es superior a la de la capacidad que hay en el depósito, se deberá advertir de que no se puede repostar esa cantidad y se le dejará intentarlo de nuevo las veces que haga falta.
# En cambio, si el repostaje es correcto, se indicará en consola la cantidad de litros que tiene la motocicleta.
# No solo hay que indicar la cantidad de combustible que tendrá la motocicleta, tiene que ser efectivo el cambio.
# En el vídeo correspondiente a este día 11 del curso, podrás ver un ejemplo orientativo de la salida en la consola, seguro que así consigues hacerlo más fácil.

class moto:
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.motor = False
    def arrancar(self):
        if self.motor:
            print("El motor ya estaba en marcha")
        else:
            self.motor = True
            print("El motor ha arrancado")
    def detener(self):
        if self.motor:
            self.motor = False
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido")
    def precio(self):
        self.precio = 1000
        print(f"El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio} $")
    def repostar(self):
        print(f"Reporte del depósito de {self.marca} {self.modelo} de motocicleta")
        print(f"La cantidad de litros que tiene de combustible es de {self.combustible_litros}")
        print(f"La capacidad máxima del tanque de combustible es de 17 litros")
        print(f"Los litros que faltan para llenar el depósito son de {17 - self.combustible_litros}")
        self.repostar = int(input("Ingrese la cantidad de litros que se quieren repostar: "))
        if self.repostar > 17 - self.combustible_litros:
            print("No se puede repostar esa cantidad")
        else:
            self.combustible_litros += self.repostar
            print(f"La cantidad de litros que tiene la motocicleta es de {self.combustible_litros}")
moto1 = moto("rojo", "1234", 10, 2, "honda", "cb190r", "2021", 120, 150)
