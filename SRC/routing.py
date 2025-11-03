import itertools
import networkx as nx

def menor_caminho(G, origem, destino):
    caminho = nx.shortest_path(G, origem, destino, weight='travel_time')
    tempo_segundos = nx.shortest_path_length(G, origem, destino, weight='travel_time')
    tempo_minutos = tempo_segundos / 60
    return caminho, tempo_minutos

def otimizar_rota(G, nodos):
    pontos = list(nodos.values())
    origem = pontos[0]
    melhor_rota = None
    menor_tempo = float('inf')

    for perm in itertools.permutations(pontos[1:]):
        rota = [origem] + list(perm)
        tempo_total = 0
        for i in range(len(rota) - 1):
            _, tempo = menor_caminho(G, rota[i], rota[i + 1])
            tempo_total += tempo
        if tempo_total < menor_tempo:
            menor_tempo = tempo_total
            melhor_rota = rota

    return melhor_rota, menor_tempo

def distribuir_entregas(nodos, entregadores=2):
    lista_entregas = list(nodos.values())[1:]
    distribuicao = {f"Entregador{i+1}": [] for i in range(entregadores)}
    for i, entrega in enumerate(lista_entregas):
        entregador = f"Entregador{(i % entregadores) + 1}"
        distribuicao[entregador].append(entrega)
    return distribuicao
