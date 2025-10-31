# Projeto_Delivery_Fast
Feito para aumentar a qualidade e diminuir o tempo de entrega trazendo melhor satisfação para o cliente 
# 🚚 Sistema Inteligente de Roteamento para Delivery

## 📖 Descrição do Problema

Empresas de delivery enfrentam desafios logísticos ao tentar **definir rotas eficientes** para seus entregadores.  
Com múltiplos pedidos, condições de trânsito variáveis e restrições urbanas, encontrar o **menor caminho entre vários pontos de entrega** se torna um problema complexo.

O objetivo deste projeto é desenvolver uma **solução baseada em Inteligência Artificial e Teoria dos Grafos** capaz de:
- Sugerir as **melhores rotas** para entregadores;
- Considerar **distâncias reais** e **tempos estimados**;
- Otimizar entregas de **múltiplos pedidos e múltiplos entregadores**;
- Adaptar-se a **condições urbanas dinâmicas**, como trânsito e obras.

---

## 🎯 Objetivos

### Objetivo Geral
Criar um **modelo inteligente de roteamento** que, a partir de um conjunto de pedidos, indique as **rotas ideais** a serem seguidas pelos entregadores, reduzindo tempo de entrega e custos operacionais.

### Objetivos Específicos
- Representar a cidade como um **grafo** (nós = pontos, arestas = ruas);
- Calcular o **menor caminho** entre locais usando **Dijkstra**;
- Resolver o **problema do caixeiro viajante (TSP)** para múltiplas entregas;
- Distribuir entregas entre múltiplos entregadores;
- Exibir **tempo estimado de entrega em minutos e horas**.

---

## 🧠 Abordagem Adotada

A cidade foi modelada como um **grafo ponderado**:

- **Nodos (vértices):** bairros, pontos de coleta e entrega.  
- **Arestas:** ruas ou conexões entre pontos.  
- **Pesos:** tempo de deslocamento em segundos, convertido em minutos.

O modelo aplica algoritmos de **busca e otimização** para calcular rotas eficientes.

### Fluxo do Modelo:
1. Criar grafo da cidade usando `osmnx` (dados do OpenStreetMap).  
2. Calcular tempo de deslocamento de cada aresta (`travel_time`).  
3. Aplicar **Dijkstra** para o menor caminho entre dois pontos.  
4. Resolver **TSP** para múltiplas entregas.  
5. Distribuir pedidos entre múltiplos entregadores.  
6. Exibir rotas e tempo total em **minutos e horas**.  
7. Gerar imagem do grafo (`outputs/grafo.png`).

---

## ⚙️ Algoritmos Utilizados

| Algoritmo | Função | Justificativa |
|------------|--------|----------------|
| **Dijkstra** | Menor caminho entre dois pontos | Ideal para grafos ponderados com pesos positivos. |
| **TSP (Travelling Salesman Problem)** | Melhor sequência de visitas | Minimiza o tempo total de entrega para cada entregador. |
| **Heurística de Distribuição** | Dividir entregas entre entregadores | Distribuição equitativa de pedidos baseada na quantidade. |

---

## 🧩 Diagrama do Grafo

Exemplo conceitual do grafo:

```text
      (Loja)
       /  \
  5min/    \10min
     /      \
(Entrega1)  (Entrega2)
     \        /
      \7min  /6min
       (Entrega3)

