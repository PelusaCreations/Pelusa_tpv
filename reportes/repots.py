from geraldo import Report, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

class ReporteCategoria(Report):
    title = 'Existencia por cagoria'
    author = 'Pelusa TPV'

    page_size = landscape(A4)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm