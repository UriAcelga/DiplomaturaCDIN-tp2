import os
from dotenv import load_dotenv
from pathlib import Path

class Rutas:
    BASE_DIR = Path(__file__).resolve().parent.parent
    PUBLIC_DIR = BASE_DIR / "public"
    REPORTES_DIR = PUBLIC_DIR / "reportes"
    APP_DIR = Path(__file__).resolve()
    FLET_DIR = APP_DIR / "flet"
        
    @classmethod
    def ruta_reportes(cls, file_name: str = "") -> str:
        return str(cls.REPORTES_DIR / file_name)
    
class Database:
    load_dotenv()
    ENGINE = os.getenv("DB_ENGINE")
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    DBNAME = os.getenv("DB_NAME")

    DB_URL = f'{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require'