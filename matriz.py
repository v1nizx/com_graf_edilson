"""
Módulo com 5 exemplos diferentes de operações com matrizes usando NumPy
Demonstra diferentes dimensões e operações matemáticas
"""

import numpy as np
import sys

def exemplo_1_matriz_2d_basica():
    """
    Exemplo 1: Matriz 2D básica - Operações fundamentais
    """
    print("=== EXEMPLO 1: MATRIZ 2D BÁSICA ===")
    
    # Criando matrizes 2D
    matriz_a = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])
    
    matriz_b = np.array([[9, 8, 7],
                         [6, 5, 4],
                         [3, 2, 1]])
    
    print("Matriz A (3x3):")
    print(matriz_a)
    print(f"Dimensões: {matriz_a.shape}")
    print()
    
    print("Matriz B (3x3):")
    print(matriz_b)
    print(f"Dimensões: {matriz_b.shape}")
    print()
    
    # Operações básicas
    soma = matriz_a + matriz_b
    print("Soma (A + B):")
    print(soma)
    print()
    
    subtracao = matriz_a - matriz_b
    print("Subtração (A - B):")
    print(subtracao)
    print()
    
    multiplicacao_elemento = matriz_a * matriz_b
    print("Multiplicação elemento por elemento (A * B):")
    print(multiplicacao_elemento)
    print()
    
    multiplicacao_matricial = np.dot(matriz_a, matriz_b)
    print("Multiplicação matricial (A @ B):")
    print(multiplicacao_matricial)
    print()
    
    print("-" * 50)

def exemplo_2_matriz_3d():
    """
    Exemplo 2: Matriz 3D - Tensor para processamento de imagens
    """
    print("=== EXEMPLO 2: MATRIZ 3D (TENSOR) ===")
    
    # Simulando uma imagem RGB pequena (4x4x3)
    # Dimensões: altura x largura x canais_cor
    imagem_rgb = np.random.randint(0, 256, size=(4, 4, 3), dtype=np.uint8)
    
    print("Tensor 3D simulando imagem RGB (4x4x3):")
    print(f"Dimensões: {imagem_rgb.shape}")
    print("Canal Vermelho (R):")
    print(imagem_rgb[:,:,0])
    print()
    print("Canal Verde (G):")
    print(imagem_rgb[:,:,1])
    print()
    print("Canal Azul (B):")
    print(imagem_rgb[:,:,2])
    print()
    
    # Operações com o tensor
    media_por_canal = np.mean(imagem_rgb, axis=(0,1))
    print("Média de intensidade por canal (R, G, B):")
    print(media_por_canal)
    print()
    
    # Converter para escala de cinza
    cinza = np.mean(imagem_rgb, axis=2)
    print("Imagem convertida para escala de cinza:")
    print(cinza.astype(np.uint8))
    print()
    
    # Estatísticas
    print(f"Valor mínimo no tensor: {np.min(imagem_rgb)}")
    print(f"Valor máximo no tensor: {np.max(imagem_rgb)}")
    print(f"Média geral: {np.mean(imagem_rgb):.2f}")
    print()
    
    print("-" * 50)

def exemplo_3_operacoes_lineares():
    """
    Exemplo 3: Operações de álgebra linear avançadas
    """
    print("=== EXEMPLO 3: ÁLGEBRA LINEAR AVANÇADA ===")
    
    # Matriz para operações lineares
    matriz = np.array([[4, 2, 1],
                       [2, 3, 1],
                       [1, 1, 2]], dtype=float)
    
    print("Matriz original (3x3):")
    print(matriz)
    print()
    
    # Determinante
    determinante = np.linalg.det(matriz)
    print(f"Determinante: {determinante:.4f}")
    print()
    
    # Inversa
    try:
        inversa = np.linalg.inv(matriz)
        print("Matriz inversa:")
        print(inversa)
        print()
        
        # Verificar se A * A^(-1) = I
        identidade = np.dot(matriz, inversa)
        print("Verificação (A * A^(-1) ≈ I):")
        print(np.round(identidade, 4))
        print()
    except np.linalg.LinAlgError:
        print("Matriz não é invertível (singular)")
    
    # Autovalores e autovetores
    autovalores, autovetores = np.linalg.eig(matriz)
    print("Autovalores:")
    print(autovalores)
    print()
    print("Autovetores:")
    print(autovetores)
    print()
    
    # Posto da matriz
    posto = np.linalg.matrix_rank(matriz)
    print(f"Posto da matriz: {posto}")
    print()
    
    print("-" * 50)

