# =============================================================================
# LOTE 1 · PYTHON · Fundamentos
# Tema: print, variables, tipos de datos, operadores, conversiones y condicionales
# Nivel general: inicial (1 a 10, de más fácil a más difícil)
#
# CÓMO USAR ESTE ARCHIVO
#   1. Busca cada función que tenga `# TODO: tu solución aquí`.
#   2. Borra el `raise NotImplementedError` y escribe tu solución (usa `return`).
#   3. Corre el archivo desde la terminal:   python archivo.py   (o python3)
#   4. Verás una línea por ejercicio: ✅ correcto, ❌ falló, ⏳ sin resolver.
#   5. Cada noche reviso tu avance y dejo comentarios `# RETRO:` en tu código.
#
# No necesitas resolverlos todos de una vez: un ejercicio sin resolver
# no rompe a los demás. ¡Tú puedes!
# =============================================================================


# =============================================================================
# EJERCICIO 1 · Saludo
# Nivel: 1
#
# Escribe una función que reciba un nombre (texto) y devuelva el saludo
# "¡Hola, <nombre>!".
#
# Ejemplos:
#   saludo("Jesús")  ->  "¡Hola, Jesús!"
#   saludo("Ana")    ->  "¡Hola, Ana!"
# =============================================================================
# RETRO: ¡Bien! El f-string está perfecto y devuelve justo lo pedido.
# Mejora opcional: el f-string ya es un texto, así que `str(...)` sobra; basta `return f"¡Hola, {nombre}!"`.
def saludo(nombre):
    return str(f"¡Hola, {nombre}!")


# =============================================================================
# EJERCICIO 2 · Área de un rectángulo
# Nivel: 1
#
# Devuelve el área de un rectángulo (base * altura).
#
# Ejemplos:
#   area_rectangulo(3, 4)    ->  12
#   area_rectangulo(2.5, 2)  ->  5.0
# =============================================================================
# RETRO: Correcto y directo: base * altura funciona con enteros y decimales sin más. Nada que mejorar.
def area_rectangulo(base, altura):
    return base * altura


# =============================================================================
# EJERCICIO 3 · De Celsius a Fahrenheit
# Nivel: 2
#
# Convierte grados Celsius a Fahrenheit con la fórmula:  F = C * 9 / 5 + 32
#
# Ejemplos:
#   celsius_a_fahrenheit(0)    ->  32.0
#   celsius_a_fahrenheit(100)  ->  212.0
# =============================================================================
# RETRO: Muy bien, la fórmula está bien traducida y el orden de operaciones es correcto.
# Mejora opcional de estilo: deja un espacio alrededor del operador (`+ 32`) para que se lea mejor (PEP 8).
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 +32


# =============================================================================
# EJERCICIO 4 · ¿Es par?
# Nivel: 3
#
# Devuelve True si el número entero es par y False si es impar.
# Pista de concepto: el operador % te da el residuo de una división.
#
# Ejemplos:
#   es_par(4)  ->  True
#   es_par(7)  ->  False
# =============================================================================
# RETRO: Correcto, usaste bien el residuo (%) y cubres pares e impares (también negativos).
# Mejora opcional: `n % 2 == 0` ya ES un True/False, así que puedes escribir solo `return n % 2 == 0`.
def es_par(n):
    if n%2==0:
        return True
    else:
        return False


# =============================================================================
# EJERCICIO 5 · Suma de textos numéricos
# Nivel: 4
#
# Recibes dos TEXTOS que contienen números enteros (por ejemplo "12" y "30").
# Devuelve la suma como número entero (no como texto).
#
# Ejemplos:
#   suma_de_textos("12", "30")  ->  42
#   suma_de_textos("5", "-2")   ->  3
# =============================================================================
# RETRO: Perfecto: convertir con int() antes de sumar es justo la idea. Funciona incluso con "-2".
def suma_de_textos(a, b):
    return int(a) + int(b)


# =============================================================================
# EJERCICIO 6 · Tipo de dato
# Nivel: 5
#
# Devuelve el nombre en español del tipo del valor recibido:
#   int -> "entero", float -> "decimal", str -> "texto", bool -> "booleano"
# Cuidado: en Python, True y False también "cuentan" como int. ¡El orden de
# tus condiciones importa!
#
# Ejemplos:
#   tipo_de_dato(7)      ->  "entero"
#   tipo_de_dato(True)   ->  "booleano"
#   tipo_de_dato("hola") ->  "texto"
# =============================================================================
# RETRO: Excelente, entendiste la trampa: revisar bool ANTES que int es la clave. Buen manejo del `else` final.
# Mejora opcional: usar `if / if / if` (sin elif) también sirve porque cada rama hace return.
def tipo_de_dato(valor):
    if isinstance(valor,bool):
        return "booleano"
    if isinstance(valor, int):
        return "entero"
    elif isinstance(valor,float):
        return "decimal"
    elif isinstance(valor,str):
        return "texto"
    else:
        return "otro tipo"


# =============================================================================
# EJERCICIO 7 · El mayor de tres
# Nivel: 6
#
# Devuelve el mayor de tres números usando if/elif/else
# (sin usar la función max()).
#
# Ejemplos:
#   mayor_de_tres(1, 5, 3)  ->  5
#   mayor_de_tres(9, 2, 9)  ->  9
# =============================================================================
# RETRO: Pasa las pruebas básicas y la estructura if/elif/else está clara, buen trabajo.
# Pero tiene un caso escondido que falla: prueba mayor_de_tres(5, 5, 3). Debería dar 5.
# ¿Qué pasa? `a > b` es falso (son iguales), `b > a` también, y se va al `else`... que devuelve c.
# PISTA: piensa qué comparación (`>` vs `>=`) deja de "descartar" a un número cuando hay empate.
# Ojo: arreglarlo puede cambiar más de una condición. Pruébalo con (5,5,3), (5,3,5) y (3,5,5).
def mayor_de_tres(a, b, c):
    if a>=b and a>=c:
            return a
    elif b>=a and b>=c:
            return b
    else: return c


# =============================================================================
# EJERCICIO 8 · Clasificar por edad
# Nivel: 7
#
# Según la edad devuelve:
#   0 a 11   -> "niño"
#   12 a 17  -> "adolescente"
#   18 a 64  -> "adulto"
#   65 o más -> "adulto mayor"
#
# Ejemplos:
#   clasificar_edad(5)   ->  "niño"
#   clasificar_edad(18)  ->  "adulto"
#   clasificar_edad(70)  ->  "adulto mayor"
# =============================================================================
# RETRO: Buena estructura: los elif encadenados con `<=` evitan repetir límites inferiores. ¡Bien pensado!
# Pero falla con edad 0 (un recién nacido): el primer `if` exige `edad > 0`, así que 0 cae en "adolescente".
# El enunciado dice "0 a 11 -> niño", o sea que el 0 SÍ cuenta.
# PISTA: revisa el límite inferior del primer if. ¿Necesitas `>`, o `>=`, o siquiera esa condición?
def clasificar_edad(edad):
    if edad >= 0 and edad <=11:
        return "niño"
    elif edad <= 17:
        return "adolescente"
    elif edad <= 64:
        return "adulto"
    elif edad >= 65:
        return "adulto mayor"
    else:
        return "desconocido"


# =============================================================================
# EJERCICIO 9 · Total con descuento
# Nivel: 8
#
# Una tienda vende artículos a un precio unitario. Según la cantidad:
#   1 a 4 artículos   -> sin descuento
#   5 a 9 artículos   -> 10% de descuento
#   10 o más          -> 20% de descuento
# Devuelve el total a pagar redondeado a 2 decimales (usa round(x, 2)).
#
# Ejemplos:
#   total_con_descuento(100, 3)   ->  300.0
#   total_con_descuento(100, 5)   ->  450.0
#   total_con_descuento(19.99, 10) ->  159.92
# =============================================================================
# RETRO: Bien resuelto: calculas el total una vez y le restas el descuento según el rango. Los límites 4/5/9/10 están bien.
# Mejora opcional: el `else: precio_final = precio_final` no hace nada y se puede quitar.
# Idea idiomática: guardar el porcentaje (0, 0.10, 0.20) en una variable según la cantidad y al final `total * (1 - descuento)`.
def total_con_descuento(precio, cantidad):
    precio_final = precio*cantidad
    if cantidad > 4 and cantidad <= 9:
        precio_final -= precio*cantidad*0.10
    elif cantidad > 9:
        precio_final -= precio*cantidad*0.20
    else:
        precio_final = precio_final
    return round(precio_final,2)


