import os
import pandas as pd
from sqlalchemy import create_engine
from app import Database as db
from exceptions import CSVError, CSVFileNotFoundError, CSVEmptyDataError

class DB:
    insert_ventas = ""
    insert_personas = "INSERT INTO personas (nombre, domicilio, nacionalidad, cuil) VALUES (%s, %s, %s, %s) RETURNING id"
    insert_clientes = "INSERT INTO clientes (persona_id, estado) VALUES (%s, %s)"
    insert_vendedores = "INSERT INTO vendedores (persona_id, desde, estado) VALUES (%s, %s::date, %s)"

    listar_ventas = ""
    reporte_clientes = ""
    listar_personas = ""
    mayor_vendedor = ""
    vendedores_antiguedad = ""
    @staticmethod
    def conn():
        engine = create_engine(db.DB_URL, echo=True)
        return engine

    @staticmethod
    def run_query(engine, q):
        with engine.connect() as conn, conn.begin():
            result = pd.read_sql_query(q, conn)
            return result
    
    @staticmethod
    def importar_csv(engine, file, query):
        try:
            df_result = pd.read_csv(file)
        except FileNotFoundError as e:
            print(f"No se encontró el archivo {file}: {e}")
            raise CSVFileNotFoundError("El archivo CSV no existe en la ruta especificada.")
        except pd.errors.EmptyDataError as e:
            print(f"El archivo {file} está vacío: {e}")
            raise CSVEmptyDataError("El archivo CSV no tiene entradas válidas.")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")
            raise CSVError(f"Error al procesar el archivo {file}.")