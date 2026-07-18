from database.db import DB
class UsuariosController:
    def __init__(self, engine):
        self.engine = engine
        self.db = DB

    def importar_csv(self):
        #importar personas archivo clientes

        #importar clientes archivo clientes

        #importar personas archivo vendedores

        #importar vendedores archivo vendedores

        #importar ventas archivo ventas
        print("Ejecucion importar csv")

    def listar_ventas(self):
        #usuarios = self.engine.obtener_usuarios()
        #return usuarios
        print("Ejecucion listar ventas")


    def listar_clientes_vendedores(self):
        print("Ejecucion listar clientes y vendedores")

    def listar_mayor_vendedor_activo(self):
        print("Ejecucion mayor vendedor activo")
        

    def listar_vendedores_antiguedad(self):
        print("Ejecucion vendedores antigüedad")

    '''
    Elimina los imports previos.
    Función peligrosa, se usa sólo para demostrar
    funcionamiento de los imports.
    '''
    def eliminar_imports(self):
        # ejecucion delete para clientes, vendedores, personas y ventas_por_producto

        # reiniciar los id
        
        print("Ejecucion eliminar imports")