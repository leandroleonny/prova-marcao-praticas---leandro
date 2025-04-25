
def adicionar_produto(codigo, nome, quantidade, preco):
    print(f"Produto adicionado: {codigo} - {nome}, Qtd: {quantidade}, Preço: R${preco}")

def listar_produtos():
    print("Listando todos os produtos cadastrados...")


def entrada_estoque(codigo_produto, quantidade):
    print(f"Entrada de {quantidade} unidades no estoque do produto {codigo_produto}")

def saida_estoque(codigo_produto, quantidade):
    print(f"Saída de {quantidade} unidades do estoque do produto {codigo_produto}")


def gerar_relatorio_estoque():
    print("Gerando relatório atual do estoque...")

def gerar_relatorio_vendas():
    print("Gerando relatório de vendas...")


def main():
    adicionar_produto(101, "Caderno", 50, 12.90)
    listar_produtos()

    entrada_estoque(101, 10)
    saida_estoque(101, 5)

    gerar_relatorio_estoque()
    gerar_relatorio_vendas()

# Executar a função principal
main()
