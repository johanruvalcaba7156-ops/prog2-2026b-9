from validaciones import validar_texto


class Asignacion:
    """Representa la inscripción de un estudiante a una materia."""

    def __init__(self, matricula, clave, codigo_docente, periodo):
        """Inicializa una asignación validando sus identificadores."""
        self._matricula = validar_texto(matricula, "La matrícula")
        self._clave = validar_texto(clave, "La clave de la materia")
        self._codigo_docente = validar_texto(codigo_docente, "El código del docente")
        self._periodo = validar_texto(periodo, "El periodo")

    @property
    def matricula(self):
        """Devuelve la matrícula del estudiante asignado."""
        return self._matricula

    @property
    def clave(self):
        """Devuelve la clave de la materia asignada."""
        return self._clave

    @property
    def codigo_docente(self):
        """Devuelve el código del docente de la asignación."""
        return self._codigo_docente

    @property
    def periodo(self):
        """Devuelve el periodo académico de la asignación."""
        return self._periodo

    def describir(self):
        """Devuelve los datos formateados de la asignación."""
        return (
            f"Matrícula: {self._matricula} | Materia: {self._clave} | "
            f"Docente: {self._codigo_docente} | Periodo: {self._periodo}"
        )