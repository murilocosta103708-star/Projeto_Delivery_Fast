import osmnx as ox
import networkx as nx
import itertools
import matplotlib.pyplot as plt  # <-- IMPORT ADICIONADO

# ============================
# 1. Criar grafo da cidade real
# ============================
cidade = "São Paulo, Brazil"  # Altere para sua cidade
G = ox.graph_from_place(cidade, network_type='drive')
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)

# ============================
# 2. Definir pontos de entrega
# ============================
entregas = {
    "Loja": (-23.5505, -46.6333),
    "Entrega1": (-23.5590, -46.6396),
    "Entrega2": (-23.5435, -46.6253),
    "Entrega3": (-23.5470, -46.6350)
}

nodos_entrega = {}
for nome, coord in entregas.items():
    nodo = ox.distance.nearest_nodes(G, X=coord[1], Y=coord[0])
    nodos_entrega[nome] = nodo

# ============================
# 3. Função para menor caminho entre dois pontos
# ============================
def menor_caminho(origem, destino):
    caminho = nx.shortest_path(G, origem, destino, weight='travel_time')
    tempo_segundos = nx.shortest_path_length(G, origem, destino, weight='travel_time')
    tempo_minutos = tempo_segundos / 60
    return caminho, tempo_minutos

# ============================
# 4. Função para otimizar rota (TSP simples)
# ============================
def otimizar_rota(nodos):
    pontos = list(nodos.values())
    origem = pontos[0]  # Assume que o primeiro item em 'nodos' é a origem
    melhor_rota = None
    menor_tempo = float('inf')

    # Itera sobre todas as permutações dos pontos de entrega (exceto a origem)
    for perm in itertools.permutations(pontos[1:]):
        rota = [origem] + list(perm)
        tempo_total = 0
        for i in range(len(rota) - 1):
            _, tempo = menor_caminho(rota[i], rota[i + 1])
            tempo_total += tempo
        
        # Verifica se esta rota é a mais rápida encontrada
        if tempo_total < menor_tempo:
            menor_tempo = tempo_total
            melhor_rota = rota

    return melhor_rota, menor_tempo

# ============================
# 5. Executar otimização
# ============================
rota_otima, tempo_total_min = otimizar_rota(nodos_entrega)
tempo_total_horas = tempo_total_min / 60

print("\n🗺️  Rota otimizada:")
for i in range(len(rota_otima) - 1):
    origem = rota_otima[i]
    destino = rota_otima[i + 1]
    _, tempo_min = menor_caminho(origem, destino)
    print(f"Trecho {i+1}: {origem} → {destino} | {tempo_min:.1f} minutos")

print(f"\n⏱️  Tempo total estimado: {tempo_total_min:.1f} minutos ({tempo_total_horas:.2f} horas)")

# ===============================================
# 6. Visualizar a Rota Otimizada (NOVA SEÇÃO)
# ===============================================
print("\nVisualizando o mapa da rota...")

# Coletar todos os trechos (listas de nós) da rota otimizada
lista_de_caminhos = []
for i in range(len(rota_otima) - 1):
    origem = rota_otima[i]
    destino = rota_otima[i + 1]
    # Usar a função menor_caminho para obter o caminho (lista de nodos)
    caminho, _ = menor_caminho(origem, destino)
    lista_de_caminhos.append(caminho)

# Obter o nó da loja
nodo_loja = nodos_entrega["Loja"]
# Obter os nós das entregas (sem a loja)
nodos_paradas = [nodo for nome, nodo in nodos_entrega.items() if nome != "Loja"]

# Plotar o grafo e as rotas
# A função plot_graph_routes desenha o grafo base E as rotas por cima
fig, ax = ox.plot_graph_routes(
    G,
    lista_de_caminhos,
    route_colors='blue',   # Cor da rota
    route_linewidths=2,
    route_alpha=0.8,
    orig_dest_size=0,    # Não mostrar O/D de cada trecho individual
    ax=None,
    node_size=0,         # Não desenhar os nós do grafo base
    edge_linewidth=0.3,
    edge_color='#999999', # Cor das ruas do grafo base
    bgcolor='w',
    show=False,          # Não mostrar a figura ainda
    close=False          # Não fechar a figura
)

# Obter as coordenadas X, Y dos nós para plotar os marcadores
# Coordenadas da Loja
x_loja = G.nodes[nodo_loja]['x']
y_loja = G.nodes[nodo_loja]['y']

# Coordenadas das Paradas
x_paradas = [G.nodes[nodo]['x'] for nodo in nodos_paradas]
y_paradas = [G.nodes[nodo]['y'] for nodo in nodos_paradas]

# Plotar os pontos no mapa (sobre o eixo 'ax' retornado pelo osmnx)
ax.scatter(x_loja, y_loja, c='green', s=100, label='Loja', zorder=5)
ax.scatter(x_paradas, y_paradas, c='red', s=100, label='Entregas', zorder=5)

# Adicionar legenda e título
ax.legend(loc='best')
ax.set_title(f"Rota Otimizada - Tempo Total: {tempo_total_min:.1f} min", fontsize=15)

# Mostrar o mapa
plt.show()

# ====================================================
# 7. Distribuir entregas entre entregadores (SEÇÃO RENOMEADA)
# ====================================================
def distribuir_entregas(nodos, entregadores=2):
    lista_entregas = list(nodos.values())[1:]
    distribuicao = {f"Entregador{i+1}": [] for i in range(entregadores)}
    for i, entrega in enumerate(lista_entregas):
        entregador = f"Entregador{(i % entregadores) + 1}"
        distribuicao[entregador].append(entrega)
    return distribuicao

distribuicao = distribuir_entregas(nodos_entrega, entregadores=2)
print("\n🚴 Distribuição entre entregadores:")
for entregador, rotas in distribuicao.items():
    print(f"  {entregador}: {len(rotas)} entregas")
