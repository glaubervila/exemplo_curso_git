
def subtracao(a, b):
    """Retorna a subtração entre 2 valores inteiros
    Args:
        a (int): qualquer valor inteiro
        b (int): qualquer valor inteiro
    Returns:
        int: Resultado da subtração entre a e b
    """
    return int(a) - int(b)

  
def soma(a, b):
    """Retorna a soma entre 2 valores inteiros

    Args:
        a (int): qualquer valor inteiro
        b (int): qualquer valor inteiro

    Returns:
        int: Resultado da soma entre a e b
    """
    return int(a) + int(b)


def multiplica(a, b):
    """Retorna o resultado da multiplicação de dois números

    Args:
        a (int): número inteiro
        b (int): número inteiro

    Returns:
        int: Resultado da multiplicação de "a" e "b"
    """
    return int(a) * int(b)


if __name__ == "__main__":

    print("---------- Caluladora Hardcoded ----------")

    # TODO: Escrever exemplos usando as funçoes.
    print(subtracao(2, 2))
    print(multiplica(2, 2))
    print(soma(2, 2))
