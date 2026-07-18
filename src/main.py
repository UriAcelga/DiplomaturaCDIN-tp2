import os
import pandas as pd
from sqlalchemy import create_engine
from app import Database as db
from database.db import DB
from controllers.rlController import RlController
from controllers.UsuariosController import UsuariosController
from ui.ui import UI


def main():
    engine = DB.conn()
    #DB.run_query(engine, "SELECT * FROM clientes;")
    print("Hello from diplomaturaCDIN-TP2!")
    #Controlador ReportLab para exportar a pdf
    rl = RlController()
    #rl.hello_world_example()


    #Controlador db
    user = UsuariosController(engine)
    
    #Inicializa app flet
    ui = UI(callback_importar_csv=user.importar_csv,
            callback_listar_ventas=user.listar_ventas,
            callback_listar_clientes_vendedores=user.listar_clientes_vendedores,
            callback_listar_mayor_vendedor_activo=user.listar_mayor_vendedor_activo,
            callback_listar_vendedores_antiguedad=user.listar_vendedores_antiguedad,
            callback_delete=user.eliminar_imports)
    ui.run_ui()

if __name__ == "__main__":
    main()