# MapaStatus (RPA)

Solução de automação RPA (Robotic Process Automation) desenvolvida em Python para otimizar o processamento de relatórios comerciais. O projeto automatiza a leitura de centenas de arquivos PDF, extraindo metadados dos nomes dos arquivos e dados estruturados do conteúdo interno, consolidando tudo em planilhas Excel prontas para análise.

### ⚠️ Problemática

Como Assistente Comercial, surgiu a necessidade crítica de realizar o controle detalhado de escolas **adotantes** vs. **não adotantes** segmentado por divulgador. No entanto, o sistema corporativo atual apresenta limitações:

* **Ausência de Relatórios Consolidados:** O sistema não fornece uma visão unificada que diferencie o status de adoção escola por escola em um único documento.
* **Processo Fragmentado:** A única forma de obter esses dados é através da emissão de múltiplos relatórios PDF separados (um para adotantes e outro para não adotantes por divulgador).
* **Carga de Trabalho Manual:** Consolidar manualmente centenas desses PDFs em uma planilha única para análise estratégica consumiria horas de trabalho repetitivo, sendo altamente passível de erros humanos.

### ✅ Solução (RPA)

Este projeto implementa um fluxo de **RPA (Robotic Process Automation)** que elimina o trabalho manual e garante 100% de precisão nos dados:

* **Automação de Ponta a Ponta:** O robô varre as pastas de relatórios, identifica o divulgador e o status de adoção (extraídos inteligentemente do nome do arquivo) e lê o conteúdo interno de cada PDF.
* **Extração com Regex:** Utiliza Expressões Regulares avançadas para capturar o nome exato e o código de cada escola, independentemente de variações na formatação do PDF.
* **Consolidação Inteligente:** O sistema une os dados de todos os relatórios processados em uma única estrutura de dados (DataFrame), gerando um arquivo Excel final pronto para tomadas de decisão comercial.
* **Alta Performance:** Graças ao processamento paralelo, o que levaria horas para ser feito manualmente é concluído em poucos segundos.

## 📁 Estrutura do Projeto

```text
MapaStatus/
├── data/                   # Centraliza todos os arquivos de dados
│   ├── input/              # [🔐 privado] Coloque aqui as pastas com os PDFs
│   ├── output/             # [🔐 privado] Local onde os arquivos Excel (.xlsx) são gerados
│   └── samples/            # 📂 Arquivos de exemplo para teste e demonstração
│       ├── input/          # Exemplo de estrutura de PDFs fictícios
│       └── output/         # Simulação do resultado consolidado
├── src/                    # Código-fonte principal
│   ├── main.py             # Ponto de entrada (CLI)
│   ├── core.py             # Lógica de extração e processamento de PDF
│   └── utils.py            # Funções auxiliares e configuração de logs
├── logs/                   # Histórico de execuções para auditoria
├── scripts/                # Atalhos de execução (Windows .bat)
├── requirements.txt        # Dependências do projeto
└── .gitignore              # Arquivos ignorados pelo controle de versão
```

## 🚀 Como Executar

### Pré-requisitos

* Python 3.8+ instalado.
* Dependências instaladas: `pip install -r requirements.txt`

### Modo Automático (Windows)

1. Coloque a pasta com os PDFs dentro de `data/input/`.
2. Execute o arquivo `scripts/executar_extracao.bat`.
3. Informe o nome da pasta quando solicitado.
4. Verifique o resultado na pasta `data/output/`.

### Modo Desenvolvedor (Linha de Comando)

```bash
python -m src.main data/input/NOME_DA_PASTA
```

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem base.
* **pdfplumber**: Extração de texto robusta de PDFs.
* **Pandas**: Manipulação de dados e exportação para Excel.
* **Concurrent Futures**: Processamento paralelo para máxima performance.
* **Logging**: Registro detalhado de sucessos e erros.

## 🤖 Desenvolvimento Aumentado por IA (AI-Assisted)

Este projeto foi desenvolvido utilizando uma abordagem moderna de engenharia de software, onde utilizei ferramentas de **Inteligência Artificial (LLMs)** como co-piloto estratégico para:

* **Arquitetura e Lógica:** Tradução de requisitos de negócio em algoritmos eficientes de extração de dados.
* **Implementação de Regex:** Criação de padrões complexos de Expressões Regulares para captura precisa em documentos não estruturados.
* **Otimização Técnica:** Implementação de processamento paralelo e tratamento de erros guiado por boas práticas sugeridas por IA.
* **Curadoria e Validação:** Capacidade de orquestrar ferramentas avançadas para entregar uma solução profissional, demonstrando agilidade e foco na resolução de problemas, mesmo em tecnologias além do meu domínio principal.

Essa metodologia demonstra minha competência em adotar novas tecnologias de produtividade para entregar resultados escaláveis e precisos em tempo recorde.

## 💾 Destaques Técnicos

* **Processamento de Alto Desempenho**: Utiliza `concurrent.futures` para processar múltiplos PDFs em paralelo, reduzindo drasticamente o
  tempo de execução.
* **Extração Robusta**: Implementação de pdfplumber e Expressões Regulares (Regex) para captura precisa de nomes e códigos de escolas.
* **Arquitetura Profissional**: Estrutura de diretórios organizada (src/, data/, logs/), facilitando a manutenção e escala.
* **Monitoramento**: Sistema de logging detalhado para auditoria de processos e tratamento de erros.
* **Interface Amigável**: Acompanha script de lote (.bat) para execução simplificada por usuários finais no Windows.
