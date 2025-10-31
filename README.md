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

## 🎯 Desafio Proposto e Objetivos

### Objetivo Geral
Criar um **modelo inteligente de roteamento** que, a partir de um conjunto de pedidos, indique as **rotas ideais** a serem seguidas pelos entregadores, reduzindo tempo de entrega e custos operacionais.

### Objetivos Específicos
- Representar a cidade como um **grafo** (nós = pontos, arestas = ruas);
- Calcular o **menor caminho** entre locais usando **Dijkstra e A***;
- Resolver o **problema do caixeiro viajante (TSP)** para múltiplas entregas;
- Distribuir entregas entre múltiplos entregadores;
- Exibir **tempo estimado de entrega em minutos e horas**;
- (Opcional) Incorporar dados reais de trânsito ou velocidade média por via.

---

## 🧠 Abordagem Adotada

A cidade foi modelada como um **grafo direcionado e ponderado**:

- **Nodos (vértices):** representam os bairros, pontos de coleta e entrega.  
- **Arestas:** representam as ruas ou conexões entre os pontos.  
- **Pesos:** representam o tempo de deslocamento (em segundos), obtido via estimativas do `osmnx`.

A partir desse grafo, o sistema aplica algoritmos de **busca e otimização** para encontrar as melhores rotas.

### Passos do Modelo:
1. Criação do grafo da cidade usando `osmnx` (dados reais do OpenStreetMap);
2. Cálculo de tempo estimado de deslocamento para cada aresta (`travel_time`);
3. Aplicação de **Dijkstra** para obter o menor caminho entre dois pontos;
4. Aplicação de **TSP (Travelling Salesman Problem)** para otimizar múltiplas entregas;
5. Distribuição automática de pedidos entre vários entregadores;
6. Exibição das rotas e tempo total em **minutos e horas**.

---

## ⚙️ Algoritmos Utilizados

| Algoritmo | Função | Justificativa |
|------------|--------|----------------|
| **Dijkstra** | Encontrar o menor caminho entre dois pontos | Ideal para grafos ponderados com pesos positivos (tempo/distância). |
| **TSP (Travelling Salesman Problem)** | Encontrar a melhor sequência de visitas para múltiplos destinos | Minimiza o tempo total de entrega para um entregador. |
| **Heurística de Distribuição** | Dividir entregas entre entregadores | Distribuição equitativa de pedidos baseada na quantidade. |
| **A\*** (possível expansão futura) | Busca heurística com custo estimado | Mais eficiente que Dijkstra quando há estimativas de distância. |

---

## 🧩 Diagrama do Grafo (Modelo Conceitual)

O grafo pode ser visualizado como abaixo:

```text
      (Loja)
       /  \
  5min/    \10min
     /      \
(Entrega1)  (Entrega2)
     \        /
      \7min  /6min
       (Entrega3)
