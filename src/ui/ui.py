import flet as ft

def ui(page: ft.Page):
    page.title = "Diplomatura CDIN - TP2"
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
                            content="Importar datos CSV"
                        ),
                        ft.Button(
                            content="Listar ventas"
                        ),
                        ft.Button(
                            content="Listar clientes / vendedores"
                        ),
                        ft.Button(
                            content="Mayor vendedor activo"
                        ),
                        ft.Button(
                            content="Listar vendedores con antigüedad"
                        )
                    ],
                )
            )
        )
    )

def run_ui():
    ft.run(ui)