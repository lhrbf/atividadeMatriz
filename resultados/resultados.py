from buscas.busca_largura import busca_largura
from buscas.busca_profundidade import busca_profundidade
from buscas.busca_gulosa import busca_gulosa
from buscas.busca_a import busca_a

def salvar_resultados():
    # Definição do labirinto
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    inicio = (0, 0)
    objetivo = (4, 4)

    # Executando as buscas
    bfs_resultado = busca_largura(maze, inicio, objetivo)
    dfs_resultado = busca_profundidade(maze, inicio, objetivo)
    gulosa_resultado = busca_gulosa(maze, inicio, objetivo)
    a_estrela_resultado = busca_a(maze, inicio, objetivo)

    # Salvando os resultados em 'resultados.txt'
    with open('resultados/resultados.txt', 'w') as f:
        f.write("Busca em Largura (BFS):\n")
        f.write(f"{bfs_resultado}\n\n")
        f.write("Busca em Profundidade (DFS):\n")
        f.write(f"{dfs_resultado}\n\n")
        f.write("Busca Gulosa:\n")
        f.write(f"{gulosa_resultado}\n\n")
        f.write("Busca A*:\n")
        f.write(f"{a_estrela_resultado}\n")

if __name__ == "__main__":
    salvar_resultados()