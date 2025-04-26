import pdfkit
import platform
from jinja2 import Environment, FileSystemLoader
import tempfile
from datetime import datetime

# Configuración automática según sistema operativo
if platform.system() == "Windows":
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
else:
    config = None  # Linux / MacOS normalmente no necesita configurar

def generar_reporte_pdf(productos: list):
    env = Environment(loader=FileSystemLoader("app/pdf/templates"))
    template = env.get_template("report.html")
    html_out = template.render(productos=productos, fecha=datetime.now().strftime("%d/%m/%Y %H:%M %p"))

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdfkit.from_string(html_out, tmp_file.name, configuration=config)
        return tmp_file.name
