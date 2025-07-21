# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
#preco = float(input().strip())
#cupom = input().strip()

preco = 100
cupom = "DESCONTO10"
result = preco - preco*(descontos[cupom])

if preco > 0 and (cupom in descontos):
  print(f"{result:.2f}")

# TODO: Aplique o desconto se o cupom for válido: