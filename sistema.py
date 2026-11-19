import json
from pathlib import Path

from asignacion import Asignacion
from docente import Docente
from estudiante import Estudiante
from materia import Materia


class SistemaEscolar:
    """Gestiona los registros y asignaciones del sistema escolar."""

    def __init__(self, periodo_actual):
        """Inicializa el sistema con el periodo académico indicado."""
        if not isinstance(periodo_actual, str) or not periodo_actual.strip():
            raise ValueError("El periodo actual no puede estar vacío.")

        self._periodo_actual = periodo_actual.strip()
        self._estudiantes = {}
        self._docentes = {}
        self._materias = {}
        self._asignaciones = []

    @property
    def periodo_actual(self):
        """Devuelve el periodo académico activo."""
        return self._periodo_actual

    @property
    def estudiantes(self):
        """Devuelve una copia del diccionario de estudiantes."""
        return dict(self._estudiantes)

    @property
    def docentes(self):
        """Devuelve una copia del diccionario de docentes."""
        return dict(self._docentes)

    @property
    def materias(self):
        """Devuelve una copia del diccionario de materias."""
        return dict(self._materias)

    @property
    def asignaciones(self):
        """Devuelve una copia de la lista de asignaciones."""
        return list(self._asignaciones)

    def _restaurar_estado(
        self, periodo_actual, estudiantes, docentes, materias, asignaciones
    ):
        """Reemplaza internamente el estado del sistema tras validar datos cargados."""
        if not isinstance(periodo_actual, str) or not periodo_actual.strip():
            raise ValueError("El periodo cargado no es válido.")

        self._periodo_actual = periodo_actual.strip()
        self._estudiantes = estudiantes
        self._docentes = docentes
        self._materias = materias
        self._asignaciones = asignaciones

    @staticmethod
    def _existe_clave(contenedor, clave):
        """Verifica si una clave ya existe sin distinguir mayúsculas o minúsculas."""
        clave_normalizada = clave.lower()
        return any(k.lower() == clave_normalizada for k in contenedor)

    # Contrato: registrar(objeto)
    def registrar(self, objeto):
        """Registra un estudiante, docente o materia en el sistema."""
        if isinstance(objeto, Estudiante):
            clave = objeto.matricula
            contenedor = self._estudiantes
            tipo = "estudiante"
        elif isinstance(objeto, Docente):
            clave = objeto.numero_empleado
            contenedor = self._docentes
            tipo = "docente"
        elif isinstance(objeto, Materia):
            clave = objeto.clave
            contenedor = self._materias
            tipo = "materia"
        else:
            raise TypeError("Solo se pueden registrar estudiantes, docentes o materias.")

        if self._existe_clave(contenedor, clave):
            if tipo == "estudiante":
                raise ValueError(f"La matrícula '{clave}' ya está registrada.")
            raise ValueError(f"Ya existe un {tipo} con el identificador '{clave}'.")

        if isinstance(objeto, Materia) and objeto.codigo_docente not in self._docentes:
            raise ValueError(
                f"No existe el docente '{objeto.codigo_docente}' en los registros."
            )

        contenedor[clave] = objeto

    # Contrato: asignar(identificador, clave)
    def asignar(self, identificador, clave):
        """Inscribe a un estudiante en una materia disponible."""
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("La matrícula del estudiante no puede estar vacía.")
        if not isinstance(clave, str) or not clave.strip():
            raise ValueError("La clave de la materia no puede estar vacía.")

        identificador = identificador.strip()
        clave = clave.strip()

        if identificador not in self._estudiantes:
            raise ValueError(
                f"El estudiante con matrícula '{identificador}' no existe."
            )

        if clave not in self._materias:
            raise ValueError(f"La materia con clave '{clave}' no fue encontrada.")

        materia = self._materias[clave]
        docente = materia.codigo_docente

        if docente not in self._docentes:
            raise ValueError(
                f"El docente '{docente}' asignado a la materia no está registrado."
            )

        for asignacion in self._asignaciones:
            if (
                asignacion.matricula == identificador
                and asignacion.clave == clave
                and asignacion.periodo == self._periodo_actual
            ):
                raise ValueError(
                    "El estudiante ya tiene registrada esa materia en este periodo."
                )

        inscritos = sum(
            1
            for asignacion in self._asignaciones
            if asignacion.clave == clave
            and asignacion.periodo == self._periodo_actual
        )

        if inscritos >= materia.cupo_maximo:
            raise ValueError(
                f"La materia '{clave}' ya alcanzó su cupo máximo ({materia.cupo_maximo})."
            )

        self._asignaciones.append(
            Asignacion(identificador, clave, docente, self._periodo_actual)
        )

    # Contrato: listar()
    def listar(self):
        """Muestra en pantalla todos los registros usando polimorfismo."""
        secciones = [
            ("ESTUDIANTES", self._estudiantes.values()),
            ("DOCENTES", self._docentes.values()),
            ("MATERIAS", self._materias.values()),
            ("ASIGNACIONES", self._asignaciones),
        ]

        for titulo, registros in secciones:
            print(f"\n--- {titulo} ---")
            registros = list(registros)

            if not registros:
                print("No hay registros.")
            else:
                for registro in registros:
                    print(registro.describir())


