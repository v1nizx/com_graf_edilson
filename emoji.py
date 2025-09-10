import cairo
import gi
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo

# Matriz para os emojis: [x, y, texto_emoji, tamanho_fonte]
matriz_emojis = [
    [50, 50, "😊", 48],
    [150, 80, "🚀", 60],
    [80, 180, "💡", 40],
    [200, 200, "💖", 55],
    [30, 250, "✨", 35]
]

# Configuração da imagem
largura, altura = 300, 300
superficie = cairo.ImageSurface(cairo.FORMAT_ARGB32, largura, altura)
contexto = cairo.Context(superficie)

# Fundo branco
contexto.set_source_rgb(1, 1, 1)
contexto.paint()

# Cor padrão para o texto (se o emoji não for colorido por si só,
# ou para sombreamento/contorno, se aplicado)
contexto.set_source_rgb(0, 0, 0) # Preto

# Cria o layout do Pango
layout = PangoCairo.create_layout(contexto)

# Itera sobre a matriz para desenhar cada emoji
for emoji_info in matriz_emojis:
    x, y, emoji_char, tamanho_fonte = emoji_info

    # Define o texto e a fonte para o layout
    layout.set_text(emoji_char, -1) # -1 para Pango calcular o comprimento
    
    # É crucial usar uma fonte que suporte emojis coloridos.
    # Noto Color Emoji é uma boa escolha, se estiver instalada no sistema.
    # Fallback para "sans" ou "serif" se não for encontrada.
    fd = Pango.FontDescription(f"Noto Color Emoji {tamanho_fonte}")
    layout.set_font_description(fd)

    # Move o contexto para a posição do emoji
    contexto.move_to(x, y)

    # Renderiza o texto (emoji)
    PangoCairo.show_layout(contexto, layout)

# Salva o resultado
superficie.write_to_png("6_emojis.png")
print("Imagem '6_emojis.png' com emojis foi criada.")