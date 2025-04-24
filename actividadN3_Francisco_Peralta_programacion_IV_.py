
# Ejercicio 1: Máximo entre tres números
def maximo_de_tres(a, b, c):
    # Simplemente usamos la función max para esto
    return max(a, b, c)

# Ejercicio 2: Máximo entre diez números
def maximo_de_diez(numeros):
    # Le damos la lista de números y le pedimos al maximo que haga su magia
    return max(numeros)

# Ejercicio 3: Sumar vectores
def cargar_vector(tamano):
    # Cargamos un vector de tamaño 'tamano'
    vector = []
    for i in range(tamano):
        num = int(input(f"Ingrese el número {i+1}: "))
        vector.append(num)
    return vector

def suma_vectores(a, b):
    # Suma de vectores, si son del mismo tamaño
    if len(a) == len(b):
        return [x + y for x, y in zip(a, b)]
    else:
        print("Los vectores no tienen la misma longitud.")
        return []

# Ejercicio 4: Contar vocales y consonantes
def contar_vocales(palabra):
    return sum(1 for letra in palabra.lower() if letra in 'aeiou')

def contar_consonantes(palabra):
    return sum(1 for letra in palabra.lower() if letra.isalpha() and letra not in 'aeiou')

# Ejercicio 5: Potencia, dígitos y capicúa
def potencia(x, k):
    return x ** k

def cantidad_digitos(n):
    return len(str(abs(n)))

def es_capicua(n):
    s = str(abs(n))
    return s == s[::-1]

# Ejercicio 6: Sumar o multiplicar matrices
def cargar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"Ingrese el valor para la posición ({i+1},{j+1}): ")))
        matriz.append(fila)
    return matriz

def sumar_matrices(a, b):
    # Suma de matrices, si son del mismo tamaño
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    else:
        print("Las matrices no tienen el mismo tamaño.")
        return []

def multiplicar_matrices(a, b):
    # Multiplicación de matrices, con verificación básica
    if len(a[0]) != len(b):
        print("No se pueden multiplicar las matrices.")
        return []
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Ejercicio 7: Operaciones con matriz y factorial
import math

def suma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))

def calcular_factorial(n):
    return math.factorial(n)

def eliminar_repetidos(vector):
    return list(set(vector))

def ordenar_vector(vector):
    return sorted(vector)

# Aquí termina el código hasta el ejercicio 7
