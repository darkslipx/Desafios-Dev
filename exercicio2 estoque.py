import json
import uuid

# Converte a lista de produtos em dicionário, usando o código como chave.
# Assim a busca por código fica direta: produtos[101]
produtos = {}
with open("estoque.json", "r", encoding="utf-8") as arquivo:
    for item in json.load(arquivo)["estoque"]:
        produtos[item["codigoProduto"]] = item

# Lista que guarda o histórico de todas as movimentações feitas
movimentacoes = []


def pausar():
    input("\nPressione Enter para continuar...")


def ler_inteiro(mensagem):
    """Pede um número inteiro e repete enquanto o usuário digitar algo inválido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def consultar_estoque():
    print("\n" + "=" * 50)
    print("                 ESTOQUE ATUAL")
    print("=" * 50)
    for codigo, produto in produtos.items():
        print(f"  {codigo}  {produto['descricaoProduto']:<30}{produto['estoque']:>6} un")
    print("=" * 50)
    pausar()


def movimentar(tipo):
    """Registra uma entrada ou saída. tipo recebe 'ENTRADA' ou 'SAIDA'."""
    codigo = ler_inteiro("\nCódigo do produto: ")

    if codigo not in produtos:
        print("Produto não encontrado.")
        pausar()
        return

    produto = produtos[codigo]
    print(f"Produto: {produto['descricaoProduto']} (estoque atual: {produto['estoque']} un)")

    descricao = input("Descrição da movimentação: ")
    quantidade = ler_inteiro("Quantidade: ")

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        pausar()
        return

    if tipo == "SAIDA" and quantidade > produto["estoque"]:
        print(f"Estoque insuficiente. Disponível: {produto['estoque']} un")
        pausar()
        return

    # Atualiza o estoque
    if tipo == "ENTRADA":
        produto["estoque"] += quantidade
    else:
        produto["estoque"] -= quantidade

    # Gera o identificador único e registra no histórico
    movimentacao = {
        "id": str(uuid.uuid4()),
        "tipo": tipo,
        "descricao": descricao,
        "codigoProduto": codigo,
        "quantidade": quantidade,
        "estoqueFinal": produto["estoque"],
    }
    movimentacoes.append(movimentacao)

    sinal = "+" if tipo == "ENTRADA" else "-"
    print("\n" + "=" * 50)
    print(f"            {tipo} REGISTRADA")
    print("=" * 50)
    print(f"  ID:            {movimentacao['id']}")
    print(f"  Descrição:     {descricao}")
    print(f"  Produto:       {produto['descricaoProduto']}")
    print(f"  Quantidade:    {sinal}{quantidade}")
    print(f"  Estoque final: {produto['estoque']} un")
    print("=" * 50)
    pausar()


def historico():
    print("\n" + "=" * 50)
    print("            HISTÓRICO DE MOVIMENTAÇÕES")
    print("=" * 50)
    if not movimentacoes:
        print("  Nenhuma movimentação registrada.")
    for mov in movimentacoes:
        sinal = "+" if mov["tipo"] == "ENTRADA" else "-"
        print(f"  {mov['id'][:8]}  {mov['codigoProduto']}  {sinal}{mov['quantidade']:<6}"
              f"{mov['descricao']}  (final: {mov['estoqueFinal']})")
    print("=" * 50)
    pausar()


def main():
    opcao = -1
    while opcao != 0:
        print("\n" + "=" * 50)
        print("                MENU DE ESTOQUE")
        print("=" * 50)
        print("  1. Consultar estoque")
        print("  2. Entrada de produtos")
        print("  3. Saída de produtos")
        print("  4. Histórico de movimentações")
        print("  0. Sair")
        print("=" * 50)
        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 1:
            consultar_estoque()
        elif opcao == 2:
            movimentar("ENTRADA")
        elif opcao == 3:
            movimentar("SAIDA")
        elif opcao == 4:
            historico()
        elif opcao == 0:
            print("\nSaindo do programa. Até logo!")
        else:
            print("Opção inválida.")
            pausar()


main()
