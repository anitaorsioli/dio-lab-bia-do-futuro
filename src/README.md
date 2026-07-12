# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

# Passo a passo da Execução

## Setup do Ollama

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

Evidências:

O meu:
<img width="886" height="486" alt="image" src="https://github.com/user-attachments/assets/f7dd9d1a-7e5e-492e-a2f3-db53f5f4a679" />

A partir daqui, evidências de que o código roda
<img width="886" height="710" alt="image" src="https://github.com/user-attachments/assets/01a1dc0e-2659-4525-a31d-bf0f7fe6ad0f" />

<img width="886" height="752" alt="image" src="https://github.com/user-attachments/assets/38144a4f-
6617-4480-92ca-bb6045e3af63" />

<img width="886" height="656" alt="image" src="https://github.com/user-attachments/assets/2f397286-0ae3-47b6-bc48-cf6ab56f772b" />

<img width="886" height="865" alt="image" src="https://github.com/user-attachments/assets/a1c8eeca-1c3d-4e26-8129-e389dda61d12" />

<img width="886" height="780" alt="image" src="https://github.com/user-attachments/assets/391c3c09-c966-44c9-9e54-f481b1a764f3" />







