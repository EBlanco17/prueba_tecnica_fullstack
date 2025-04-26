import pdfkit
import platform
from jinja2 import Environment, FileSystemLoader
import tempfile
from datetime import datetime
from typing import List

"""
Este módulo se encarga de generar reportes en formato PDF utilizando plantillas HTML
y datos proporcionados. Usa la librería `pdfkit` para la conversión de HTML a PDF.
"""

# Configuración automática según sistema operativo
if platform.system() == "Windows":
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
else:
    config = None  # Linux / MacOS normalmente no necesita configurar

def generar_reporte_pdf(productos: List[dict]) -> str:
    """
    Genera un reporte en formato PDF basado en una lista de productos.

    Args:
        productos (List[dict]): Lista de productos con las claves:
            - "total_comprado" (int): Cantidad total comprada del producto.
            - "precio_unitario" (float): Precio unitario del producto.

    Returns:
        str: Ruta al archivo PDF generado.

    El reporte incluye:
        - Lista de productos con sus detalles.
        - Total de productos vendidos.
        - Precio total acumulado.
        - Fecha y hora de generación del reporte.
    """
    # Calcular el total vendido y el precio total
    total_vendido: int = sum(p["total_comprado"] for p in productos)
    precio_total: float = sum(p["total_comprado"] * p["precio_unitario"] for p in productos)

    # Configurar el entorno de Jinja2 y renderizar el template
    env: Environment = Environment(loader=FileSystemLoader("app/pdf/templates"))
    template = env.get_template("report.html")
    html_out: str = template.render(
        productos=productos,
        total_vendido=total_vendido,
        precio_total=precio_total,
        fecha=datetime.now().strftime("%d/%m/%Y %H:%M %p")
    )

    # Generar el archivo PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdfkit.from_string(html_out, tmp_file.name, configuration=config)
        return tmp_file.name