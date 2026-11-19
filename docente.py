from persona import Persona
from validaciones import validar_texto

class Docente(Persona):
    """Representa a un docente adscrito a un departamento."""

    def __init__(self, numero_empleado, nombre, departamento):
        """Inicializa un docente con número de empleado, nombre y departamento."""
        super().__init__(numero_empleado, nombre)
        self._departamento = validar_texto(departamento, "El departamento")

    @property
    def numero_empleado(self):
        """Devuelve el número de empleado del docente."""
        return self._identificador

    @property
    def departamento(self):
        """Devuelve el departamento del docente."""
        return self._departamento

    def describir(self):
        """Devuelve los datos formateados del docente."""
        return (
            f"Docente | Número: {self._identificador} | "
            f"Nombre: {self._nombre} | Departamento: {self._departamento}"
        )