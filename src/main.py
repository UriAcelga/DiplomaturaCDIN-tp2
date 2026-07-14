import os
import pandas as pd
from sqlalchemy import create_engine
from app import Database as db
from database.db import DB
from pdf.rlController import ReportLab
from ui.ui import run_ui


def main():
    engine = DB.conn()
    #DB.run_query(engine, "SELECT * FROM clientes;")
    print("Hello from diplomaturaCDIN-TP2!")
    rl = ReportLab()
    #rl.hello_world_example()

    run_ui()

if __name__ == "__main__":
    main()

""" FLET
def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=counter,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


ft.run(main)
"""