class Docente:
    """Representa a un docente."""

    def __init__(self, codigo, nombre, departamento):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento

    @classmethod
    def registrar(cls):
        """Pide los datos y crea un docente."""
        codigo = input("Código del docente: ").strip()
        nombre = input("Nombre del docente: ").strip()
        departamento = input("Departamento: ").strip()

        if not codigo or not nombre or not departamento:
            raise ValueError("Todos los campos son obligatorios.")

        return cls(codigo, nombre, departamento)

    def obtener_datos(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "departamento": self.departamento,
        }

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Departamento: {self.departamento}"
        )