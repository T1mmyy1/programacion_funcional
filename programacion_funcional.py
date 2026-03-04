# ============================================================
# Práctica: Programación Funcional en Python
# ============================================================

from functools import reduce


# ------------------------------------------------------------
# Ejercicio 1: Función pura suma(a, b)
# Solo depende de sus parámetros (sin efectos secundarios)
# ------------------------------------------------------------

def suma(a, b):
    """Función pura: retorna la suma de a y b."""
    return a + b

print("=" * 50)
print("Ejercicio 1: Función pura suma(a, b)")
print("=" * 50)
print(f"suma(3, 5)   = {suma(3, 5)}")
print(f"suma(10, -4) = {suma(10, -4)}")
print(f"suma(0, 0)   = {suma(0, 0)}")


# ------------------------------------------------------------
# Ejercicio 2: Función recursiva factorial(n)
# ------------------------------------------------------------

def factorial(n):
    """Calcula el factorial de n de forma recursiva.
    Caso base: factorial(0) = 1
    Caso recursivo: factorial(n) = n * factorial(n - 1)
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("\n" + "=" * 50)
print("Ejercicio 2: Factorial recursivo")
print("=" * 50)
for i in range(8):
    print(f"factorial({i}) = {factorial(i)}")


# ------------------------------------------------------------
# Ejercicio 3: Función recursiva Fibonacci(n)
# Retorna el n-ésimo número de la secuencia de Fibonacci
# ------------------------------------------------------------

def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva.
    Caso base: fibonacci(0) = 0, fibonacci(1) = 1
    Caso recursivo: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    """
    if n < 0:
        raise ValueError("n debe ser un entero no negativo.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n" + "=" * 50)
print("Ejercicio 3: Fibonacci recursivo")
print("=" * 50)
for i in range(11):
    print(f"fibonacci({i:2d}) = {fibonacci(i)}")


# ------------------------------------------------------------
# Ejercicio 4: map, filter y reduce sobre [1..10]
# ------------------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\n" + "=" * 50)
print("Ejercicio 4: map, filter y reduce")
print("=" * 50)
print(f"Lista original: {numeros}")

# -- 4a: Cuadrados con map --
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"\n[map] Cuadrados de cada número:")
print(f"  {cuadrados}")

# -- 4b: Números pares con filter --
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"\n[filter] Números pares:")
print(f"  {pares}")

# -- 4c: Suma de [1..10] con reduce --
suma_total = reduce(lambda acum, x: acum + x, numeros)
print(f"\n[reduce] Suma de [1..10]:")
print(f"  {' + '.join(map(str, numeros))} = {suma_total}")

# -- 4d: Producto de [1..5] con reduce --
primeros_cinco = [1, 2, 3, 4, 5]
producto = reduce(lambda acum, x: acum * x, primeros_cinco)
print(f"\n[reduce] Producto de [1..5]:")
print(f"  {' × '.join(map(str, primeros_cinco))} = {producto}")

print("\n" + "=" * 50)
print("✔ Todos los ejercicios completados.")
print("=" * 50)
