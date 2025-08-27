# Implementação do Algoritmo de Karatsuba em Python

**Trabalho Individual 1 da disciplina de Fundamentos de Projetos e Análise de Algoritmos.**

## Objetivo

Desenvolver um programa em Python que implemente o algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros.

## O que é o Algoritmo de Karatsuba?

O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de números inteiros grandes, introduzida por Anatolii Karatsuba em 1960. Ele melhora a complexidade da multiplicação em comparação ao método tradicional de multiplicação direta.

## Explicação do Algoritmo

### Implementação Algoritmo de Karatsuba

```python
def karatsuba(num_x, num_y):

    if num_x < 10 or num_y < 10:
        return num_x * num_y

    s = max(len(str(num_x)), len(str(num_y)))
    m = s // 2

    alta_x, baixa_x = divmod(num_x, 10 ** m)
    alta_y, baixa_y = divmod(num_y, 10 ** m)

    z0 = karatsuba(baixa_x, baixa_y)
    z1 = karatsuba((baixa_x + alta_x), (baixa_y + alta_y))
    z2 = karatsuba(alta_x, alta_y)

    return (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0

if __name__ == "__main__":

    num_x = int(input("Digite o primeiro número: "))
    num_y = int(input("Digite o segundo número: "))

    resultado = karatsuba(num_x, num_y)

    print(f"O produto de {num_x} e {num_y} é:")
    print(resultado)

    print("\nVerificação com a multiplicação padrão do Python:")
    print(num_x * num_y)

    assert resultado == num_x * num_y
    print("\n✅ Resultado verificado com sucesso!")
```

### Algoritmo com explicações

```python

def karatsuba(num_x, num_y):
    """
    Multiplicação de dois números inteiros usando o algoritmo de Karatsuba.
    """
    """
    Caso base para o metodo recursivo
    É aplicado o metodo até que os números fiquem pequenos o suficiente para usar a multiplicação normal.
    """
    if num_x < 10 or num_y < 10:
        return num_x * num_y
    """
    Descobre o tamanho dos números para dividí-los em duas metades
    A parte "Alta(dígitos mais significativos) e "Baixa" (dígitos menos significativos)"
    """
    s = max(len(str(num_x)), len(str(num_y)))
    m = s // 2
    """
    Divide os números nas duas metades
    """
    alta_x, baixa_x = divmod(num_x, 10 ** m)
    alta_y, baixa_y = divmod(num_y, 10 ** m)
    """
    Utiliza a recursividade para o cálculo de z0, z1 e z2
    Para dividir o "problema grande em subproblemas menores" 
    Como acontece em dividir e conquistar.
    """
    z0 = karatsuba(baixa_x, baixa_y)
    z1 = karatsuba((baixa_x + alta_x), (baixa_y + alta_y))
    z2 = karatsuba(alta_x, alta_y)

    """
    Aplica a formula final do Algoritmo de Karatsuba usando os resultados de z0, z1 e z2
    """
    return (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0


if __name__ == "__main__":

    num_x = int(input("Digite o primeiro número: "))
    num_y = int(input("Digite o segundo número: "))

    #Utiliza o metodo de Karatsuba
    resultado = karatsuba(num_x, num_y)

    print("\nUtilizando o algoritmo de Karatsuba")
    print(f"O produto de {num_x} e {num_y} é:")
    print(resultado)

    # Verificação com o metodo padrão
    print("\nVerificação com a multiplicação padrão do Python:")
    print(num_x * num_y)

    # Verifica se os resultados são iguais
    assert resultado == num_x * num_y
    print("\n✅ Resultado verificado com sucesso!")
```

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
4. Digite os dois números para realizar a multiplicação através do Algoritmo de Karatsuba


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

