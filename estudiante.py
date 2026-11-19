from persona import Persona
from validaciones import validar_texto


class Estudiante(Persona):
    """Representa a un estudiante inscrito en una carrera."""

    def __init__(self, matricula, nombre, carrera):
        """Inicializa un estudiante con matrícula, nombre y carrera."""
        super().__init__(matricula, nombre)
        self._carrera = validar_texto(carrera, "La carrera")

    @property
    def matricula(self):
        """Devuelve la matrícula del estudiante."""
        return self._identificador

    @property
    def carrera(self):
        """Devuelve la carrera del estudiante."""
        return self._carrera

    def describir(self):
        """Devuelve los datos formateados del estudiante."""
        return (
            f"Estudiante | Matrícula: {self._identificador} | "
            f"Nombre: {self._nombre} | Carrera: {self._carrera}"
        )