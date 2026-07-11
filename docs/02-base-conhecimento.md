# Base de Conhecimento
> [!TIP]
> Prompt sugerido para esta etapa: Preciso organizar a base de conhecimento do meu agente financeiro educativo. Tenho estes arquivos de dados: [liste os arquivos]. Me ajude a: (1) entender o que cada arquivo contém, (2) decidir como usar cada um, (3) criar um exemplo de contexto formatado para incluir no prompt.


## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, dar continuidade de forma mais eficiente |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre  as dúvidas e necessidades de aprendizado do cliente |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil; conhecer os produtos disponíveis para que possam ser explicado e ensinados ao cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usaressas informações de forma didática |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.
> Deixar para consultas futuras, em outros projetos
---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O Produto FII foi adicionado, substituindo o fundo multimercado, pois não tenho muito conhecimento ao respeito

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt. Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl C,Ctrl V) ou carregar os arquivos via código

```python
import pandas as pd
import json

# CSVs
histórico= pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r',encoding='utf-8') as f:
  podutos = json.load(f)
```
como está no código no vscode:
import pandas as pd
import json

# ---- CARREGAR DADOS ----------

perfil = json.load(open('.data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transcaoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))


### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?
> Para simplificar, podemos injetar no nosso prompt, garantindo que o agente tenha o melhor contexto possível. Lembrando que, em soluções mais robustas,o ideal é que essas informações seja carregadas dinamicamente para que possamos ganhar flexibilidade, poisseos dados mudarem, muda na fonte, não no código.

```text
Dados do Cliente e Perfil:
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}


Transações do cliente: {transacoes.csv}

data	descricao	categoria	valor	tipo
2025-10-01	Salário	receita	5000.00	entrada
2025-10-02	Aluguel	moradia	1200.00	saida
2025-10-03	Supermercado	alimentacao	450.00	saida
2025-10-05	Netflix	lazer	55.90	saida
2025-10-07	Farmácia	saude	89.00	saida
2025-10-10	Restaurante	alimentacao	120.00	saida
2025-10-12	Uber	transporte	45.00	saida
2025-10-15	Conta de Luz	moradia	180.00	saida
2025-10-20	Academia	saude	99.00	saida
2025-10-25	Combustível	transporte	250.00	saida


Histórico de atendimento do Cliente:

data	canal	tema	resumo	resolvido
2025-09-15	chat	CDB	Cliente perguntou sobre rentabilidade e prazos	sim
2025-09-22	telefone	Problema no app	Erro ao visualizar extrato foi corrigido	sim
2025-10-01	chat	Tesouro Selic	Cliente pediu explicação sobre o funcionamento do Tesouro Direto	sim
2025-10-12	chat	Metas financeiras	Cliente acompanhou o progresso da reserva de emergência	sim
2025-10-25	email	Atualização cadastral	Cliente atualizou e-mail e telefone	sim

Produtos disponíveis para ensino:

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliario (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "6% a 12% ao ano",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]
```
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.
O exemplo abaixo montado, se baseia em dados originais da base de conhecimento, mas o sitetisa, deixando somente as informações mais relevantes, otimizando assim, o consumo de tokens. Vale lembrar que mais importante que economizartokens, é ter todas as informações relevantes disponíveis em seu contexto
```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000
- Objetivo: Construir reserva deemergência
- Reserva atual: R$ 10.000(meta: R$ 15.000)

Resumo de gastos:
- Alimentação - R$ 1.300
- Streaming - R$ 55
- Moradia - R$ 1.000
- Transporte: R$ 295
- Saúde: R$ 100
- Lazer: R$ 55,00
- Total de saídas: R$ 2.805

Produtos disponíveis para explicar:
- Tesouro selic (Risco baixo)
- CDB Liquidez Diária (Risco baixo)
- LCI/LCA (Risco baixo)
- Funco Imobiliario (FII) (Risco médio)
- Fundo de ações (Risco alto)

```
