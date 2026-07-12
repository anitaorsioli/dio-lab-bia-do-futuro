import json
import pandas as pd
import requests
import streamlit as st
# import subprocess

# -----CONFIGURAÇÃO ----
OLLAMA_URL = 'http://localhost:11434/api/generate'
modelo = "gpt-oss"

# ---- CARREGAR DADOS ----------
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

#--------MONTAR CONTEXTO -----
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R${perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ----------SYSTEM PROMPT ---------------
SYSTEM_PROMPT = """Você é a AnIA, um educador financeiro amigável e didático.
Objetivo:
ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplo prático.

REGRAS:
- Sempre baseie suas respostas nos dados fornecidos para dar exemplos personalizados
- Nunca invente informações financeiras
- Se não souber algo, admita e ofereça alternativas
- Nunca recomende investimentos específicos, apenas explique como funciona;
- Linguagem simples, como se explicsse para um amigo;
- Sempre pergunte se o cliente entendeu;
- Jamais responda a pergunta fora do tema ensino de finanças pessoais;
- Quando ocorrer, responda lembrando que seu papel é ser educador financeiro.
"""

#---------Chamar ollama ---------
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": modelo, "prompt": prompt, "stream": False})
 #   print("Status:", r.status_code)
 #   print("Resposta:", r.text)
    return r.json()['response']

# ---- INTERFACE -----
st.title("Sou AnIA, Sua educadora financeira")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))

#Desisti de rodar pelo Prompt do Powershell do VSCode e rodei direto do prompt do anaconda, deu muito erro de instalação
#(base) C:\Users\FAMILY\Documents\Anita\bootcamp Afya\Chatbot-financeiro>streamlit run src\app.py

# You can now view your Streamlit app in your browser.

# Local URL: http://localhost:8501
# Network URL: http://192.168.0.22:8501 
#rodou sem problemas, só demora muito pra retornar, pois minha máquina já é lenta