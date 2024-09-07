from collections import deque

def busca_largura(labirinto, inicio, objetivo):
    linhas, colunas = len(labirinto), len(labirinto[0])
    fila = deque([inicio])
    visitados = set([inicio])
    pai = {inicio: None}

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimentos: cima, baixo, esquerda, direita

    while fila:
        atual = fila.popleft()

        if atual == objetivo:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = pai[atual]
            return caminho[::-1]  # Caminho do início ao objetivo

        for direcao in direcoes:
            prox_celula = (atual[0] + direcao[0], atual[1] + direcao[1])
            if 0 <= prox_celula[0] < linhas and 0 <= prox_celula[1] < colunas and labirinto[prox_celula[0]][prox_celula[1]] == 0 and prox_celula not in visitados:
                fila.append(prox_celula)
                visitados.add(prox_celula)
                pai[prox_celula] = atual

    return None  # Sem caminho