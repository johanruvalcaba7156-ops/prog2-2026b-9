from abc import ABC, abstractmethod

from validaciones import validar_texto


class Persona(ABC):
    """Clase base abstracta que representa a una persona en el sistema."""

    def __init__(self, identificador, nombre):
        """Inicializa los atributos internos de una persona."""
        self._identificador = validar_texto(identificador, "La identificación")
        self._nombre = validar_texto(nombre, "El nombre")

    @property
    def identificador(self):
        """Devuelve el identificador de la persona."""
        return self._identificador

    @property
    def nombre(self):
        """Devuelve el nombre de la persona."""
        return self._nombre

    @abstractmethod
    def describir(self):
        """Devuelve una representación en texto de la persona."""