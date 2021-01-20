from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from pdf2image import convert_from_path, convert_from_bytes

drawing = svg2rlg("originalCountyMap.svg")
renderPDF.drawToFile(drawing, "file.pdf")
renderPM.drawToFile(drawing, "file2.png", fmt="PNG")

#images = convert_from_path('file.pdf')
