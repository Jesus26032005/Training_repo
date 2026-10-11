// =============================================================================
// LOTE 2 · KOTLIN · Fundamentos
// Tema: val/var, tipos, funciones, if como expresión, when y rangos
// Nivel general: inicial (1 a 10, de más fácil a más difícil)
//
// CÓMO USAR ESTE ARCHIVO
//   1. Busca cada función que tenga `// TODO: tu solución aquí`.
//   2. Borra la línea `TODO("tu solución aquí")` y escribe tu solución.
//      Puedes usar `return ...` o el cuerpo de expresión: fun f(x: Int) = x + 1
//   3. Corre el archivo de una de estas formas:
//        kotlinc archivo.kt -include-runtime -d lote.jar && java -jar lote.jar
//      o pega TODO el archivo en https://play.kotlinlang.org/
//   4. Verás una línea por ejercicio: ✅ correcto, ❌ falló, ⏳ sin resolver.
//   5. Cada noche reviso tu avance y dejo comentarios `// RETRO:` en tu código.
//
// Un ejercicio sin resolver no rompe a los demás. ¡Tú puedes!
// =============================================================================


// =============================================================================
// EJERCICIO 1 · Saludo con plantilla
// Nivel: 1
//
// Devuelve el saludo "¡Hola, <nombre>! Bienvenido a Kotlin".
// Pista de concepto: en Kotlin los strings aceptan plantillas con $variable.
//
// Ejemplos:
//   saludar("Jesús")  ->  "¡Hola, Jesús! Bienvenido a Kotlin"
//   saludar("Ana")    ->  "¡Hola, Ana! Bienvenido a Kotlin"
// =============================================================================
fun saludar(nombre: String): String {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// EJERCICIO 2 · Perímetro de un rectángulo
// Nivel: 1
//
// Devuelve el perímetro de un rectángulo: 2 * (base + altura).
//
// Ejemplos:
//   perimetroRectangulo(3, 4)  ->  14
//   perimetroRectangulo(5, 5)  ->  20
// =============================================================================
fun perimetroRectangulo(base: Int, altura: Int): Int {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// EJERCICIO 3 · Promedio de tres notas
// Nivel: 2
//
// Recibes tres notas enteras y devuelves su promedio como Double.
// Cuidado: en Kotlin, Int / Int es una división ENTERA (se pierden los
// decimales). Convierte con .toDouble() antes de dividir.
//
// Ejemplos:
//   promedio(10, 8, 9)  ->  9.0
//   promedio(7, 8, 8)   ->  7.666666666666667
// =============================================================================
fun promedio(a: Int, b: Int, c: Int): Double {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// EJERCICIO 4 · El mayor de dos (if como expresión)
// Nivel: 3
//
// Devuelve el mayor de dos enteros usando un `if` como EXPRESIÓN
// (sin usar maxOf ni max). Por ejemplo: val r = if (x > y) x else y
//
// Ejemplos:
//   mayorDeDos(3, 8)   ->  8
//   mayorDeDos(10, 10) ->  10
// =============================================================================
fun mayorDeDos(a: Int, b: Int): Int {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// EJERCICIO 5 · ¿Es vocal?
// Nivel: 4
//
// Devuelve true si el carácter es una vocal (a, e, i, o, u), sin importar si
// es mayúscula o minúscula. Usa `when` con varias opciones separadas por coma.
// No se consideran las vocales con acento.
//
// Ejemplos:
//   esVocal('a')  ->  true
//   esVocal('E')  ->  true
//   esVocal('z')  ->  false
// =============================================================================
fun esVocal(c: Char): Boolean {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// EJERCICIO 6 · Nombre del día
// Nivel: 5
//
// Recibe un número del 1 al 7 y devuelve el día de la semana, donde 1 es
// "lunes", 2 "martes", 3 "miércoles", 4 "jueves", 5 "viernes", 6 "sábado" y
// 7 "domingo". Cualquier otro número devuelve "inválido". Usa `when`.
//
// Ejemplos:
//   nombreDelDia(1)  ->  "lunes"
//   nombreDelDia(7)  ->  "domingo"
//   nombreDelDia(9)  ->  "inválido"
// =============================================================================
fun nombreDelDia(numero: Int): String {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// EJERCICIO 7 · ¿Está dentro del rango?
// Nivel: 6
//
// Devuelve true si `n` está entre `desde` y `hasta`, ambos INCLUIDOS.
// Usa un rango con el operador `in`:  n in desde..hasta
//
// Ejemplos:
//   estaEnRango(5, 1, 10)   ->  true
//   estaEnRango(10, 1, 10)  ->  true
//   estaEnRango(11, 1, 10)  ->  false
// =============================================================================
fun estaEnRango(n: Int, desde: Int, hasta: Int): Boolean {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// EJERCICIO 8 · Suma de un rango
// Nivel: 7
//
// Devuelve la suma de todos los enteros desde `inicio` hasta `fin`, ambos
// incluidos. Si `inicio` es mayor que `fin`, devuelve 0.
// Pista de concepto: un rango como 1..5 se puede recorrer con `for` o sumar
// con `.sum()`. Ojo: 5..1 es un rango vacío.
//
// Ejemplos:
//   sumaDeRango(1, 5)  ->  15   (1 + 2 + 3 + 4 + 5)
//   sumaDeRango(3, 3)  ->  3
//   sumaDeRango(5, 1)  ->  0
// =============================================================================
fun sumaDeRango(inicio: Int, fin: Int): Int {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// EJERCICIO 9 · Calificación con letra
// Nivel: 8
//
// Convierte una nota (0 a 100) en letra usando `when` con rangos:
//   90..100 -> "A"    80..89 -> "B"    70..79 -> "C"
//   60..69  -> "D"    0..59  -> "F"
// Cualquier nota fuera de 0..100 devuelve "inválida".
//
// Ejemplos:
//   calificacionLetra(95)   ->  "A"
//   calificacionLetra(70)   ->  "C"
//   calificacionLetra(101)  ->  "inválida"
// =============================================================================
fun calificacionLetra(nota: Int): String {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// EJERCICIO 10 · Tipo de triángulo
// Nivel: 10
//
// Dados los tres lados de un triángulo, devuelve:
//   "inválido"     si algún lado es <= 0, o si no se cumple la desigualdad
//                  triangular (cada lado debe ser MENOR que la suma de los otros dos)
//   "equilátero"   si los tres lados son iguales
//   "isósceles"    si exactamente dos lados son iguales
//   "escaleno"     si los tres lados son distintos
// Pista de concepto: `when` sin argumento permite condiciones libres:
//   when { condicion1 -> ...; condicion2 -> ...; else -> ... }
// ¡El orden de las condiciones importa!
//
// Ejemplos:
//   tipoDeTriangulo(3, 3, 3)  ->  "equilátero"
//   tipoDeTriangulo(3, 3, 5)  ->  "isósceles"
//   tipoDeTriangulo(3, 4, 5)  ->  "escaleno"
//   tipoDeTriangulo(1, 2, 3)  ->  "inválido"
// =============================================================================
fun tipoDeTriangulo(a: Int, b: Int, c: Int): String {
    // TODO: tu solución aquí
    TODO("tu solución aquí")
}


// =============================================================================
// CORREDOR DE PRUEBAS — no necesitas modificar nada de aquí hacia abajo
// =============================================================================
class Caso(val descripcion: String, val esperado: Any, val obtener: () -> Any)

fun iguales(obtenido: Any, esperado: Any): Boolean =
    if (esperado is Double && obtenido is Double) Math.abs(obtenido - esperado) < 1e-6
    else obtenido == esperado

class Ejercicio(val numero: Int, val titulo: String, val casos: List<Caso>)

fun construirEjercicios(): List<Ejercicio> = listOf(
    Ejercicio(1, "Saludo con plantilla", listOf(
        Caso("saludar(\"Jesús\")", "¡Hola, Jesús! Bienvenido a Kotlin") { saludar("Jesús") },
        Caso("saludar(\"Ana\")", "¡Hola, Ana! Bienvenido a Kotlin") { saludar("Ana") },
        Caso("saludar(\"\")", "¡Hola, ! Bienvenido a Kotlin") { saludar("") },
    )),
    Ejercicio(2, "Perímetro de un rectángulo", listOf(
        Caso("perimetroRectangulo(3, 4)", 14) { perimetroRectangulo(3, 4) },
        Caso("perimetroRectangulo(5, 5)", 20) { perimetroRectangulo(5, 5) },
        Caso("perimetroRectangulo(0, 7)", 14) { perimetroRectangulo(0, 7) },
    )),
    Ejercicio(3, "Promedio de tres notas", listOf(
        Caso("promedio(10, 8, 9)", 9.0) { promedio(10, 8, 9) },
        Caso("promedio(7, 8, 8)", 23.0 / 3) { promedio(7, 8, 8) },
        Caso("promedio(0, 0, 1)", 1.0 / 3) { promedio(0, 0, 1) },
        Caso("promedio(5, 5, 5)", 5.0) { promedio(5, 5, 5) },
    )),
    Ejercicio(4, "El mayor de dos", listOf(
        Caso("mayorDeDos(3, 8)", 8) { mayorDeDos(3, 8) },
        Caso("mayorDeDos(8, 3)", 8) { mayorDeDos(8, 3) },
        Caso("mayorDeDos(10, 10)", 10) { mayorDeDos(10, 10) },
        Caso("mayorDeDos(-5, -2)", -2) { mayorDeDos(-5, -2) },
    )),
    Ejercicio(5, "¿Es vocal?", listOf(
        Caso("esVocal('a')", true) { esVocal('a') },
        Caso("esVocal('E')", true) { esVocal('E') },
        Caso("esVocal('u')", true) { esVocal('u') },
        Caso("esVocal('O')", true) { esVocal('O') },
        Caso("esVocal('z')", false) { esVocal('z') },
        Caso("esVocal('B')", false) { esVocal('B') },
        Caso("esVocal('1')", false) { esVocal('1') },
    )),
    Ejercicio(6, "Nombre del día", listOf(
        Caso("nombreDelDia(1)", "lunes") { nombreDelDia(1) },
        Caso("nombreDelDia(3)", "miércoles") { nombreDelDia(3) },
        Caso("nombreDelDia(6)", "sábado") { nombreDelDia(6) },
        Caso("nombreDelDia(7)", "domingo") { nombreDelDia(7) },
        Caso("nombreDelDia(0)", "inválido") { nombreDelDia(0) },
        Caso("nombreDelDia(8)", "inválido") { nombreDelDia(8) },
        Caso("nombreDelDia(-1)", "inválido") { nombreDelDia(-1) },
    )),
    Ejercicio(7, "¿Está dentro del rango?", listOf(
        Caso("estaEnRango(5, 1, 10)", true) { estaEnRango(5, 1, 10) },
        Caso("estaEnRango(1, 1, 10)", true) { estaEnRango(1, 1, 10) },
        Caso("estaEnRango(10, 1, 10)", true) { estaEnRango(10, 1, 10) },
        Caso("estaEnRango(0, 1, 10)", false) { estaEnRango(0, 1, 10) },
        Caso("estaEnRango(11, 1, 10)", false) { estaEnRango(11, 1, 10) },
        Caso("estaEnRango(-3, -5, -1)", true) { estaEnRango(-3, -5, -1) },
    )),
    Ejercicio(8, "Suma de un rango", listOf(
        Caso("sumaDeRango(1, 5)", 15) { sumaDeRango(1, 5) },
        Caso("sumaDeRango(3, 3)", 3) { sumaDeRango(3, 3) },
        Caso("sumaDeRango(5, 1)", 0) { sumaDeRango(5, 1) },
        Caso("sumaDeRango(-2, 2)", 0) { sumaDeRango(-2, 2) },
        Caso("sumaDeRango(1, 100)", 5050) { sumaDeRango(1, 100) },
    )),
    Ejercicio(9, "Calificación con letra", listOf(
        Caso("calificacionLetra(100)", "A") { calificacionLetra(100) },
        Caso("calificacionLetra(90)", "A") { calificacionLetra(90) },
        Caso("calificacionLetra(89)", "B") { calificacionLetra(89) },
        Caso("calificacionLetra(80)", "B") { calificacionLetra(80) },
        Caso("calificacionLetra(75)", "C") { calificacionLetra(75) },
        Caso("calificacionLetra(60)", "D") { calificacionLetra(60) },
        Caso("calificacionLetra(59)", "F") { calificacionLetra(59) },
        Caso("calificacionLetra(0)", "F") { calificacionLetra(0) },
        Caso("calificacionLetra(101)", "inválida") { calificacionLetra(101) },
        Caso("calificacionLetra(-1)", "inválida") { calificacionLetra(-1) },
    )),
    Ejercicio(10, "Tipo de triángulo", listOf(
        Caso("tipoDeTriangulo(3, 3, 3)", "equilátero") { tipoDeTriangulo(3, 3, 3) },
        Caso("tipoDeTriangulo(3, 3, 5)", "isósceles") { tipoDeTriangulo(3, 3, 5) },
        Caso("tipoDeTriangulo(5, 3, 3)", "isósceles") { tipoDeTriangulo(5, 3, 3) },
        Caso("tipoDeTriangulo(3, 5, 3)", "isósceles") { tipoDeTriangulo(3, 5, 3) },
        Caso("tipoDeTriangulo(3, 4, 5)", "escaleno") { tipoDeTriangulo(3, 4, 5) },
        Caso("tipoDeTriangulo(1, 2, 3)", "inválido") { tipoDeTriangulo(1, 2, 3) },
        Caso("tipoDeTriangulo(1, 1, 3)", "inválido") { tipoDeTriangulo(1, 1, 3) },
        Caso("tipoDeTriangulo(0, 0, 0)", "inválido") { tipoDeTriangulo(0, 0, 0) },
        Caso("tipoDeTriangulo(-3, -3, -3)", "inválido") { tipoDeTriangulo(-3, -3, -3) },
        Caso("tipoDeTriangulo(2, 2, 4)", "inválido") { tipoDeTriangulo(2, 2, 4) },
    )),
)

fun main() {
    var correctos = 0
    val ejercicios = construirEjercicios()
    for (ej in ejercicios) {
        val etiqueta = "Ejercicio ${ej.numero.toString().padStart(2)} · ${ej.titulo}"
        val resultado = runCatching {
            var fallo: String? = null
            for (caso in ej.casos) {
                val obtenido = caso.obtener()
                if (!iguales(obtenido, caso.esperado)) {
                    fallo = "${caso.descripcion}: esperado ${caso.esperado}, obtenido $obtenido"
                    break
                }
            }
            fallo
        }
        val error = resultado.exceptionOrNull()
        when {
            error is NotImplementedError -> println("⏳ $etiqueta  (sin resolver)")
            error != null -> println("❌ $etiqueta  -> error: ${error::class.simpleName}: ${error.message}")
            resultado.getOrNull() == null -> { println("✅ $etiqueta"); correctos++ }
            else -> println("❌ $etiqueta  -> ${resultado.getOrNull()}")
        }
    }
    println("\nResumen: $correctos/${ejercicios.size} correctos")
}