# =============================================================================
# EJERCICIO 10 · Año bisiesto
# Nivel: 10
#
# Un año es bisiesto si es divisible entre 4, EXCEPTO los divisibles entre 100,
# a menos que también sean divisibles entre 400.
# Devuelve True o False.
#
# Ejemplos:
#   es_bisiesto(2024)  ->  True
#   es_bisiesto(1900)  ->  False   (divisible entre 100 pero no entre 400)
#   es_bisiesto(2000)  ->  True    (divisible entre 400)
# =============================================================================
# RETRO: Correcto, ¡buen ejercicio difícil! Tu lógica respeta la regla completa (4, 100 y 400).
# Mejora opcional: `anio % 400 == 0` ya implica `anio % 100 == 0`, así que basta `(anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0`.
# Y como antes, puedes devolver la condición directamente en vez de if/else.
def es_bisiesto(anio):
    if (anio%4 == 0 and anio%100!=0) or (anio%400==0 and anio%100==0):
        return True
    else:
        return False


# =============================================================================
# CORREDOR DE PRUEBAS — no necesitas modificar nada de aquí hacia abajo
# =============================================================================
def _iguales(obtenido, esperado):
    """Compara resultados; para decimales tolera diferencias minúsculas."""
    if isinstance(esperado, float) and isinstance(obtenido, (int, float)) \
            and not isinstance(obtenido, bool):
        return abs(obtenido - esperado) < 1e-6
    # Evita que True == 1 pase como correcto
    return type(obtenido) is type(esperado) and obtenido == esperado


PRUEBAS = [
    (1, "Saludo", "saludo", [
        (("Jesús",), "¡Hola, Jesús!"),
        (("Ana",), "¡Hola, Ana!"),
        (("",), "¡Hola, !"),
    ]),
    (2, "Área de un rectángulo", "area_rectangulo", [
        ((3, 4), 12),
        ((2.5, 2), 5.0),
        ((0, 10), 0),
    ]),
    (3, "De Celsius a Fahrenheit", "celsius_a_fahrenheit", [
        ((0,), 32.0),
        ((100,), 212.0),
        ((-40,), -40.0),
        ((37,), 98.6),
    ]),
    (4, "¿Es par?", "es_par", [
        ((4,), True),
        ((7,), False),
        ((0,), True),
        ((-3,), False),
    ]),
    (5, "Suma de textos numéricos", "suma_de_textos", [
        (("12", "30"), 42),
        (("5", "-2"), 3),
        (("0", "0"), 0),
    ]),
    (6, "Tipo de dato", "tipo_de_dato", [
        ((7,), "entero"),
        ((3.14,), "decimal"),
        (("hola",), "texto"),
        ((True,), "booleano"),
        ((False,), "booleano"),
    ]),
    (7, "El mayor de tres", "mayor_de_tres", [
        ((1, 5, 3), 5),
        ((9, 2, 9), 9),
        ((-1, -5, -3), -1),
        ((4, 4, 4), 4),
        ((7, 1, 2), 7),
        ((5, 5, 3), 5),
        ((3, 5, 5), 5),
        ((5, 3, 5), 5),
    ]),
    (8, "Clasificar por edad", "clasificar_edad", [
        ((0,), "niño"),
        ((5,), "niño"),
        ((11,), "niño"),
        ((12,), "adolescente"),
        ((17,), "adolescente"),
        ((18,), "adulto"),
        ((64,), "adulto"),
        ((65,), "adulto mayor"),
        ((90,), "adulto mayor"),
    ]),
    (9, "Total con descuento", "total_con_descuento", [
        ((100, 3), 300.0),
        ((100, 5), 450.0),
        ((100, 9), 810.0),
        ((100, 10), 800.0),
        ((19.99, 10), 159.92),
        ((50, 1), 50.0),
    ]),
    (10, "Año bisiesto", "es_bisiesto", [
        ((2024,), True),
        ((1900,), False),
        ((2000,), True),
        ((2023,), False),
        ((2100,), False),
        ((1996,), True),
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
