import json


def calcular_comissao(valor):
    """Aplica a regra de comissão sobre uma única venda."""
    if valor < 100:
        return 0
    elif valor < 500:
        return valor * 0.01
    else:
        return valor * 0.05


def main():
    # Lê o arquivo JSON e pega a lista de vendas
    with open("vendas.json", "r", encoding="utf-8") as arquivo:
        vendas = json.load(arquivo)["vendas"]

    # Dicionário que acumula, por vendedor, o total vendido e a comissão
    resumo = {}

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = venda["valor"]
        comissao = calcular_comissao(valor)

        # Primeira vez que o vendedor aparece: cria a entrada zerada
        if vendedor not in resumo:
            resumo[vendedor] = {"total_vendido": 0, "comissao": 0, "qtd_vendas": 0}

        resumo[vendedor]["total_vendido"] += valor
        resumo[vendedor]["comissao"] += comissao
        resumo[vendedor]["qtd_vendas"] += 1

    # Exibição do resultado
    print("=" * 62)
    print("                  COMISSÃO POR VENDEDOR")
    print("=" * 62)
    print(f"  {'Vendedor':<18}{'Vendas':>8}{'Total vendido':>17}{'Comissão':>15}")
    print("-" * 62)

    total_geral = 0
    for vendedor, info in resumo.items():
        print(f"  {vendedor:<18}{info['qtd_vendas']:>8}"
              f"{'R$ ' + format(info['total_vendido'], '.2f'):>17}"
              f"{'R$ ' + format(info['comissao'], '.2f'):>15}")
        total_geral += info["comissao"]

    print("-" * 62)
    print(f"  {'Total de comissões':<43}{'R$ ' + format(total_geral, '.2f'):>15}")
    print("=" * 62)


main()
