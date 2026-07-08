from pathlib import Path

class Rutas:
    BASE_DIR = Path(__file__).resolve().parent.parent
    PUBLIC_DIR = BASE_DIR / "public"
    REPORTES_DIR = PUBLIC_DIR / "reportes"
        
    @classmethod
    def ruta_reportes(cls, file_name: str = "") -> str:
        return str(cls.REPORTES_DIR / file_name)
    