def _validar_ruta(ruta):
    """Valida y convierte la ruta de archivo a un objeto Path."""
    if isinstance(ruta, Path):
        if not str(ruta).strip():
            raise ValueError("La ruta del archivo no puede estar vacía.")
        return ruta
    if isinstance(ruta, str) and ruta.strip():
        return Path(ruta.strip())
    raise ValueError("La ruta del archivo debe ser una cadena válida.")


# Contrato: guardar(sistema, ruta)
def guardar(sistema, ruta):
    """Guarda los datos del sistema en un archivo JSON."""
    if not isinstance(sistema, SistemaEscolar):
        raise TypeError("Se esperaba una instancia de SistemaEscolar.")

    datos = {
        "periodo_actual": sistema.periodo_actual,
        "estudiantes": [
            {
                "matricula": e.matricula,
                "nombre": e.nombre,
                "carrera": e.carrera,
            }
            for e in sistema.estudiantes.values()
        ],
        "docentes": [
            {
                "numero_empleado": d.numero_empleado,
                "nombre": d.nombre,
                "departamento": d.departamento,
            }
            for d in sistema.docentes.values()
        ],
        "materias": [
            {
                "clave": m.clave,
                "nombre": m.nombre,
                "creditos": m.creditos,
                "cupo_maximo": m.cupo_maximo,
                "codigo_docente": m.codigo_docente,
            }
            for m in sistema.materias.values()
        ],
        "asignaciones": [
            {
                "matricula": a.matricula,
                "clave": a.clave,
                "codigo_docente": a.codigo_docente,
                "periodo": a.periodo,
            }
            for a in sistema.asignaciones
        ],
    }

    try:
        archivo_ruta = _validar_ruta(ruta)
        archivo_ruta.parent.mkdir(parents=True, exist_ok=True)
        with archivo_ruta.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
    except (OSError, TypeError, ValueError) as error:
        raise RuntimeError(
            f"Falló el almacenamiento persistente: {error}"
        ) from error


# Contrato: cargar(sistema, ruta)
def cargar(sistema, ruta):
    """Carga los datos del sistema desde un archivo JSON."""
    if not isinstance(sistema, SistemaEscolar):
        raise TypeError("Se esperaba una instancia de SistemaEscolar.")

    try:
        archivo_ruta = _validar_ruta(ruta)
    except ValueError as error:
        raise RuntimeError(f"Ruta inválida: {error}") from error

    if not archivo_ruta.exists():
        return

    try:
        with archivo_ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, dict):
            raise ValueError("El formato raíz del archivo debe ser un objeto JSON.")

        lista_estudiantes = datos.get("estudiantes", [])
        lista_docentes = datos.get("docentes", [])
        lista_materias = datos.get("materias", [])
        lista_asignaciones = datos.get("asignaciones", [])

        if not all(
            isinstance(seccion, list)
            for seccion in (
                lista_estudiantes,
                lista_docentes,
                lista_materias,
                lista_asignaciones,
            )
        ):
            raise ValueError("Las colecciones del archivo deben ser listas.")

        estudiantes = {}
        for e in lista_estudiantes:
            est = Estudiante(e["matricula"], e["nombre"], e["carrera"])
            estudiantes[est.matricula] = est

        docentes = {}
        for d in lista_docentes:
            doc = Docente(d["numero_empleado"], d["nombre"], d["departamento"])
            docentes[doc.numero_empleado] = doc

        materias = {}
        for m in lista_materias:
            mat = Materia(
                m["clave"],
                m["nombre"],
                m["creditos"],
                m["cupo_maximo"],
                m["codigo_docente"],
            )
            if mat.codigo_docente not in docentes:
                raise ValueError(
                    f"La materia '{mat.clave}' referencia al docente inexistente '{mat.codigo_docente}'."
                )
            materias[mat.clave] = mat

        asignaciones = []
        for a in lista_asignaciones:
            asig = Asignacion(
                a["matricula"],
                a["clave"],
                a["codigo_docente"],
                a["periodo"],
            )
            if asig.matricula not in estudiantes or asig.clave not in materias:
                raise ValueError("Hay asignaciones con estudiantes o materias inexistentes.")
            asignaciones.append(asig)

        sistema._restaurar_estado(
            datos.get("periodo_actual", sistema.periodo_actual),
            estudiantes,
            docentes,
            materias,
            asignaciones,
        )

    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        raise RuntimeError(
            f"No se pudieron cargar los datos del archivo: {error}"
        ) from error