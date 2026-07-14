class CSVError(Exception):
    """Excepción base para errores relacionados con el CSV."""
    pass

class CSVFileNotFoundError(CSVError):
    """El archivo CSV no existe en la ruta especificada."""
    pass

class CSVEmptyDataError(CSVError):
    """El archivo no tiene entradas válidas."""
    pass