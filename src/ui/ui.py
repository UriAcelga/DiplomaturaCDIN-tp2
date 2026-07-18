import flet as ft

class UI:
    def __init__(self,
                  callback_importar_csv,
                  callback_listar_ventas,
                  callback_listar_clientes_vendedores,
                  callback_listar_mayor_vendedor_activo,
                  callback_listar_vendedores_antiguedad,
                  callback_delete):
        self.fn_importar_csv = callback_importar_csv
        self.fn_listar_ventas = callback_listar_ventas
        self.fn_listar_clientes_vendedores = callback_listar_clientes_vendedores
        self.fn_listar_mayor_vendedor_activo = callback_listar_mayor_vendedor_activo
        self.fn_listar_vendedores_antiguedad = callback_listar_vendedores_antiguedad
        self.fn_delete = callback_delete
        
        self.TITLE = "Diplomatura CDIN - TP2"
    

    
    def ui(self, page: ft.Page):
        page.title = self.TITLE
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.add(
            ft.SafeArea(
                expand=True,
                content=ft.Container(
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        alignment=ft.Alignment.CENTER,
                        controls=[
                            ft.Button(
                                content="Importar datos CSV",
                                on_click=self.fn_importar_csv
                            ),
                            ft.Button(
                                content="Eliminar imports",
                                on_click=self.fn_delete
                            ),
                            ft.Button(
                                content="Listar ventas",
                                on_click=self.fn_listar_ventas
                            ),
                            ft.Button(
                                content="Listar vendedores con antigüedad",
                                on_click=self.fn_listar_vendedores_antiguedad
                            ),
                            ft.Button(
                                content="Listar clientes / vendedores",
                                on_click=self.fn_listar_clientes_vendedores
                            ),
                            ft.Button(
                                content="Mayor vendedor activo",
                                on_click=self.fn_listar_mayor_vendedor_activo
                            ),
                            ft.Button(
                                content="Listar vendedores con antigüedad",
                                on_click=self.fn_listar_vendedores_antiguedad
                            ),
                            ft.Button(
                                content="Exit Program",
                                on_click=page.window.close
                            )
                        ],
                    )
                )
            )
        )

    def run_ui(self):
        ft.run(self.ui)