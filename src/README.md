# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

# Passo a passo da Execução

## Setup do Ollma

```bash
# 1. Instalar Ollama (ollma.com)
# 2. Baixar um modelo leve
ollma pull gpt-oss
# 3. Testar se funciona
ollama run gpt-oss "olá!"

## Código completo

Todo código-fonte está no arquivo "app.py".



```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)


├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
1. Instalar dependências
pip install streamlit pandas requirements

2. Garantir que o ollama está rodando
ollama serve

3. Rodar o app
Streamlit run app.py

openai -> ollama
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py ou streamlit run .\src\app.py
```
