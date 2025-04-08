# Projeto: API de Preços de Criptomoedas

Este é um projeto que consome dados de uma API para obter os preços de criptomoedas em tempo real, converte os valores para BRL (reais) e os armazena em um arquivo JSON. Além disso, o projeto inclui funcionalidades de automação e visualização de dados.

## Funcionalidades
- Consumo de dados da API CoinGecko para Bitcoin, Ethereum e Litecoin.
- Conversão dos preços para BRL com base em uma taxa de câmbio fixa.
- Registro de `timestamp` no arquivo JSON para acompanhamento do horário de coleta.
- Geração de histórico de preços.
- Automatização de consultas à API usando `schedule`.
- Visualização dos dados com gráficos utilizando Matplotlib.

## Estrutura do Projeto
```plaintext
projeto-API-cripto/
├── data/                 # Armazena arquivos gerados pelo projeto
│   └── cripto_precos.json  # Preços de criptomoedas com timestamps
├── src/                  # Código-fonte principal
│   ├── API.PY            # Script principal para consumo da API
│   ├── scheduler.py      # Automação de consultas com agendador
│   ├── visualization.py  # Geração de gráficos com Matplotlib
├── docs/                 # Documentação do projeto
│   └── README.md         # Este arquivo
├── .gitignore            # Arquivo para excluir arquivos irrelevantes do Git
└── requirements.txt      # Dependências necessárias
