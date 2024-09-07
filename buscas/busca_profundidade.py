def busca_profundidade(labirinto, inicio, objetivo):
    pilha = [inicio]
    visitados = set([inicio])
    pai = {inicio: None}
    
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimentos: cima, baixo, esquerda, direita

    while pilha:
        atual = pilha.pop()

        if atual == objetivo:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = pai[atual]
            return caminho[::-1]  # Caminho do início ao objetivo

        for direcao in direcoes:
            prox_celula = (atual[0] + direcao[0], atual[1] + direcao[1])
            if 0 <= prox_celula[0] < len(labirinto) and 0 <= prox_celula[1] < len(labirinto[0]) and labirinto[prox_celula[0]][prox_celula[1]] == 0 and prox_celula not in visitados:
                pilha.append(prox_celula)
                visitados.add(prox_celula)
                pai[prox_celula] = atual

    return None  # Sem caminho
