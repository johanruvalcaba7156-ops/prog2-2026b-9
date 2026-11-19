from validaciones import validar_entero_positivo, validar_texto


class Materia:
    """Representa una materia académica con créditos, cupo y docente."""

    def __init__(self, clave, nombre, creditos, cupo_maximo, codigo_docente):
        """Inicializa una materia validando sus datos."""
        self._clave = validar_texto(clave, "La clave")
        self._nombre = validar_texto(nombre, "El nombre de la materia")
        self._creditos = validar_entero_positivo(creditos, "La cantidad de créditos")
        self._cupo_maximo = validar_entero_positivo(cupo_maximo, "El cupo máximo")
        self._codigo_docente = validar_texto(codigo_docente, "El código del docente")

    @property
    def clave(self):
        """Devuelve la clave de la materia."""
        return self._clave

    @property
    def nombre(self):
        """Devuelve el nombre de la materia."""
        return self._nombre

    @property
    def creditos(self):
        """Devuelve los créditos de la materia."""
        return self._creditos

    @property
    def cupo_maximo(self):
        """Devuelve el cupo máximo de la materia."""
        return self._cupo_maximo

    @property
    def codigo_docente(self):
        """Devuelve el código del docente asignado."""
        return self._codigo_docente

    def describir(self):
        """Devuelve los datos formateados de la materia."""
        return (
            f"Materia | Clave: {self._clave} | Nombre: {self._nombre} | "
            f"Créditos: {self._creditos} | Cupo: {self._cupo_maximo} | "
            f"Docente: {self._codigo_docente}"
        )