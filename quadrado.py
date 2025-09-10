import cairo

# Matriz para os quadrados: [x, y, lado, (r, g, b)]
matriz_quadrados = [
    [50, 50, 200, (0.9, 0.9, 0.2)],   # Amarelo
    [75, 75, 150, (0.9, 0.5, 0.2)],   # Laranja
    [100, 100, 100, (0.8, 0.2, 0.2)]  # Vermelho
]

# Configuração da imagem
largura, altura = 300, 300
superficie = cairo.ImageSurface(cairo.FORMAT_ARGB32, largura, altura)
contexto = cairo.Context(superficie)

# Fundo branco
contexto.set_source_rgb(1, 1, 1)
contexto.paint()

# Desenha e preenche os quadrados com base nos dados da matriz
for quadrado in matriz_quadrados:
    x, y, lado, cor = quadrado
    r, g, b = cor
    contexto.set_source_rgb(r, g, b)
    contexto.rectangle(x, y, lado, lado)
    contexto.fill()

# Salva o resultado
superficie.write_to_png("5_quadrados.png")
print("Imagem '5_quadrados.png' foi criada.")