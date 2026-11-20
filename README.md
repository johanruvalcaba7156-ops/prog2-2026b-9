# Proyecto Integrador: Sistema Escolar (tipo SIIAU)

Este programa sirve para llevar el control básico de una escuela desde la consola. Permite registrar estudiantes, docentes y materias, inscribir alumnos a sus clases y guardar toda la información en un archivo para no perderla al cerrar el programa.

## Integrantes del equipo

| Codigo | Nombre |
| :--- | :--- |
| **221233412** | Mario de Jesús Martínez Castro |
| **221471569** | Johan Daniel Ruvalcaba Vazquez |

## Que datos se registran?

| Módulo | Datos que pide |
| :--- | :--- |
| **Estudiante** | Matrícula, nombre y carrera |
| **Docente** | Número de empleado, nombre y departamento |
| **Materia** | Clave, nombre, créditos, cupo máximo y número de empleado del docente |
| **Asignación** | Matrícula del estudiante y clave de la materia (se guarda junto con el docente y el periodo) |

## Archivos del proyecto

* `main.py`: Muestra el menú principal para usar el sistema
* `sistema.py`: Tiene las funciones para registrar, asignar, listar, guardar y cargar los datos
* `persona.py`: Clase base con los datos que comparten estudiantes y docentes
* `estudiante.py`: Clase para crear y mostrar estudiantes
* `docente.py`: Clase para crear y mostrar docentes
* `materia.py`: Clase para crear y mostrar materias
* `asignacion.py`: Clase para inscribir a un estudiante en una materia.
* `validaciones.py`: Revisa que no se guarden textos vacíos ni números inválidos
* `datos_escolares.txt`: Archivo donde se guarda toda la información

## Como ejecutarlo

1. Abre una terminal en la carpeta donde están los archivos.
2. Escribe el siguiente comando:

```bash
python main.py
```

3. Usa los números del menú para elegir lo que quieras hacer y selecciona `0` para guardar y salir.
