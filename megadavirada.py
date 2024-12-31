from random import randint, sample

NUMERO_DEZENAS = 6

# Lista dos últimos 10 resultados da Mega-Sena da Virada para comparação
ULTIMOS_RESULTADOS = [
    [24, 56, 33, 48, 21, 41],  
    [3, 10, 12, 23, 27, 58],
    [5, 10, 25, 32, 47, 49],
    [2, 18, 31, 42, 51, 56],
    [6, 21, 35, 38, 53, 57],
    [1, 3, 5, 10, 12, 21],
    [8, 22, 27, 35, 40, 41],
    [4, 17, 20, 27, 38, 53],
    [7, 14, 23, 30, 46, 56],
    [9, 11, 16, 21, 36, 48]
]

def existeNumero(numeros, n):
    return n in numeros

def gerarPalpiteLogico(ultimos_resultados):
    # Baseia-se em números mais frequentes ou próximos dos últimos resultados
    frequencia = {}
    for resultado in ultimos_resultados:
        for numero in resultado:
            frequencia[numero] = frequencia.get(numero, 0) + 1

    # Ordena os números pela frequência
    numeros_frequentes = sorted(frequencia, key=frequencia.get, reverse=True)

    # Adiciona variação aleatória para evitar jogos iguais
    numeros_unicos = list(set(numeros_frequentes))
    if len(numeros_unicos) >= NUMERO_DEZENAS:
        return sorted(sample(numeros_unicos, NUMERO_DEZENAS))

    # Preenche com números aleatórios caso não haja suficientes
    palpite = numeros_unicos[:]
    while len(palpite) < NUMERO_DEZENAS:
        numero = randint(1, 60)
        if numero not in palpite:
            palpite.append(numero)

    return sorted(palpite)

def gerarJogos(qtd_jogos, ultimos_resultados):
    jogos = []
    for _ in range(qtd_jogos):
        jogos.append(gerarPalpiteLogico(ultimos_resultados))
    return jogos

def main():
    print("Bem-vindo ao Gerador de Palpites para a Mega-Sena da Virada!")
    try:
        qtd_jogos = int(input("Quantos jogos você deseja gerar? "))
        if qtd_jogos <= 0:
            print("Por favor, insira um número maior que 0.")
            return
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
        return

    jogos = gerarJogos(qtd_jogos, ULTIMOS_RESULTADOS)
    print("\nSeus jogos gerados com base nos últimos resultados:")
    for i, jogo in enumerate(jogos, start=1):
        print(f"Jogo {i}: {', '.join(map(str, jogo))}")

if __name__ == "__main__":
    main()
