def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    confirmadas = []
    recusadas = []

    for quarto in reservas_solicitadas:
        if quarto in quartos_disponiveis:
            confirmadas.append(quarto)
            quartos_disponiveis.remove(quarto)
        else:
            recusadas.append(quarto)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()