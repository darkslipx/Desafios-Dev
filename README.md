# Desafio Dev

Resolução dos três exercícios do desafio técnico, desenvolvidos em **Python 3**, utilizando apenas bibliotecas nativas da linguagem.

## Estrutura do projeto

```
desafio-dev/
├── exercicio1_comissao.py   # Cálculo de comissão por vendedor
├── exercicio2_estoque.py    # Movimentação de estoque
├── exercicio3_juros.py      # Cálculo de juros por atraso
├── vendas.json              # Dados de vendas (usado no exercício 1)
├── estoque.json             # Estoque inicial (usado no exercício 2)
└── README.md
```

## Requisitos

* Python 3.8 ou superior
* Nenhuma biblioteca externa. São usados apenas módulos nativos: `json`, `uuid` e `datetime`

Para verificar se o Python está instalado:

```bash
python --version
```

Caso não esteja, faça o download em [python.org/downloads](https://www.python.org/downloads/). No Windows, marque a opção **Add Python to PATH** durante a instalação.

## Como executar

**1. Clone o repositório**

```bash
git clone https://github.com/SEU_USUARIO/desafio-dev.git
cd desafio-dev
```

Ou baixe pelo botão **Code > Download ZIP** e extraia a pasta.

**2. Execute o exercício desejado**

Os comandos devem ser executados dentro da pasta do projeto, pois os exercícios 1 e 2 leem os arquivos JSON que estão nela.

```bash
python exercicio1_comissao.py
python exercicio2_estoque.py
python exercicio3_juros.py
```

Em alguns sistemas (Linux e macOS) o comando pode ser `python3` em vez de `python`.

## Exercício 1: Comissão por vendedor

### Enunciado

Ler os registros de vendas do time comercial e calcular a comissão de cada vendedor, aplicando a regra abaixo em cada venda:

| Valor da venda | Comissão |
|---|---|
| Abaixo de R$ 100,00 | Sem comissão |
| Abaixo de R$ 500,00 | 1% |
| A partir de R$ 500,00 | 5% |

### Como funciona

1. O arquivo `vendas.json` é aberto e convertido em estrutura Python com `json.load()`
2. Cada venda é percorrida com um `for`, e a função `calcular_comissao()` aplica a regra
3. Os valores são acumulados em um dicionário que usa o nome do vendedor como chave, guardando quantidade de vendas, total vendido e comissão
4. Ao final, o resumo é exibido em formato de tabela, com o total geral de comissões

### Resultado

```
==============================================================
                  COMISSÃO POR VENDEDOR
==============================================================
  Vendedor            Vendas    Total vendido       Comissão
--------------------------------------------------------------
  João Silva              10      R$ 10754.70      R$ 495.68
  Maria Souza              9       R$ 9874.30      R$ 465.95
  Carlos Oliveira          8       R$ 7928.35      R$ 379.37
  Ana Lima                 9       R$ 8763.95      R$ 404.98
--------------------------------------------------------------
  Total de comissões                              R$ 1745.98
==============================================================
```

## Exercício 2: Movimentação de estoque

### Enunciado

Permitir lançar movimentações de entrada e saída dos produtos do estoque, onde cada movimentação possui um **identificador único** e uma **descrição**, retornando ao final a quantidade em estoque do produto movimentado.

### Como funciona

1. O arquivo `estoque.json` é lido e a lista de produtos é convertida em um dicionário, usando o código do produto como chave. Isso permite localizar um produto diretamente pelo código, sem percorrer a lista a cada busca
2. Um menu interativo roda dentro de um `while` até o usuário escolher sair
3. Em cada movimentação o usuário informa o código do produto, uma descrição e a quantidade
4. O estoque é atualizado e a movimentação recebe um ID único gerado com `uuid.uuid4()`
5. Cada movimentação é registrada em uma lista de histórico, que pode ser consultada pelo menu

### Menu

```
==================================================
                MENU DE ESTOQUE
==================================================
  1. Consultar estoque
  2. Entrada de produtos
  3. Saída de produtos
  4. Histórico de movimentações
  0. Sair
==================================================
```

### Exemplo de movimentação

```
==================================================
            SAIDA REGISTRADA
==================================================
  ID:            5624fb1b-99fd-4f14-9e1f-d4c453dbfcf7
  Descrição:     Venda
  Produto:       Caderno Universitário
  Quantidade:    -10
  Estoque final: 65 un
==================================================
```

### Validações

* Código de produto inexistente é recusado
* Quantidade deve ser maior que zero
* Saídas maiores que o estoque disponível são bloqueadas, evitando estoque negativo
* Entradas não numéricas não encerram o programa, o valor é solicitado novamente

### Observação

As movimentações são mantidas em memória durante a execução. Ao encerrar o programa, o estoque volta aos valores do arquivo `estoque.json`.

## Exercício 3: Juros por atraso

### Enunciado

A partir de um valor e de uma data de vencimento, calcular o valor dos juros na data de hoje, considerando multa de 2,5% ao dia.

### Como funciona

1. O usuário informa o valor do título e a data de vencimento no formato `DD/MM/AAAA`
2. A data é convertida de texto para data com `datetime.strptime()`
3. A diferença entre a data de hoje e o vencimento resulta na quantidade de dias de atraso
4. Os juros são calculados com a fórmula:

```
juros = valor × 0,025 × dias de atraso
total = valor + juros
```

5. Se o título ainda não venceu, o programa informa que não há juros

### Exemplo

Valor de R$ 1.000,00 com 3 dias de atraso:

```
========================================
  Valor original:  R$ 1000.00
  Vencimento:      01/10/2026
  Data de hoje:    04/10/2026
----------------------------------------
  Dias em atraso:  3
  Juros (2,5%/dia): R$ 75.00
  Total a pagar:   R$ 1075.00
========================================
```

### Validações

* O valor aceita vírgula ou ponto como separador decimal
* Valores negativos, zero ou não numéricos são recusados
* Datas em formato inválido são solicitadas novamente

## Decisões técnicas

**Python como linguagem:** escolhido pela leitura clara da lógica, permitindo que o raciocínio de cada exercício fique evidente no código.

**Dados em arquivos JSON separados:** os dados ficam fora do código, como em um cenário real, onde viriam de um arquivo ou de uma API. Para alterar as vendas ou o estoque basta editar os arquivos JSON, sem mexer nos programas.

**Organização em funções:** cada responsabilidade está em uma função com nome descritivo (`calcular_comissao`, `movimentar`, `ler_data`), facilitando a leitura e evitando repetição. Entrada e saída de estoque, por exemplo, compartilham a mesma função.

**Tratamento de erros:** entradas do usuário são validadas com `try/except`, impedindo que o programa seja encerrado por um valor digitado incorretamente.
