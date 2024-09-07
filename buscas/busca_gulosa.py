import heapq

def distancia_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def busca_gulosa(labirinto, inicio, objetivo):
    linhas, colunas = len(labirinto), len(labirinto[0])
    fila_prioridade = [(distancia_manhattan(inicio, objetivo), inicio)]
    visitados = set([inicio])
    pai = {inicio: None}

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimentos: cima, baixo, esquerda, direita

    while fila_prioridade:
        _, atual = heapq.heappop(fila_prioridade)

        if atual == objetivo:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = pai[atual]
            return caminho[::-1]  # Caminho do início ao objetivo

        for direcao in direcoes:
            prox_celula = (atual[0] + direcao[0], atual[1] + direcao[1])
            if 0 <= prox_celula[0] < linhas and 0 <= prox_celula[1] < colunas and labirinto[prox_celula[0]][prox_celula[1]] == 0 and prox_celula not in visitados:
                heapq.heappush(fila_prioridade, (distancia_manhattan(prox_celula, objetivo), prox_celula))
                visitados.add(prox_celula)
                pai[prox_celula] = atual

    return None  # Sem caminho
