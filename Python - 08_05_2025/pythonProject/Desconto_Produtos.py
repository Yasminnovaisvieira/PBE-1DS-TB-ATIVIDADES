# 10% de desconto em três produtos. Calculo do preço final de cada um (Produto 1: R$ 50,00 / Produto 2: R$ 120,00 / Produto 3: R$ 200,00).

def desconto_produto(produto):
    resultado = produto - (produto * 0.10)
    print(f"Preço do produto: {produto:.2f}\nPreço com desconto (10%): {resultado:.2f}\n")
    return resultado

desconto_produto(50.00)
desconto_produto(120.00)
desconto_produto(200.00)