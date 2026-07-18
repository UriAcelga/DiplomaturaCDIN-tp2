from app import Rutas as r
from reportlab.pdfgen import canvas

class RlController:  
    def __init__(self, file="rl-hello_world.pdf"):
        self.file = r.ruta_reportes(file)
        self.canvas = None
        self.set_canvas_A4()

    def set_canvas_A4(self):
        self.canvas = canvas.Canvas(self.file, pagesize=(595.27, 841.89))

    def hello_world_example(self):
        self.canvas.drawString(50, 780, "Hello World!")
        # finish page
        self.canvas.showPage()
        # construct and save file to .pdf
        self.canvas.save()
    