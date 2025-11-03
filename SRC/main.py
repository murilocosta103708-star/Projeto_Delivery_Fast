import osmnx as ox
import networkx as nx
from src.routing import menor_caminho, otimizar_rota, distribuir_entregas
from src.utils import salvar_grafo, carregar_entregas, salvar_resultados

cidade = "São Paulo, Brazil"
G = ox.graph_from_place(cidade, network_type='drive')
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)
salvar_grafo(G, "data/grafo_sao_paulo.gpkg")

entregas = carregar_entregas("data/entregas.csv")

nodos_entrega = {}
for nome, coord in entregas.items():
    nodo = ox.distance.nearest_nodes(G, X=coord[1], Y=coord[0])
    nodos_entrega[nome] = nodo

rota_otima, tempo_total_min = otimizar_rota(G, nodos_entrega)
tempo_total_horas = tempo_total_min / 60

print("\n🗺️  Rota otimizada:")
for i in range(len(rota_otima) - 1):
    origem = rota_otima[i]
    destino = rota_otima[i + 1]
    _, tempo_min = menor_caminho(G, origem, destino)
    print(f"Trecho {i+1}: {origem} → {destino} | {tempo_min:.1f} minutos")

print(f"\n⏱️  Tempo total estimado: {tempo_total_min:.1f} minutos ({tempo_total_horas:.2f} horas)")

distribuicao = distribuir_entregas(nodos_entrega, entregadores=2)
print("\n🚴 Distribuição entre entregadores:")
for entregador, rotas in distribuicao.items():
    print(f'  {entregador}: {len(rotas)} entregas')

salvar_resultados(G, rota_otima, tempo_total_min)
