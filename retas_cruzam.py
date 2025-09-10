import cairo

# Matriz para retas variadas: [x1, y1, x2, y2]
matriz_cruzadas = [
    [50, 50, 250, 250],
    [250, 50, 50, 250],
    [150, 20, 150, 280],
    [20, 150, 280, 150]
]

# Configuração da imagem
largura, altura = 300, 300
superficie = cairo.ImageSurface(cairo.FORMAT_ARGB32, largura, altura)
contexto = cairo.Context(superficie)

# Fundo branco
contexto.set_source_rgb(1, 1, 1)
contexto.paint()

# Define a cor e espessura
contexto.set_source_rgb(0.2, 0.6, 0.3) # Verde
contexto.set_line_width(4)

# Desenha as retas com base nos dados da matriz
for reta in matriz_cruzadas:
    x1, y1, x2, y2 = reta
    contexto.move_to(x1, y1)
    contexto.line_to(x2, y2)
    contexto.stroke()

# Salva o resultado
superficie.write_to_png("3_retas_cruzadas.png")
print("Imagem '3_retas_cruzadas.png' foi criada.")