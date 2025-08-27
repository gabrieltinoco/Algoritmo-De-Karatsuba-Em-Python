# main.py

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