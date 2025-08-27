# Implementação do Algoritmo de Karatsuba em Python

**Trabalho Individual 1 da disciplina de Fundamentos de Projetos e Análise de Algoritmos.**

## Objetivo

Desenvolver um programa em Python que implemente o algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros.

## O que é o Algoritmo de Karatsuba?

O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de números inteiros grandes, introduzida por Anatolii Karatsuba em 1960. Ele melhora a complexidade da multiplicação em comparação ao método tradicional de multiplicação direta.

## Explicação do Algoritmo

## Como executar o projeto

1. Clone o repositório:
```Bash
git clone https://github.com/gabrieltinoco/Algoritmo-De-Karatsuba-Em-Python.git
```
2. Navegue até o diretório do projeto:
```Bash
cd Algoritmo-De-Karatsuba-Em-Python
```
3. Execute o script Python:
```Bash
python main.py
```


## Relatório Técnico

### O que é a Complexidade Assintótica?

A **complexidade assintótica** é uma maneira de expressar o comportamento de um algoritmo quando o tamanho da entrada tende ao infinito. Ela descreve o tempo ou espaço de execução de um algoritmo em termos do tamanho da entrada, ignorando fatores como o hardware ou o tempo de execução real. A complexidade assintótica ajuda a comparar a eficiência de diferentes algoritmos de forma mais objetiva, independentemente das condições do sistema.

### O que é a Complexidade Ciclomática?

A **complexidade ciclomática** é uma métrica usada para medir a complexidade do fluxo de controle de um programa. Ela calcula o número de caminhos independentes no código, considerando estruturas como loops (`for`, `while`) e condicionais (`if`, `try/except`). Quanto maior o valor, mais complexo é o código.

**Fórmula:**  
\(
M = E - N + 2P
\)  

Onde:  
- \(M\): Complexidade Ciclomática  
- \(E\): Número de arestas (transições) no grafo do controle de fluxo  
- \(N\): Número de nós (blocos de código)  
- \(P\): Componentes conectados (geralmente 1 para programas simples)

