# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto

Este repositório contém a minha implementação para o desafio de desenvolvimento de um Agente Financeiro Inteligente utilizando IA Generativa.

## Minha Implementação e Diferenciais

🌟 Principais Funcionalidades Implementadas:
Antecipação Ativa: O agente não espera o usuário perguntar; ele analisa o transacoes.csv e sugere insights baseados em desvios de padrão.

Persona Adaptativa: Configurado com um tom de voz [ex: Consultor Amigável / Analista Técnico] detalhado no System Prompt.

Mecanismo Anti-Alucinação: Implementação de travas de segurança via prompt e checagem de dados para garantir que o agente só recomende produtos contidos em produtos_financeiros.json.

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.
Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:
---
🛠️ Tecnologias e Ferramentas Utilizadas
Para este protótipo, selecionei a seguinte stack tecnológica:

LLM: Ollama com gpt-oss

Interface Visual: Streamlit

Orquestração & Prompts: Utilizando o Python no VS Code

Análise de Dados: 
    Pandas (para leitura dos arquivos mockados em data/)
    Streamlit (para visualização do chat criado)
    
---

[ ] 1. Documentação do Agente: Detalhada 

- **Caso de Uso:** Qual problema financeiro ele resolve? (ex: consultoria de investimentos, planejamento de metas, alertas de gastos)
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?
- 📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

[ ] 2. Base de Conhecimento

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |

Você pode adaptar ou expandir esses dados conforme seu caso de uso.

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

[ ] 3. Prompts do Agente: Engenharia de prompt documentada em docs/03-prompts.md

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

[ ] 4. Aplicação Funcional: Código do protótipo interativo localizado na pasta src/

🏃‍♂️ Como Executar a Aplicação

Foi desenvolvido um **protótipo funcional** do agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

[ ] 5. Avaliação e Métricas: Relatório de comportamento do modelo em docs/04-metricas.md

Como avaliar a qualidade do agente:

**Métricas Utilizadas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

[ ] 6. Pitch: Roteiro e link do vídeo de 3 minutos em docs/05-pitch.md

Vídeo **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

🤝 Créditos
Este projeto é um fork do desafio original Agente Financeiro Inteligente com IA Generativa. As instruções de contexto e os dados mockados da pasta data/ foram mantidos para garantir a conformidade com os requisitos propostos.

## Considerações Finais do Passo a Passo:

1. **Começamos pelo prompt:** Pois um bom system prompt é a base de um agente eficaz
2. **Usamos os dados mockados:** Pois eles garantem consistência e evitam problemas com dados sensíveis
3. **Focamos na segurança:** No setor financeiro, evitar alucinações é crítico
4. **Testamos cenários reais:** Simular perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos aproximadamente
