import os
import pandas as pd
import osmnx as ox
from PIL import Image, ImageDraw

def salvar_grafo(G, path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    ox.save_graph_geopackage(G, filepath=path)

def carregar_entregas(path):
    df = pd.read_csv(path)
    entregas = {row['nome']: (row['lat'], row['lon']) for _, row in df.iterrows()}
    return entregas

def salvar_resultados(G, rota, tempo_total_min):
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    # Criar imagem fictícia da rota
    img = Image.new('RGB', (400, 400), color='white')
    d = ImageDraw.Draw(img)
    d.line([(50,50),(350,50),(350,350),(50,350),(50,50)], fill='blue', width=5)
    img.save('outputs/rota_otimizada.png')
    with open('outputs/resumo_rota.txt', 'w') as f:
        f.write(f'Tempo total: {tempo_total_min:.1f} minutos\n')
        f.write('Rota ótima (fictícia)\n')
        for nodo in rota:
            f.write(str(nodo)+'\n')
