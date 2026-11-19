from docente import Docente
from estudiante import Estudiante
from materia import Materia
from sistema import SistemaEscolar, cargar, guardar


RUTA_DATOS = "datos_escolares.txt"


def pedir_entero(mensaje):
    """Solicita y valida que el usuario ingrese un número entero."""
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Ingresa un número entero válido.")


def main():
    """Ejecuta el menú principal e interactúa con el sistema escolar."""
    sistema = SistemaEscolar(periodo_actual="2026-B")

    try:
        cargar(sistema, RUTA_DATOS)
    except RuntimeError as error:
        print(error)
        print("El sistema iniciará sin los datos del archivo.")

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Registrar estudiante")
        print("2. Registrar docente")
        print("3. Registrar materia")
        print("4. Asignar materia a estudiante")
        print("5. Listar")
        print("6. Guardar")
        print("0. Guardar y salir")

        try:
            opcion = input("Opción: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma interrumpido por el usuario.")
            break

        try:
            if opcion == "1":
                objeto = Estudiante(
                    input("Matrícula: "),
                    input("Nombre: "),
                    input("Carrera: "),
                )
                sistema.registrar(objeto)
                print("Estudiante registrado correctamente.")

            elif opcion == "2":
                objeto = Docente(
                    input("Número de empleado: "),
                    input("Nombre: "),
                    input("Departamento: "),
                )
                sistema.registrar(objeto)
                print("Docente registrado correctamente.")

            elif opcion == "3":
                objeto = Materia(
                    input("Clave: "),
                    input("Nombre de la materia: "),
                    pedir_entero("Créditos: "),
                    pedir_entero("Cupo máximo: "),
                    input("Número de empleado del docente: "),
                )
                sistema.registrar(objeto)
                print("Materia registrada correctamente.")

            elif opcion == "4":
                matricula = input("Matrícula del estudiante: ").strip()
                clave = input("Clave de la materia: ").strip()
                sistema.asignar(matricula, clave)
                print("Asignación realizada correctamente.")

            elif opcion == "5":
                sistema.listar()

            elif opcion == "6":
                guardar(sistema, RUTA_DATOS)
                print("Datos guardados.")

            elif opcion == "0":
                guardar(sistema, RUTA_DATOS)
                print("Datos guardados. Programa finalizado.")
                break

            else:
                print("Opción inválida.")

        except (ValueError, TypeError, RuntimeError) as error:
            print(f"Operación rechazada: {error}")


if __name__ == "__main__":
    main()