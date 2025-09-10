import cairo
import math

# Matriz para os círculos: [cx, cy, raio, espessura]
matriz_circulos = [
    [150, 150, 120, 8],
    [150, 150, 80, 4],
    [150, 150, 40, 2]
]

# Configuração da imagem
largura, altura = 300, 300
superficie = cairo.ImageSurface(cairo.FORMAT_ARGB32, largura, altura)
contexto = cairo.Context(superficie)

# Fundo branco
contexto.set_source_rgb(1, 1, 1)
contexto.paint()

# Define a cor dos círculos (roxo)
contexto.set_source_rgb(0.6, 0.2, 0.8)

# Desenha os círculos com base nos dados da matriz
for circulo in matriz_circulos:
    cx, cy, raio, espessura = circulo
    contexto.set_line_width(espessura)
    contexto.arc(cx, cy, raio, 0, 2 * math.pi)
    contexto.stroke()

# Salva o resultado
superficie.write_to_png("4_circulos.png")
print("Imagem '4_circulos.png' foi criada.")