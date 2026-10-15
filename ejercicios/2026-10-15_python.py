# =============================================================================
# LOTE 3 · PYTHON · Bucles y textos
# Tema: for, while, range, acumuladores, listas simples y recorrer strings
# Nivel general: inicial-intermedio (1 a 10, de más fácil a más difícil)
#
# CÓMO USAR ESTE ARCHIVO
#   1. Busca cada función que tenga `# TODO: tu solución aquí`.
#   2. Borra el `raise NotImplementedError` y escribe tu solución (usa `return`).
#   3. Corre el archivo desde la terminal:   python archivo.py   (o python3)
#   4. Verás una línea por ejercicio: ✅ correcto, ❌ falló, ⏳ sin resolver.
#   5. Cada noche reviso tu avance y dejo comentarios `# RETRO:` en tu código.
#
# Idea clave de este lote: casi todos se resuelven con un "acumulador"
# (una variable que empieza vacía o en 0 y va cambiando dentro del bucle).
# No necesitas resolverlos todos de una vez. ¡Tú puedes!
# =============================================================================

# =============================================================================
# EJERCICIO 1 · Suma hasta n
# Nivel: 1
#
# Devuelve la suma de los enteros desde 1 hasta n (incluido), usando un bucle
# `for` con `range`. Si n es 0 o negativo, devuelve 0.
#
# Ejemplos:
#   suma_hasta(5)  ->  15   (1 + 2 + 3 + 4 + 5)
#   suma_hasta(0)  ->  0
# =============================================================================
def suma_hasta(n):
    # TODO: tu solución aquí
    raise NotImplementedError

# =============================================================================
# EJERCICIO 2 · Tabla de multiplicar
# Nivel: 2
#
# Devuelve una lista con los resultados de n*1, n*2, ..., n*10.
#
# Ejemplos:
#   tabla_multiplicar(3)  ->  [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
#   tabla_multiplicar(0)  ->  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# =============================================================================
def tabla_multiplicar(n):
    # TODO: tu solución aquí
    raise NotImplementedError

# =============================================================================
# EJERCICIO 3 · Contar pares
# Nivel: 3
#
# Recibe una lista de enteros y devuelve cuántos son pares. Recorre la lista
# con `for` y usa un contador.
#
# Ejemplos:
#   contar_pares([1, 2, 3, 4])  ->  2
#   contar_pares([])  ->  0
# =============================================================================
def contar_pares(lista):
    # TODO: tu solución aquí
    raise NotImplementedError

# =============================================================================
# EJERCICIO 4 · Cuenta regresiva
# Nivel: 4
#
# Usa un bucle `while` para devolver una lista que va de n hasta 1 (de mayor a
# menor). Si n es 0 o negativo, devuelve la lista vacía.
#
# Ejemplos:
#   cuenta_regresiva(3)  ->  [3, 2, 1]
#   cuenta_regresiva(0)  ->  []
# =============================================================================
def cuenta_regresiva(n):
    # TODO: tu solución aquí
    raise NotImplementedError

# =============================================================================
# EJERCICIO 5 · Invertir texto
# Nivel: 5
#
# Devuelve el texto al revés. Hazlo con un bucle (sin usar `[::-1]` ni
# `reversed`); luego, si quieres, compara con la forma corta.
#
# Ejemplos:
#   invertir_texto("hola")  ->  "aloh"
#   invertir_texto("")  ->  ""
# =============================================================================
def invertir_texto(texto):
    # TODO: tu solución aquí
    raise NotImplementedError

# =============================================================================
# EJERCICIO 6 · Contar una letra
# Nivel: 5
#
# Cuenta cuántas veces aparece `letra` (un solo carácter) en `texto`, sin
# importar mayúsculas o minúsculas. No uses el método `.count()`.
#
# Ejemplos:
#   contar_letra("Banana", "a")  ->  3
#   contar_letra("Hola", "z")  ->  0
# =============================================================================
def contar_letra(texto, letra):
    # TODO: tu solución aquí
    raise NotImplementedError

# =============================================================================
# EJERCICIO 7 · ¿Es palíndromo?
# Nivel: 6
#
# Devuelve True si el texto se lee igual al derecho y al revés, ignorando
# espacios y mayúsculas/minúsculas (los acentos no se consideran: no habrá en
# las pruebas).
#
# Ejemplos:
#   es_palindromo("Anita lava la tina")  ->  True
#   es_palindromo("Python")  ->  False
# =============================================================================
def es_palindromo(texto):
    # TODO: tu solución aquí
    raise NotImplementedError

# =============================================================================
# EJERCICIO 8 · Factorial
# Nivel: 7
#
# Devuelve n! (n * (n-1) * ... * 1) usando un bucle. Por definición 0! = 1. No
# uses `math.factorial`.
#
# Ejemplos:
#   factorial(5)  ->  120
#   factorial(0)  ->  1
# =============================================================================
def factorial(n):
    # TODO: tu solución aquí
    raise NotImplementedError