def exemplo_4_estatisticas_dados():
    """
    Exemplo 4: Análise estatística com arrays multidimensionais
    """
    print("=== EXEMPLO 4: ANÁLISE ESTATÍSTICA ===")
    
    # Simulando dados de vendas (12 meses x 5 produtos)
    np.random.seed(42)  # Para resultados reproduzíveis
    vendas = np.random.normal(1000, 200, size=(12, 5))  # média=1000, desvio=200
    vendas = np.maximum(vendas, 0)  # Garantir valores não negativos
    
    print("Dados de vendas (12 meses x 5 produtos):")
    print(f"Dimensões: {vendas.shape}")
    print("Primeiras 6 linhas:")
    print(np.round(vendas[:6], 2))
    print()
    
    # Estatísticas por produto (ao longo dos meses)
    print("=== ESTATÍSTICAS POR PRODUTO ===")
    for i in range(5):
        produto = vendas[:, i]
        print(f"Produto {i+1}:")
        print(f"  Média: {np.mean(produto):.2f}")
        print(f"  Mediana: {np.median(produto):.2f}")
        print(f"  Desvio padrão: {np.std(produto):.2f}")
        print(f"  Min: {np.min(produto):.2f}")
        print(f"  Max: {np.max(produto):.2f}")
        print()
    
    # Estatísticas por mês (ao longo dos produtos)
    vendas_mensais = np.sum(vendas, axis=1)
    print("=== VENDAS TOTAIS MENSAIS ===")
    print("Total por mês:", np.round(vendas_mensais, 2))
    print(f"Melhor mês: {np.argmax(vendas_mensais) + 1} (Vendas: {np.max(vendas_mensais):.2f})")
    print(f"Pior mês: {np.argmin(vendas_mensais) + 1} (Vendas: {np.min(vendas_mensais):.2f})")
    print()
    
    # Correlação entre produtos
    correlacao = np.corrcoef(vendas.T)
    print("Matriz de correlação entre produtos:")
    print(np.round(correlacao, 3))
    print()
    
    print("-" * 50)

def exemplo_5_transformacoes_geometricas():
    """
    Exemplo 5: Transformações geométricas 2D usando matrizes
    """
    print("=== EXEMPLO 5: TRANSFORMAÇÕES GEOMÉTRICAS 2D ===")
    
    # Pontos originais (vértices de um triângulo)
    pontos_originais = np.array([[0, 1, 0.5],    # coordenadas x
                                 [0, 0, 1],      # coordenadas y
                                 [1, 1, 1]])     # coordenadas homogêneas
    
    print("Pontos originais do triângulo:")
    print("Ponto A: (0, 0)")
    print("Ponto B: (1, 0)")  
    print("Ponto C: (0.5, 1)")
    print("Matriz de pontos (coordenadas homogêneas):")
    print(pontos_originais)
    print()
    
    # 1. Translação
    translacao = np.array([[1, 0, 2],    # mover 2 unidades em x
                           [0, 1, 1],    # mover 1 unidade em y
                           [0, 0, 1]])   # coordenada homogênea
    
    pontos_transladados = np.dot(translacao, pontos_originais)
    print("=== TRANSLAÇÃO ===")
    print("Matriz de translação:")
    print(translacao)
    print("Pontos após translação:")
    for i in range(3):
        print(f"Ponto {chr(65+i)}: ({pontos_transladados[0,i]:.1f}, {pontos_transladados[1,i]:.1f})")
    print()
    
    # 2. Rotação (45 graus)
    angulo = np.pi / 4  # 45 graus em radianos
    cos_a, sin_a = np.cos(angulo), np.sin(angulo)
    
    rotacao = np.array([[cos_a, -sin_a, 0],
                        [sin_a,  cos_a, 0],
                        [0,      0,     1]])
    
    pontos_rotacionados = np.dot(rotacao, pontos_originais)
    print("=== ROTAÇÃO (45°) ===")
    print("Matriz de rotação:")
    print(np.round(rotacao, 3))
    print("Pontos após rotação:")
    for i in range(3):
        print(f"Ponto {chr(65+i)}: ({pontos_rotacionados[0,i]:.3f}, {pontos_rotacionados[1,i]:.3f})")
    print()
    
    # 3. Escala
    escala = np.array([[2, 0, 0],    # escalar 2x em x
                       [0, 1.5, 0],  # escalar 1.5x em y
                       [0, 0, 1]])
    
    pontos_escalados = np.dot(escala, pontos_originais)
    print("=== ESCALA ===")
    print("Matriz de escala:")
    print(escala)
    print("Pontos após escala:")
    for i in range(3):
        print(f"Ponto {chr(65+i)}: ({pontos_escalados[0,i]:.1f}, {pontos_escalados[1,i]:.1f})")
    print()
    
    # 4. Transformação composta
    transformacao_composta = np.dot(translacao, np.dot(rotacao, escala))
    pontos_final = np.dot(transformacao_composta, pontos_originais)
    
    print("=== TRANSFORMAÇÃO COMPOSTA (Escala → Rotação → Translação) ===")
    print("Matriz de transformação composta:")
    print(np.round(transformacao_composta, 3))
    print("Pontos finais:")
    for i in range(3):
        print(f"Ponto {chr(65+i)}: ({pontos_final[0,i]:.3f}, {pontos_final[1,i]:.3f})")
    print()
    
    print("-" * 50)

def demonstracao_completa():
    """Executa todos os 5 exemplos de matrizes NumPy"""
    print("=" * 60)
    print("DEMONSTRAÇÃO COMPLETA - NUMPY MATRIZES")
    print("5 Exemplos com Diferentes Dimensões e Operações")
    print("=" * 60)
    print()
    
    try:
        exemplo_1_matriz_2d_basica()
        exemplo_2_matriz_3d()
        exemplo_3_operacoes_lineares()
        exemplo_4_estatisticas_dados()
        exemplo_5_transformacoes_geometricas()
        
        print("=" * 60)
        print("DEMONSTRAÇÃO NUMPY CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        
    except Exception as e:
        print(f"ERRO durante execução: {e}")
        print(f"Tipo do erro: {type(e).__name__}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    demonstracao_completa()