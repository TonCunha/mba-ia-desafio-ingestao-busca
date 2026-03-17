# Desafio MBA Engenharia de Software com IA - Full Cycle

Este projeto implementa uma solução completa de Recuperação Aumentada por Geração (RAG - Retrieval-Augmented Generation) para processamento e consulta de documentos PDF. O sistema permite ingerir documentos, armazená-los em um banco de dados vetorial e realizar consultas conversacionais baseadas no conteúdo dos documentos.

## Funcionalidades

- **Ingestão de Documentos**: Carrega e processa arquivos PDF, dividindo o conteúdo em chunks e armazenando embeddings vetoriais.
- **Busca Vetorial**: Utiliza PostgreSQL com pgvector para busca semântica eficiente.
- **Chat Interativo**: Interface de chat que responde perguntas baseadas exclusivamente no conteúdo dos documentos ingeridos.

## Pré-requisitos

- Python
- Docker e Docker Compose
- Chave da API do OpenAI
- Arquivo PDF para ingestão

## Configuração do Ambiente

### 1. Criar Ambiente Virtual

```bash
python -m venv venv
```

### 2. Ativar Ambiente Virtual

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
OPENAI_API_KEY=SUA_CHAVE_AQUI
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
OPENAI_LLM_MODEL=gpt-5-nano
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag
PG_VECTOR_COLLECTION_NAME=openapi_collection
PDF_PATH=CAMINHO_COMPLETO_PARA_O_SEU_PDF
```

**Notas importantes**:
- Substitua `SUA_CHAVE_AQUI` pela sua chave da API do OpenAI
- `PDF_PATH` deve ser o caminho absoluto para o arquivo PDF que deseja ingerir
- Ajuste `OPENAI_LLM_MODEL` caso necessário (ex: `gpt-4`, `gpt-3.5-turbo`)

### 5. Iniciar Banco de Dados

```bash
docker compose up -d
```

Este comando iniciará um container PostgreSQL com a extensão pgvector configurada.

## Executando a Aplicação

### Ordem de Execução Importante

**IMPORTANTE**: Você deve executar `ingest.py` **antes** de `chat.py` para garantir que os documentos estejam disponíveis para consulta.

### 1. Ingerir Documentos

Execute o script de ingestão para processar e armazenar o PDF:

```bash
python src/ingest.py
```

Este script irá:
- Carregar o PDF especificado em `PDF_PATH`
- Dividir o conteúdo em chunks de texto
- Gerar embeddings usando OpenAI
- Armazenar os vetores no banco de dados PostgreSQL

### 2. Iniciar Chat

Após a ingestão, execute o chat interativo:

```bash
python src/chat.py
```

O chat permitirá fazer perguntas sobre o conteúdo do documento PDF ingerido.

## Estrutura do Projeto

```
src/
├── ingest.py    # Script para ingestão de documentos PDF
├── search.py    # Configuração da busca vetorial e chain RAG
└── chat.py      # Interface de chat interativo
```

## Como Usar

1. Configure o ambiente conforme descrito acima
2. Inicie o Docker Compose
3. Execute `python src/ingest.py` para ingerir o PDF
4. Execute `python src/chat.py` para iniciar o chat
5. Digite suas perguntas no prompt
6. Digite "sair" para encerrar o chat

## Notas Técnicas

- O sistema utiliza LangChain para orquestração
- Embeddings são gerados usando modelos da OpenAI
- O banco vetorial é PostgreSQL com pgvector
- As respostas são baseadas exclusivamente no contexto dos documentos ingeridos
- Não há conhecimento prévio ou externo utilizado nas respostas

## Solução de Problemas

- **Erro de conexão com banco**: Verifique se o Docker Compose está rodando e as credenciais estão corretas
- **Erro de API OpenAI**: Confirme sua chave da API e limites de uso
- **Arquivo PDF não encontrado**: Verifique o caminho absoluto em `PDF_PATH`
- **Dependências faltando**: Execute `pip install -r requirements.txt` novamente
