import cairo

# Matriz para as retas verticais: [x, y1, y2, espessura]
matriz_verticais = [
    [50, 40, 260, 6],
    [150, 20, 280, 2],
    [250, 80, 220, 10]
]

# Configuração da imagem
largura, altura = 300, 300
superficie = cairo.ImageSurface(cairo.FORMAT_ARGB32, largura, altura)
contexto = cairo.Context(superficie)

# Fundo branco
contexto.set_source_rgb(1, 1, 1)
contexto.paint()

# Define a cor das retas (azul)
contexto.set_source_rgb(0.1, 0.4, 0.8)

# Desenha as retas com base nos dados da matriz
for reta in matriz_verticais:
    x, y1, y2, espessura = reta
    contexto.set_line_width(espessura)
    contexto.move_to(x, y1)
    contexto.line_to(x, y2)
    contexto.stroke()

# Salva o resultado
superficie.write_to_png("1_retas_verticais.png")
print("Imagem '1_retas_verticais.png' foi criada.")