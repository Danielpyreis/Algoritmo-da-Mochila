# Algoritmo-da-Mochila

# 🧬 Algoritmo Genético para o Problema da Mochila

Este projeto implementa uma solução para o **Problema da Mochila** (Knapsack Problem) utilizando um **Algoritmo Genético (AG)**. O problema da mochila é um dos desafios clássicos da otimização combinatória, onde o objetivo é maximizar o valor de itens selecionados sem ultrapassar um limite de peso.

## 🧠 Sobre o Problema
O Problema da Mochila consiste em escolher um subconjunto de itens, cada um com um peso e valor, de modo que o valor total seja o máximo possível sem que o peso exceda uma capacidade pré-definida.

## ⚙️ Algoritmo Genético (AG)
Um **Algoritmo Genético** é uma técnica baseada nos princípios da seleção natural, que evolui uma população de soluções candidatas através de seleção, cruzamento e mutação. Abaixo está uma breve explicação do funcionamento do AG para resolver o problema:

### Representação dos Indivíduos
Cada indivíduo é representado como uma lista binária:
- **0**: O item não foi incluído na mochila.
- **1**: O item foi incluído.

### Função de Aptidão (Fitness)
A função de aptidão calcula o valor total dos itens incluídos na mochila. Se o peso exceder a capacidade, a aptidão da solução é penalizada ou considerada inválida.

### Seleção
A seleção é realizada utilizando o método da **Roleta**, onde indivíduos com maior aptidão têm mais chances de serem escolhidos para a próxima geração.

### Cruzamento (Crossover)
Dado um par de pais, ocorre o cruzamento, trocando genes a partir de um ponto de corte aleatório, gerando assim dois novos indivíduos.

### Mutação
Cada gene (item) tem uma pequena chance de ser alterado, garantindo diversidade na população e evitando que o algoritmo fique preso em soluções subótimas.

### Evolução
O processo de evolução é repetido ao longo de várias gerações, buscando melhorar as soluções até atingir uma solução satisfatória.

## 🖥️ Interface Gráfica
Este projeto inclui uma **interface gráfica** desenvolvida com **Tkinter**, onde o usuário pode:
- Adicionar itens com pesos e valores.
- Definir parâmetros como número de gerações e taxa de mutação.
- Visualizar os resultados da execução do algoritmo em tempo real.

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.x
- Biblioteca **Tkinter** para a interface gráfica.

### Instalação
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/seu-usuario/algoritmo-da-mochila.git
cd algoritmo-da-mochila
````
## 📚 Documentação Adicional
Este projeto conta com uma implementação detalhada de um **Algoritmo Genético** aplicado ao **Problema da Mochila**, e foi desenvolvido com o intuito de ser uma ferramenta educacional e prática. Abaixo estão algumas referências e explicações extras sobre o projeto:

- **Algoritmo Genético**: Explora conceitos de seleção natural, aptidão, cruzamento e mutação. Para uma visão mais aprofundada sobre algoritmos genéticos, veja [este guia sobre AG](https://en.wikipedia.org/wiki/Genetic_algorithm).
  
- **Tkinter**: A interface gráfica foi criada usando a biblioteca Tkinter, nativa do Python. Se você deseja entender melhor como o Tkinter funciona, consulte a [documentação oficial do Tkinter](https://docs.python.org/3/library/tkinter.html).

- **Problema da Mochila**: Este problema clássico de otimização combinatória é amplamente estudado. Para mais informações, confira a [descrição detalhada do Problema da Mochila](https://pt.wikipedia.org/wiki/Problema_da_mochila).

Se deseja explorar mais sobre a teoria por trás do projeto e os experimentos realizados, você pode acessar o [artigo completo](link-para-o-artigo), que oferece uma explicação detalhada sobre:
- A lógica utilizada no algoritmo genético.
- Comparações de performance entre diferentes abordagens.
- Experimentos e análises de resultados.