# =============================================================================
# EJERCICIO 9 · FizzBuzz
# Nivel: 8
#
# Devuelve una lista de textos con los números de 1 a n, pero: si el número es
# múltiplo de 3 pon "Fizz", si es múltiplo de 5 pon "Buzz", y si es múltiplo
# de ambos pon "FizzBuzz". Los demás números van como texto (por ejemplo "1").
#
# Ejemplos:
#   fizzbuzz(5)  ->  ["1", "2", "Fizz", "4", "Buzz"]
#   fizzbuzz(15)[-1]  ->  "FizzBuzz"
# =============================================================================
def fizzbuzz(n):
    # TODO: tu solución aquí
    raise NotImplementedError

# =============================================================================
# EJERCICIO 10 · ¿Es primo?
# Nivel: 9
#
# Devuelve True si n es un número primo (solo divisible entre 1 y entre sí
# mismo). Ojo: 0, 1 y los negativos NO son primos. Pista general: basta probar
# divisores hasta la raíz cuadrada de n, pero probar hasta n-1 también vale.
#
# Ejemplos:
#   es_primo(17)  ->  True
#   es_primo(21)  ->  False   (3 * 7)
# =============================================================================
def es_primo(n):
    # TODO: tu solución aquí
    raise NotImplementedError


# =============================================================================
# CORREDOR DE PRUEBAS — no necesitas modificar nada de aquí hacia abajo
# =============================================================================
def _iguales(obtenido, esperado):
    """Compara resultados; evita que True == 1 pase como correcto."""
    return type(obtenido) is type(esperado) and obtenido == esperado


PRUEBAS = [
    (1, "Suma hasta n", "suma_hasta", [
        ((5,), 15),
        ((0,), 0),
        ((1,), 1),
        ((-3,), 0),
        ((100,), 5050),
    ]),
    (2, "Tabla de multiplicar", "tabla_multiplicar", [
        ((3,), [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]),
        ((0,), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        ((-2,), [-2, -4, -6, -8, -10, -12, -14, -16, -18, -20]),
    ]),
    (3, "Contar pares", "contar_pares", [
        (([1, 2, 3, 4],), 2),
        (([],), 0),
        (([1, 3, 5],), 0),
        (([0, -2, 8],), 3),
        (([7],), 0),
    ]),
    (4, "Cuenta regresiva", "cuenta_regresiva", [
        ((3,), [3, 2, 1]),
        ((0,), []),
        ((1,), [1]),
        ((-2,), []),
        ((5,), [5, 4, 3, 2, 1]),
    ]),
    (5, "Invertir texto", "invertir_texto", [
        (('hola',), 'aloh'),
        (('',), ''),
        (('a',), 'a'),
        (('Hola Mundo',), 'odnuM aloH'),
    ]),
    (6, "Contar una letra", "contar_letra", [
        (('Banana', 'a'), 3),
        (('Hola', 'z'), 0),
        (('Mississippi', 'S'), 4),
        (('', 'x'), 0),
        (('AaAa', 'a'), 4),
    ]),
    (7, "¿Es palíndromo?", "es_palindromo", [
        (('Anita lava la tina',), True),
        (('Python',), False),
        (('',), True),
        (('a',), True),
        (('Ana',), True),
        (('Dabale arroz a la zorra el abad',), True),
        (('hola mundo',), False),
    ]),
    (8, "Factorial", "factorial", [
        ((5,), 120),
        ((0,), 1),
        ((1,), 1),
        ((10,), 3628800),
        ((3,), 6),
    ]),
    (9, "FizzBuzz", "fizzbuzz", [
        ((5,), ['1', '2', 'Fizz', '4', 'Buzz']),
        ((0,), []),
        ((1,), ['1']),
        ((15,), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']),
    ]),
    (10, "¿Es primo?", "es_primo", [
        ((17,), True),
        ((21,), False),
        ((2,), True),
        ((1,), False),
        ((0,), False),
        ((-7,), False),
        ((97,), True),
        ((100,), False),
        ((49,), False),
        ((3,), True),
    ]),
]


def correr_pruebas():
    correctos = 0
    for numero, titulo, nombre_funcion, casos in PRUEBAS:
        etiqueta = f"Ejercicio {numero:>2} · {titulo}"
        try:
            funcion = globals()[nombre_funcion]
            fallo = None
            for argumentos, esperado in casos:
                obtenido = funcion(*argumentos)
                if not _iguales(obtenido, esperado):
                    fallo = (argumentos, esperado, obtenido)
                    break
            if fallo is None:
                print(f"✅ {etiqueta}")
                correctos += 1
            else:
                args, esperado, obtenido = fallo
                print(f"❌ {etiqueta}  -> {nombre_funcion}{args}: "
                      f"esperado {esperado!r}, obtenido {obtenido!r}")
        except NotImplementedError:
            print(f"⏳ {etiqueta}  (sin resolver)")
        except Exception as error:
            print(f"❌ {etiqueta}  -> error: {type(error).__name__}: {error}")
    print(f"\nResumen: {correctos}/{len(PRUEBAS)} correctos")


if __name__ == "__main__":
    correr_pruebas()
