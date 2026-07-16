import os
import pandas as pd
from sqlalchemy import create_engine
from app import Database as db
from exceptions import CSVError, CSVFileNotFoundError, CSVEmptyDataError

class DB:
    #es importante el orden, ventas al final
    insert_personas = "INSERT INTO personas (nombre, domicilio, nacionalidad, cuil) VALUES (%s, %s, %s, %s) RETURNING id"
    insert_clientes = "INSERT INTO clientes (persona_id, estado) VALUES (%s, %s)"
    insert_vendedores = "INSERT INTO vendedores (persona_id, desde, estado) VALUES (%s, %s::date, %s)"
    insert_ventas = "INSERT INTO ventas_por_producto (producto_id, cliente_id, fecha, cantidad, precio_unitario, porcentaje_descuento, vendedor_id) VALUES (%s, %s, %s::date, %s, %s, %s, %s)"

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
    def leer_csv(file):
        try:
            df_nuevos = pd.read_csv(file)
            return df_nuevos
        except FileNotFoundError as e:
            print(f"No se encontró el archivo {file}: {e}")
            raise CSVFileNotFoundError("El archivo CSV no existe en la ruta especificada.")
        except pd.errors.EmptyDataError as e:
            print(f"El archivo {file} está vacío: {e}")
            raise CSVEmptyDataError("El archivo CSV no tiene entradas válidas.")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")
            raise CSVError(f"Error al procesar el archivo {file}.")
        
    @classmethod
    def importar_personas_desde_csv(cls, engine, dataframe):
        if dataframe.empty:
            raise CSVEmptyDataError("El DataFrame está vacío. No se pueden importar datos.")
        
        ids = []
        with engine.connect() as conn, conn.begin():
            for i, fila in dataframe.iterrows():
                id = conn.execute(cls.insert_personas, {
                    'nombre': fila['Nombre'],
                    'domicilio': fila['Domicilio'],
                    'nacionalidad': fila['Nacionalidad'],
                    'cuil': fila['CUIL']
                }).scalar()
                ids.append(id)
        return ids
    
    @classmethod
    def importar_clientes_desde_csv(cls, engine, dataframe):
        dataframe = cls.remover_duplicados_df(engine, dataframe, 'personas', 'cuil')
        if dataframe.empty:
            raise CSVEmptyDataError("El DataFrame está vacío. No se pueden importar datos.")
        try:
            ids = cls.importar_personas_desde_csv(engine, dataframe)
        except CSVEmptyDataError as e:
            print(f"Error al importar personas: {e}")
            raise

        with engine.connect() as conn, conn.begin():
            for i, fila in dataframe.iterrows():
                conn.execute(cls.insert_clientes, {
                    'persona_id': ids[i],
                    'estado': fila['Estado']
                })

    @classmethod
    def importar_vendedores_desde_csv(cls, engine, dataframe):
        dataframe = cls.remover_duplicados_df(engine, dataframe, 'personas', 'cuil')
        if dataframe.empty:
            raise CSVEmptyDataError("El DataFrame está vacío. No se pueden importar datos.")
        try:
            ids = cls.importar_personas_desde_csv(engine, dataframe)
        except CSVEmptyDataError as e:
            print(f"Error al importar personas: {e}")
            raise

        with engine.connect() as conn, conn.begin():
            for i, fila in dataframe.iterrows():
                conn.execute(cls.insert_vendedores, {
                    'persona_id': ids[i],
                    'desde': fila['Desde'],
                    'estado': fila['Estado']
                })

    @classmethod
    def remover_duplicados_df(cls, engine, dataframe, table, columna_clave):
        with engine.connect() as conn, conn.begin():
            res = conn.execute(f"SELECT {columna_clave} FROM {table}")
        if res.rowcount == 0:
            return dataframe
        else:
            clave = {fila[columna_clave] for fila in res.fetchall()}
            df_nuevo = dataframe[~dataframe[columna_clave].isin(clave)]
            return df_nuevo