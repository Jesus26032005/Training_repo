# 🧑‍💻 Training Repo — Tu entrenamiento diario de programación

Este repositorio es tu gimnasio de código. Cada noche (medianoche, hora de Monterrey) un tutor revisa lo que hiciste y, cuando estás listo, publica un lote nuevo de ejercicios.

## ¿Cómo funciona?

1. **Se publica un lote** de 10 ejercicios en un solo archivo dentro de `ejercicios/`, por ejemplo `ejercicios/2026-10-09_python.py`. La fecha es el día en que se creó el lote.
2. **Los lenguajes se alternan**: Python, Kotlin, Python, Kotlin... La dificultad sube poco a poco, desde cero.
3. **Tú resuelves** los ejercicios editando directamente el archivo: reemplazas el `TODO` y `raise NotImplementedError` (o `TODO("tu solución aquí")` en Kotlin) por tu código.
4. **Haces commit y push** a la rama `main` con tus soluciones.
5. **Esa noche el tutor revisa tu código** y deja comentarios `# RETRO:` (o `// RETRO:` en Kotlin) justo encima de cada función que intentaste.
6. **Si los 10 están correctos**, el lote se marca como *aprobado* y aparece un lote nuevo en el otro lenguaje. Si no, se queda el mismo lote hasta que lo termines (no se acumulan lotes).

## ¿Cómo corro un archivo?

**Python**

```bash
python ejercicios/2026-10-09_python.py     # o python3
```

**Kotlin**

```bash
kotlinc ejercicios/archivo.kt -include-runtime -d lote.jar
java -jar lote.jar
```

También puedes pegar el archivo completo en [Kotlin Playground](https://play.kotlinlang.org/).

Al final del archivo hay un **corredor de pruebas** que muestra una línea por ejercicio:

- ✅ el ejercicio pasa todas las pruebas
- ❌ falla (te dice el caso, lo esperado y lo obtenido)
- ⏳ todavía no lo has resuelto

Un ejercicio sin resolver o con error **no detiene** a los demás, así que puedes avanzar a tu ritmo. Al final verás un resumen, por ejemplo `7/10 correctos`.

## ¿Cómo es la retroalimentación?

La retro vive **dentro de tu mismo código**, como comentarios encima de cada función:

- Primero te digo **qué hiciste bien**.
- Luego **qué falló y por qué**, con una **pista** (sin darte la solución completa).
- Si después de una pista el ejercicio sigue mal, en la siguiente revisión te dejo la **solución comentada línea por línea** para que aprendas de ella.
- Nunca borro ni cambio tu código; solo agrego comentarios.

## Archivos importantes

- `ejercicios/` — un archivo por lote (10 ejercicios cada uno).
- `progreso.md` — la bitácora: una fila por lote con su estado (pendiente / con errores / aprobado) y el resumen de la revisión.

## Consejos

- Intenta primero sin ayuda; las pistas llegan después.
- Corre el archivo seguido: los ejemplos del enunciado son tus primeras pruebas.
- Si te atoras, deja el ejercicio y sigue con otro. ¡No es una carrera!
