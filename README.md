# 📄 API de Documentos - Flask & MongoDB Atlas

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

*Uma API RESTful robusta para gerenciamento de documentos usando Flask e MongoDB Atlas*

[🚀 Começar](#️-configuração-e-instalação) •
[📖 Documentação](#-endpoints-da-api) •
[🧪 Testes](#-testando-os-endpoints) •
[🔧 Solução de Problemas](#️-solução-de-problemas)

</div>

---

## 🌟 Funcionalidades

<table>
<tr>
<td width="50%">

### ✨ **Operações CRUD Completas**
- ✅ Cadastro de documentos JSON
- 🔍 Pesquisa por nome (case-insensitive)
- 🏠 Pesquisa por endereço/rua
- 🛒 Pesquisa por histórico de compras
- 🗑️ Exclusão por ID

</td>
<td width="50%">

### 🔧 **Recursos Técnicos**
- 🌐 API RESTful com Flask
- ☁️ Integração com MongoDB Atlas
- 🔒 Variáveis de ambiente seguras
- 📊 Tratamento robusto de erros
- 🎯 Queries otimizadas com regex

</td>
</tr>
</table>

---

## 🛠️ Stack Tecnológica

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| **Python** | 3.8+ | Linguagem principal |
| **Flask** | 2.0+ | Framework web |
| **PyMongo** | Latest | Driver MongoDB |
| **python-dotenv** | Latest | Gerenciamento de variáveis |
| **MongoDB Atlas** | Cloud | Banco de dados |

---

## 🚀 Endpoints da API

### 📋 Resumo dos Endpoints

```http
GET    /                    # Status da API
POST   /cadastrar          # Cadastra documento
GET    /pesquisar_nome     # Pesquisa por nome
GET    /pesquisar_rua      # Pesquisa por rua
GET    /pesquisar_compras  # Pesquisa por produto
DELETE /deletar/<id>       # Remove documento
```

### 📚 Detalhamento dos Endpoints

<details>
<summary><b>🏠 GET / - Status da API</b></summary>

**Descrição:** Verifica se a API está funcionando

**Resposta:**
```json
{
  "mensagem": "Bem-vindo à API de Documentos! Use os endpoints /cadastrar, /pesquisar_nome, etc."
}
```
</details>

<details>
<summary><b>➕ POST /cadastrar - Cadastrar Documento</b></summary>

**Descrição:** Cadastra um novo documento no banco

**Body (JSON):**
```json
{
  "nome": "Ana Clara Oliveira",
  "email": "ana.clara@example.com",
  "telefone": "5511987654321",
  "endereco": {
    "rua": "Rua das Acacias",
    "numero": "45",
    "cidade": "São Paulo"
  },
  "historico_compras": [
    {
      "descricao": "Livro de culinária",
      "valor": "75.00"
    }
  ]
}
```

**Resposta (201):**
```json
{
  "mensagem": "Documento cadastrado com sucesso!",
  "id_inserido": "60c72b2f9b1d8b3a4c5d6e7f"
}
```
</details>

<details>
<summary><b>🔍 GET /pesquisar_nome - Pesquisar por Nome</b></summary>

**Descrição:** Busca documentos por nome (parcial, case-insensitive)

**Parâmetros:**
- `nome` (query): Nome ou parte do nome a pesquisar

**Exemplo:** `/pesquisar_nome?nome=Ana`

**Resposta (200):**
```json
[
  {
    "_id": "60c72b2f9b1d8b3a4c5d6e7f",
    "nome": "Ana Clara Oliveira",
    "email": "ana.clara@example.com"
  }
]
```
</details>

<details>
<summary><b>🏠 GET /pesquisar_rua - Pesquisar por Rua</b></summary>

**Descrição:** Busca documentos por nome da rua

**Parâmetros:**
- `rua` (query): Nome da rua ou parte dela

**Exemplo:** `/pesquisar_rua?rua=Acacias`
</details>

<details>
<summary><b>🛒 GET /pesquisar_compras - Pesquisar por Compras</b></summary>

**Descrição:** Busca documentos por produtos no histórico de compras

**Parâmetros:**
- `produto` (query): Descrição do produto ou parte dela

**Exemplo:** `/pesquisar_compras?produto=Livro`
</details>

<details>
<summary><b>🗑️ DELETE /deletar/&lt;id&gt; - Deletar Documento</b></summary>

**Descrição:** Remove um documento pelo ID

**Parâmetros:**
- `id` (path): ObjectId do MongoDB

**Exemplo:** `/deletar/60c72b2f9b1d8b3a4c5d6e7f`

**Resposta (200):**
```json
{
  "mensagem": "Documento deletado com sucesso!",
  "id_deletado": "60c72b2f9b1d8b3a4c5d6e7f"
}
```
</details>

---

## ⚙️ Configuração e Instalação

### 📋 Pré-requisitos

- **Python 3.8+** instalado
- **Conta MongoDB Atlas** (cluster M0 gratuito)
- **Insomnia/Postman** para testes

### 🔧 Passo a Passo

#### 1️⃣ **Preparar o Ambiente**

```bash
# Clone ou crie a pasta do projeto
mkdir api-documentos-mongodb
cd api-documentos-mongodb

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

#### 2️⃣ **Instalar Dependências**

```bash
pip install Flask pymongo python-dotenv
```

#### 3️⃣ **Configurar MongoDB Atlas**

1. Acesse [MongoDB Atlas](https://cloud.mongodb.com/)
2. Crie um cluster (M0 gratuito)
3. Configure o **Network Access** (adicione seu IP)
4. Crie um **usuário do banco** com senha
5. Obtenha a **string de conexão**

#### 4️⃣ **Configurar Variáveis de Ambiente**

Crie o arquivo `.env` na raiz do projeto:

```env
MONGODB_URI="mongodb+srv://usuario:senha@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGODB_DB_NAME="seu_banco_de_dados"
MONGODB_COLLECTION_NAME="sua_colecao"
```

> ⚠️ **Importante:** Substitua `usuario`, `senha`, e os nomes do banco/coleção pelos seus valores reais.

#### 5️⃣ **Criar o arquivo app.py**

```python
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# --- CONFIGURAÇÃO DO MONGODB ATLAS ---
MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGODB_DB_NAME")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")

if not MONGO_URI:
    raise ValueError("MONGODB_URI não configurado no arquivo .env ou ambiente.")
if not DB_NAME:
    raise ValueError("MONGODB_DB_NAME não configurado no arquivo .env.")
if not COLLECTION_NAME:
    raise ValueError("MONGODB_COLLECTION_NAME não configurado no arquivo .env.")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# --- ENDPOINTS DA API ---

@app.route('/', methods=['GET'])
def home():
    """
    Rota raiz para verificar se a API está no ar.
    """
    return jsonify({"mensagem": "Bem-vindo à API de Documentos! Use os endpoints /cadastrar, /pesquisar_nome, etc."})

@app.route('/cadastrar', methods=['POST'])
def cadastrar_documento():
    """
    Recebe um documento JSON no corpo da requisição e o cadastra no MongoDB.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"erro": "Requisição inválida. Envie um JSON no corpo da requisição."}), 400

        result = collection.insert_one(data)
        return jsonify({
            "mensagem": "Documento cadastrado com sucesso!",
            "id_inserido": str(result.inserted_id)
        }), 201

    except Exception as e:
        return jsonify({"erro": f"Erro ao cadastrar documento: {str(e)}"}), 500

@app.route('/pesquisar_nome', methods=['GET'])
def pesquisar_nome():
    """
    Recebe 'nome' como parâmetro na URL e retorna documentos que contenham esse nome.
    """
    nome = request.args.get('nome')
    if not nome:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório na URL."}), 400

    try:
        documentos = list(collection.find({"nome": {"$regex": nome, "$options": "i"}}))
        for doc in documentos:
            doc['_id'] = str(doc['_id'])

        if documentos:
            return jsonify(documentos), 200
        else:
            return jsonify({"mensagem": "Nenhum documento encontrado com o nome fornecido."}), 404

    except Exception as e:
        return jsonify({"erro": f"Erro ao pesquisar por nome: {str(e)}"}), 500

@app.route('/pesquisar_rua', methods=['GET'])
def pesquisar_rua():
    """
    Recebe 'rua' como parâmetro na URL e retorna documentos que contenham essa rua.
    """
    rua = request.args.get('rua')
    if not rua:
        return jsonify({"erro": "Parâmetro 'rua' é obrigatório na URL."}), 400

    try:
        documentos = list(collection.find({"endereco.rua": {"$regex": rua, "$options": "i"}}))
        for doc in documentos:
            doc['_id'] = str(doc['_id'])

        if documentos:
            return jsonify(documentos), 200
        else:
            return jsonify({"mensagem": "Nenhum documento encontrado com a rua fornecida."}), 404

    except Exception as e:
        return jsonify({"erro": f"Erro ao pesquisar por rua: {str(e)}"}), 500

@app.route('/pesquisar_compras', methods=['GET'])
def pesquisar_compras():
    """
    Recebe 'produto' como parâmetro na URL e retorna documentos de pessoas que compraram esse produto.
    """
    produto = request.args.get('produto')
    if not produto:
        return jsonify({"erro": "Parâmetro 'produto' é obrigatório na URL."}), 400

    try:
        documentos = list(collection.find({"historico_compras.descricao": {"$regex": produto, "$options": "i"}}))
        for doc in documentos:
            doc['_id'] = str(doc['_id'])

        if documentos:
            return jsonify(documentos), 200
        else:
            return jsonify({"mensagem": "Nenhum documento encontrado com o produto fornecido."}), 404
    except Exception as e:
        return jsonify({"erro": f"Erro ao pesquisar por produto: {str(e)}"}), 500

@app.route('/deletar/<id>', methods=['DELETE'])
def deletar_documento(id):
    """
    Deleta um documento pelo seu _id.
    """
    try:
        object_id = ObjectId(id)
    except Exception:
        return jsonify({"erro": "ID inválido. O ID deve ser um ObjectId válido do MongoDB."}), 400

    try:
        result = collection.delete_one({"_id": object_id})

        if result.deleted_count == 1:
            return jsonify({"mensagem": "Documento deletado com sucesso!", "id_deletado": id}), 200
        else:
            return jsonify({"mensagem": "Nenhum documento encontrado com o ID fornecido para deletar."}), 404

    except Exception as e:
        return jsonify({"erro": f"Erro ao deletar documento: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

#### 6️⃣ **Executar a API**

```bash
python app.py
```

🎉 **Pronto!** Sua API estará rodando em `http://127.0.0.1:5000`

---

## 🧪 Testando os Endpoints

### 🔧 Configuração do Insomnia/Postman

#### 📝 Estrutura de Documento Exemplo

```json
{
  "nome": "Ana Clara Oliveira",
  "email": "ana.clara@example.com",
  "telefone": "5511987654321",
  "data_nascimento": "1988-11-25T00:00:00.000+00:00",
  "endereco": {
    "rua": "Rua das Acacias",
    "numero": "45",
    "bairro": "Jardim Paulista",
    "cidade": "São Paulo",
    "estado": "SP",
    "cep": "01400-000"
  },
  "ativo": true,
  "tags": ["cliente ouro", "newsletter"],
  "historico_compras": [
    {
      "product_id": "book543",
      "descricao": "Livro de culinária",
      "valor": "75.00"
    },
    {
      "product_id": "home123",
      "descricao": "Conjunto de panelas",
      "valor": "350.00"
    }
  ]
}
```

### 🎯 Testes no Insomnia

#### 1️⃣ **Teste: Status da API**
```http
GET http://127.0.0.1:5000/
```

#### 2️⃣ **Teste: Cadastrar Documento**
```http
POST http://127.0.0.1:5000/cadastrar
Content-Type: application/json

{
  "nome": "João Silva",
  "email": "joao@email.com",
  "endereco": {
    "rua": "Rua dos Coqueiros",
    "numero": "123"
  },
  "historico_compras": [
    {
      "descricao": "Fritadeira Elétrica",
      "valor": "120.00"
    }
  ]
}
```

#### 3️⃣ **Teste: Pesquisar por Nome**
```http
GET http://127.0.0.1:5000/pesquisar_nome?nome=João
```

#### 4️⃣ **Teste: Pesquisar por Rua**
```http
GET http://127.0.0.1:5000/pesquisar_rua?rua=Coqueiros
```

#### 5️⃣ **Teste: Pesquisar por Compras**
```http
GET http://127.0.0.1:5000/pesquisar_compras?produto=Fritadeira
```

#### 6️⃣ **Teste: Deletar Documento**
```http
DELETE http://127.0.0.1:5000/deletar/60c72b2f9b1d8b3a4c5d6e7f
```

---

## ⚠️ Solução de Problemas

### 🔧 Problemas Comuns

<details>
<summary><b>❌ Python não foi encontrado</b></summary>

**Problema:** `'python' is not recognized as an internal or external command`

**Soluções:**
- Verifique se o Python está instalado: `python --version`
- Adicione o Python ao PATH do sistema
- Use `python3` ao invés de `python`
- Reinstale o Python pelo Microsoft Store (Windows)
</details>

<details>
<summary><b>🔐 Erro de Autenticação MongoDB</b></summary>

**Problema:** `bad auth: authentication failed`

**Soluções:**
- Verifique usuário e senha no arquivo `.env`
- Confirme se o IP está liberado no Network Access
- Teste a string de conexão no MongoDB Compass
</details>

<details>
<summary><b>🌐 Erro 404 - Page Not Found</b></summary>

**Problema:** Endpoint não encontrado

**Soluções:**
- Verifique se a API está rodando (`python app.py`)
- Confirme a URL: `http://127.0.0.1:5000/`
- Verifique se o método HTTP está correto
</details>

<details>
<summary><b>💥 Erro 500 - Internal Server Error</b></summary>

**Problema:** Erro interno do servidor

**Soluções:**
- Veja o traceback no terminal onde a API roda
- Verifique se todas as variáveis de ambiente estão configuradas
- Confirme se o MongoDB Atlas está ativo
</details>

<details>
<summary><b>📊 Documentos não aparecem</b></summary>

**Problema:** Consultas retornam vazio

**Soluções:**
- Verifique se o POST retornou status 201
- Confirme nomes do banco e coleção no `.env`
- Use MongoDB Compass para verificar os dados
- Verifique se os campos existem nos documentos
</details>

---

## 📁 Estrutura do Projeto

```
api-documentos-mongodb/
├── app.py              # Código principal da API
├── .env                # Variáveis de ambiente
├── requirements.txt    # Dependências (opcional)
├── README.md          # Este arquivo
└── venv/              # Ambiente virtual (não versionar)
```

---

## 📦 Dependências

```txt
Flask==2.3.3
pymongo==4.5.0
python-dotenv==1.0.0
```

---

## 🔒 Segurança

- ✅ **Variáveis de ambiente** para credenciais sensíveis
- ✅ **Validação de entrada** nos endpoints
- ✅ **Tratamento de erros** robusto
- ✅ **Sanitização de ObjectId** para prevenir injeção

> ⚠️ **Aviso:** Esta API é para fins de desenvolvimento. Para produção, implemente autenticação, rate limiting e HTTPS.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`
4. Push para a branch: `git push origin feature/nova-funcionalidade`
5. Abrir um Pull Request

---

## 📝 Licença

Este projeto está sob a licença De Igor Sebastian. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Agradecimentos

- **Flask** - Framework web minimalista
- **MongoDB Atlas** - Banco de dados em nuvem
- **PyMongo** - Driver oficial do MongoDB para Python

---

<div align="center">

**Feito com ❤️ e ☕**

[⬆ Voltar ao topo](#-api-de-documentos---flask--mongodb-atlas)

</div>
