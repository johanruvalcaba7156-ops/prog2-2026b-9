def validar_texto(valor, campo):
    """Valida que un valor sea texto no vacío y elimina espacios extremos."""
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} no puede estar vacío.")
    return valor.strip()


def validar_entero_positivo(valor, campo):
    """Valida que un valor sea un número entero mayor que cero."""
    if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
        raise ValueError(f"{campo} debe ser un entero positivo.")
    return valor