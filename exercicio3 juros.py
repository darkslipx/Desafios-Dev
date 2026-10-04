from datetime import date, datetime

TAXA_DIARIA = 0.025  # 2,5% ao dia


def ler_valor():
    """Pede o valor e aceita tanto vírgula quanto ponto como separador decimal."""
    while True:
        texto = input("Valor do título (R$): ").replace(",", ".")
        try:
            valor = float(texto)
            if valor > 0:
                return valor
            print("O valor deve ser maior que zero.")
        except ValueError:
            print("Valor inválido. Exemplo: 1500.00")


def ler_data():
    """Pede a data de vencimento no formato DD/MM/AAAA."""
    while True:
        texto = input("Data de vencimento (DD/MM/AAAA): ")
        try:
            return datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Exemplo: 25/09/2026")


def main():
    print("=" * 40)
    print("        CÁLCULO DE JUROS POR ATRASO")
    print("=" * 40)

    valor = ler_valor()
    vencimento = ler_data()
    hoje = date.today()

    # Subtrair datas gera um timedelta; .days pega o número de dias
    dias_atraso = (hoje - vencimento).days

    print("\n" + "=" * 40)
    print(f"  Valor original:  R$ {valor:.2f}")
    print(f"  Vencimento:      {vencimento.strftime('%d/%m/%Y')}")
    print(f"  Data de hoje:    {hoje.strftime('%d/%m/%Y')}")
    print("-" * 40)

    if dias_atraso <= 0:
        print("  Título não está vencido. Sem juros.")
    else:
        juros = valor * TAXA_DIARIA * dias_atraso
        total = valor + juros
        print(f"  Dias em atraso:  {dias_atraso}")
        print(f"  Juros (2,5%/dia): R$ {juros:.2f}")
        print(f"  Total a pagar:   R$ {total:.2f}")

    print("=" * 40)


main()
