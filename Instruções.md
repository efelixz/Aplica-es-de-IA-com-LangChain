
# 📚 Bibliotecas Python para IA, Manipulação de Dados e Integrações

---

## 🤖 IA e Modelos de Linguagem

### `openai`
- 📌 Cliente oficial da OpenAI para usar modelos como GPT-3.5 e GPT-4.
- ⚙️ `pip install openai`
- 🧪 Exemplo:
  ```python
  import openai
  openai.api_key = 'sua-chave'
  response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[{"role": "user", "content": "Olá, tudo bem?"}]
  )
  print(response['choices'][0]['message']['content'])
  ```

### `langchain`
- 📌 Framework para construir aplicações com LLMs (agentes, cadeias, memória).
- ⚙️ `pip install langchain`
- 🧪 Exemplo:
  ```python
  from langchain.chat_models import ChatOpenAI
  llm = ChatOpenAI(model_name="gpt-4")
  ```

### `langchain-community`, `langchain-openai`
- 📌 Componentes adicionais e integrações do LangChain.
- ⚙️ `pip install langchain-community langchain-openai`

### `huggingface-hub`
- 📌 Acesso a modelos e datasets hospedados no Hugging Face.
- ⚙️ `pip install huggingface-hub`
- 🧪 Exemplo:
  ```python
  from huggingface_hub import snapshot_download
  snapshot_download(repo_id="bert-base-uncased")
  ```

### `transformers`
- 📌 Biblioteca da Hugging Face para modelos como BERT, GPT2, T5.
- ⚙️ `pip install transformers`
- 🧪 Exemplo:
  ```python
  from transformers import pipeline
  classifier = pipeline("sentiment-analysis")
  print(classifier("Eu amo inteligência artificial!"))
  ```

### `tiktoken`
- 📌 Tokenizador oficial da OpenAI (contagem de tokens).
- ⚙️ `pip install tiktoken`

### `sentence-transformers`
- 📌 Geração de embeddings e busca semântica.
- ⚙️ `pip install sentence-transformers`

### `faiss-cpu`
- 📌 Indexação vetorial para buscas por similaridade.
- ⚙️ `pip install faiss-cpu`

### `llama-index`
- 📌 Conecta documentos e bases de dados a LLMs (ex: PDF + GPT).
- ⚙️ `pip install llama-index`

### `cohere`
- 📌 Cliente para usar modelos da API Cohere (textos, embeddings).
- ⚙️ `pip install cohere`

---

## 📄 Manipulação de Dados

### `pypdf`
- 📌 Leitura e extração de conteúdo de arquivos PDF.
- ⚙️ `pip install pypdf`

### `beautifulsoup4`
- 📌 Web scraping e parsing de HTML/XML.
- ⚙️ `pip install beautifulsoup4`

### `pandas`
- 📌 Manipulação de dados tabulares.
- ⚙️ `pip install pandas`

### `numpy`
- 📌 Computação científica com arrays.
- ⚙️ `pip install numpy`

### `unstructured`
- 📌 Extração de conteúdo de documentos diversos (PDF, DOCX).
- ⚙️ `pip install "unstructured[all-docs]"`

### `python-docx`
- 📌 Leitura e escrita de documentos `.docx`.
- ⚙️ `pip install python-docx`

---

## 🎥 YouTube e Áudio

### `yt_dlp`
- 📌 Download de vídeos e áudios (YouTube e outros).
- ⚙️ `pip install yt-dlp`
- 🧪 Exemplo:
  ```bash
  yt-dlp https://youtube.com/video123
  ```

### `pydub`
- 📌 Processamento de arquivos de áudio (edição, corte, etc.).
- ⚙️ `pip install pydub`

### `openai-whisper`
- 📌 Transcrição automática de áudio para texto.
- ⚙️ `pip install git+https://github.com/openai/whisper.git`

### `moviepy`
- 📌 Edição de vídeo (recorte, texto, concatenação).
- ⚙️ `pip install moviepy`

---

## 🧩 Templates e Geração Dinâmica

### `jinja2`
- 📌 Criação de templates dinâmicos (HTML, prompts).
- ⚙️ `pip install jinja2`

### `markdown2`
- 📌 Conversão de Markdown em HTML.
- ⚙️ `pip install markdown2`

---

## ☁️ APIs do Google

### `google-api-python-client`
- 📌 Cliente para acesso às APIs do Google.
- ⚙️ `pip install google-api-python-client`

### `google-auth-httplib2`
- 📌 Autenticação com httplib2.
- ⚙️ `pip install google-auth-httplib2`

### `google-auth-oauthlib`
- 📌 Autenticação OAuth 2.0.
- ⚙️ `pip install google-auth-oauthlib`

### `gspread`
- 📌 Leitura e escrita em Google Sheets.
- ⚙️ `pip install gspread`

---

## 📓 Jupyter e Execução de Código

### `ipykernel`
- 📌 Kernel Python para Jupyter.
- ⚙️ `pip install ipykernel`

### `notebook`
- 📌 Interface clássica do Jupyter.
- ⚙️ `pip install notebook`

### `jupyterlab`
- 📌 Ambiente moderno para notebooks e dados.
- ⚙️ `pip install jupyterlab`

### `ipywidgets`
- 📌 Componentes interativos em notebooks.
- ⚙️ `pip install ipywidgets`

---

## 🧰 Utilitários Recomendados

### `python-dotenv`
- 📌 Carrega variáveis de ambiente de arquivos `.env`.
- ⚙️ `pip install python-dotenv`

### `tenacity`
- 📌 Re-tentativas automáticas de funções (útil para APIs).
- ⚙️ `pip install tenacity`

### `rich`
- 📌 Saída elegante e colorida no terminal.
- ⚙️ `pip install rich`

### `loguru`
- 📌 Logger poderoso e simples.
- ⚙️ `pip install loguru`

### `requests`
- 📌 Cliente HTTP básico.
- ⚙️ `pip install requests`

### `httpx`
- 📌 Cliente HTTP moderno (assíncrono).
- ⚙️ `pip install httpx`

---
