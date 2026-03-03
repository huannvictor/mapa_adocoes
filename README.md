# Extrator de Dados de Escolas (RPA)

Solução de automação (RPA) desenvolvida em Python para otimizar o processamento de relatórios comerciais. O projeto automatiza a leitura de centenas de arquivos PDF, extraindo metadados dos nomes dos arquivos e dados estruturados do conteúdo interno, consolidando tudo em planilhas Excel prontas para análise.

## 📁 Estrutura do Projeto

```text
mapa-adocoes/
├── data/                   # Centraliza todos os arquivos de dados
│   ├── input/              # Coloque aqui as pastas com os PDFs (ex: 2026_01_13_relacao_escolas/)
│   └── output/             # Local onde os arquivos Excel (.xlsx) são gerados
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

- Python 3.8+ instalado.
- Dependências instaladas: `pip install -r requirements.txt`

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

- **Python**: Linguagem base.
- **pdfplumber**: Extração de texto robusta de PDFs.
- **Pandas**: Manipulação de dados e exportação para Excel.
- **Concurrent Futures**: Processamento paralelo para máxima performance.
- **Logging**: Registro detalhado de sucessos e erros.

## 💾 Destaques Técnicos:

* **Processamento de Alto Desempenho**: Utiliza `concurrent.futures` para processar múltiplos PDFs em paralelo, reduzindo drasticamente o
  tempo de execução.
* **Extração Robusta**: Implementação de pdfplumber e Expressões Regulares (Regex) para captura precisa de nomes e códigos de escolas.
* **Arquitetura Profissional**: Estrutura de diretórios organizada (src/, data/, logs/), facilitando a manutenção e escala.
* **Monitoramento**: Sistema de logging detalhado para auditoria de processos e tratamento de erros.
* **Interface Amigável**: Acompanha script de lote (.bat) para execução simplificada por usuários finais no Windows.


