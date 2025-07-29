class Pedido:
    def __init__(self):
        self.itens = []  
    
    def adicionar_item(self, preco):
        self.itens.append(preco)

    def calcular_total(self,):
        return sum(self.itens)

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    #TODO: Chame o método adicionar_item corretamente: 
    pedido.adicionar_item(float(preco))

# TODO: Exiba o total formatado com duas casas decimais:
print(f"{pedido.calcular_total():.2f}")