import cairo

# Matriz para as retas horizontais: [x1, x2, y, espessura]
matriz_horizontais = [
    [40, 260, 50, 6],
    [20, 280, 150, 2],
    [80, 220, 250, 10]
]

# Configuração da imagem
largura, altura = 300, 300
superficie = cairo.ImageSurface(cairo.FORMAT_ARGB32, largura, altura)
contexto = cairo.Context(superficie)

# Fundo branco
contexto.set_source_rgb(1, 1, 1)
contexto.paint()

# Define a cor das retas (vermelho)
contexto.set_source_rgb(0.9, 0.2, 0.2)

# Desenha as retas com base nos dados da matriz
for reta in matriz_horizontais:
    x1, x2, y, espessura = reta
    contexto.set_line_width(espessura)
    contexto.move_to(x1, y)
    contexto.line_to(x2, y)
    contexto.stroke()

# Salva o resultado
superficie.write_to_png("2_retas_horizontais.png")
print("Imagem '2_retas_horizontais.png' foi criada.")