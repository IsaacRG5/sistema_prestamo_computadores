
# Sistema de Préstamo de Computadores

## Descripción

Este proyecto consiste en una aplicación de consola desarrollada en Python que permite gestionar el préstamo y la devolución de computadores dentro de un centro de formación.

El sistema facilita el registro de computadores, la consulta de disponibilidad, el registro de préstamos y el control de las devoluciones.

## Objetivo

Desarrollar un sistema sencillo que permita organizar y controlar los préstamos de computadores, evitando que un mismo equipo sea prestado a más de una persona al mismo tiempo.

## Tecnologías utilizadas

- Python 3
- Visual Studio Code (editor recomendado)
- Git y GitHub (control de versiones)

## Estructura del proyecto

```text
prestamo-computadores/
│
├── prestamos.py
└── README.md
```

## Funcionalidades

El sistema cuenta con las siguientes opciones:

1. Registrar computador: permite agregar un computador con su código.
2. Consultar computadores: muestra los equipos registrados y su disponibilidad.
3. Prestar computador: registra el nombre y documento del aprendiz, el computador y la fecha del préstamo.
4. Devolver computador: registra la devolución de un equipo prestado.
5. Consultar préstamos: muestra los registros de préstamos.
6. Salir: permite cerrar el programa.

## Requisitos

Para ejecutar el proyecto necesitas:

- Tener Python 3 instalado.
- Tener acceso a una terminal o consola.
- Descargar o clonar el proyecto.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar a la carpeta del proyecto

```bash
cd prestamo-computadores
```

### 3. Ejecutar el programa

```bash
python prestamos.py
```

Si el comando anterior no funciona en Windows, prueba:

```bash
py prestamos.py
```

## Ejemplo del menú

```text
===== SISTEMA DE PRÉSTAMO DE COMPUTADORES =====

1. Registrar computador
2. Consultar computadores
3. Prestar computador
4. Devolver computador
5. Consultar préstamos
6. Salir

Seleccione una opción:
```

## Conceptos de Python utilizados

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos:

- Variables: almacenan información del sistema.
- Listas: permiten guardar computadores y préstamos.
- Diccionarios: organizan los datos de cada computador y préstamo.
- Funciones: dividen el programa en tareas específicas.
- Condicionales: permiten tomar decisiones.
- Ciclos while: mantienen activo el menú.
- Validaciones: evitan registrar información obligatoria vacía.

## Limitaciones

- La información se almacena temporalmente en memoria.
- Al cerrar el programa, los datos registrados se pierden.
- Las fechas se reciben como texto y no se valida su formato.
- No cuenta con una base de datos.

## Autor

Desarrollado como proyecto de aprendizaje para practicar programación en Python, lógica de programación y organización de información.

## Licencia

Proyecto desarrollado con fines educativos.
