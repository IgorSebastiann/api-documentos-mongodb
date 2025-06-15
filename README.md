# 📚 API de Documentos com Flask e MongoDB Atlas

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

*Uma API RESTful simples e poderosa desenvolvida em Python com Flask para interagir com MongoDB Atlas na nuvem*

</div>

---

## 🚀 Funcionalidades

A API oferece um conjunto completo de endpoints para gerenciamento de documentos:

| Endpoint | Método | Descrição | Exemplo |
|----------|--------|-----------|---------|
| `/` | `GET` | 🏠 Verificar status da API | - |
| `/cadastrar` | `POST` | ➕ Cadastrar novo documento | `{"nome": "João", "email": "..."}` |
| `/pesquisar_nome` | `GET` | 🔍 Buscar por nome | `?nome=Ana` |
| `/pesquisar_rua` | `GET` | 📍 Buscar por endereço | `?rua=Acacias` |
| `/pesquisar_compras` | `GET` | 🛒 Buscar por produtos | `?produto=Livro` |
| `/deletar/{id}` | `DELETE` | 🗑️ Deletar documento | - |

> **💡 Dica:** Todas as pesquisas são **case-insensitive** e suportam busca parcial!

---

## 📋 Pré-requisitos

Antes de começar, você precisará ter:

### 🐍 Python
- **Versão:** Python 3.8 ou superior
- **Verificação:** `python --version` ou `python3 --version`
- **Windows:** Configure os "Aliases de execução do aplicativo" ou instale via Microsoft Store

### 🍃 MongoDB Atlas
- ✅ Conta no MongoDB Atlas
- ✅ Cluster configurado (M0 Sandbox gratuito é suficiente)
- ✅ Usuário do banco com credenciais
- ✅ Acesso de rede configurado para seu IP

### 🔧 Ferramentas de Teste
Escolha uma das opções:
- [📱 Insomnia](https://insomnia.rest/download) (Recomendado)
- [📮 Postman](https://www.postman.com/downloads/)

---

## ⚙️ Configuração e Instalação

### 1️⃣ Preparar o Ambiente

```bash
# Criar pasta do projeto
mkdir meu_projeto_api
cd meu_projeto_api
```

### 2️⃣ Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows (CMD/PowerShell):
.\venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

> **✅ Sucesso:** Você verá `(venv)` no início da linha de comando

### 3️⃣ Instalar Dependências

```bash
pip install Flask pymongo python-dotenv
```

### 4️⃣ Configurar MongoDB Atlas

1. 🌐 Acesse seu [painel do MongoDB Atlas](https://cloud.mongodb.com/)
2. 📊 Vá para **Database** (ou Clusters)
3. 🔗 No seu cluster, clique em **Connect**
4. 🐍 Escolha **Connect your application** > **Python**
5. 📋 Copie a string de conexão:

```
mongodb+srv://IgorSebastiann:<db_password>@cluster0.nzglgwc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
```

> **⚠️ Importante:** Substitua `<db_password>` pela senha real!

### 5️⃣ Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
MONGODB_URI="mongodb+srv://IgorSebastiann:SUA_SENHA_REAL@cluster0.nzglgwc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGODB_DB_NAME="trabalho_final_db"
MONGODB_COLLECTION_NAME="clientes_geral"
```

### 6️⃣ Criar o Arquivo Principal

Crie o arquivo `app.py` com o código da API (código fornecido no documento original).

---

## ▶️ Executando a API

1. **🔄 Verifique se seu cluster MongoDB Atlas está ativo**
2. **🚀 Execute a aplicação:**

```bash
python app.py
```

3. **✅ Você verá:**

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

> **🎉 Pronto!** Sua API está rodando em `http://127.0.0.1:5000`

---

## 🧪 Como Testar com Insomnia

### 📝 Estrutura de Documento de Exemplo

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

### 🎯 Cenários de Teste

<details>
<summary><strong>1️⃣ Testar Status da API</strong></summary>

- **Método:** `GET`
- **URL:** `http://127.0.0.1:5000/`
- **Esperado:** `200 OK` + mensagem de boas-vindas

</details>

<details>
<summary><strong>2️⃣ Cadastrar Documento</strong></summary>

- **Método:** `POST`
- **URL:** `http://127.0.0.1:5000/cadastrar`
- **Body:** JSON (exemplo acima)
- **Esperado:** `201 Created` + ID do documento

</details>

<details>
<summary><strong>3️⃣ Pesquisar por Nome</strong></summary>

- **Método:** `GET`
- **URL:** `http://127.0.0.1:5000/pesquisar_nome?nome=Ana`
- **Esperado:** Lista de documentos ou `404` se não encontrar

</details>

<details>
<summary><strong>4️⃣ Pesquisar por Rua</strong></summary>

- **Método:** `GET`
- **URL:** `http://127.0.0.1:5000/pesquisar_rua?rua=Acacias`
- **Esperado:** Documentos com endereços correspondentes

</details>

<details>
<summary><strong>5️⃣ Pesquisar por Produto</strong></summary>

- **Método:** `GET`
- **URL:** `http://127.0.0.1:5000/pesquisar_compras?produto=Livro`
- **Esperado:** Documentos com histórico de compras correspondente

</details>

<details>
<summary><strong>6️⃣ Deletar Documento</strong></summary>

- **Método:** `DELETE`
- **URL:** `http://127.0.0.1:5000/deletar/{ID_DO_DOCUMENTO}`
- **Esperado:** `200 OK` + confirmação de exclusão

</details>

---

## 🔧 Solução de Problemas

<details>
<summary><strong>🚨 Problemas Comuns e Soluções</strong></summary>

### 🐍 Python não encontrado
- Verifique a instalação do Python
- Configure o PATH do sistema
- Use `python3` em vez de `python`

### 🔐 Erro de Autenticação (`bad auth`)
- ✅ Verifique usuário e senha no `.env`
- ✅ Confirme se seu IP está na whitelist do Atlas
- ✅ Teste a conexão no MongoDB Compass

### 🌐 Page Not Found (404)
- ✅ Verifique se todas as rotas estão definidas
- ✅ Confirme se a função `home()` existe
- ✅ Reinicie a aplicação

### 💥 Internal Server Error (500)
- 📊 Olhe o terminal para ver o traceback
- 🔍 Verifique as variáveis de ambiente
- 🔧 Confirme a conexão com o banco

### 📊 Documentos não aparecem
- ✅ Confirme se o POST retornou `201 Created`
- ✅ Verifique os nomes do banco e coleção (case-sensitive)
- 🔍 Use o MongoDB Compass para visualizar os dados

</details>

---

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Você pode:

- 🐛 Reportar bugs
- 💡 Sugerir novas funcionalidades
- 🔧 Melhorar o código
- 📚 Aprimorar a documentação

### 💻 Para Desenvolvedores

```bash
# Fork o projeto
git clone https://github.com/seu-usuario/api-documentos-mongodb.git
cd api-documentos-mongodb

# Crie uma branch para sua feature
git checkout -b feature/nova-funcionalidade

# Faça suas alterações e commit
git commit -m "Adiciona nova funcionalidade"

# Push e abra um Pull Request
git push origin feature/nova-funcionalidade
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 📞 Suporte

Encontrou algum problema?

- 📧 **Email:** seuemail@example.com
- 💬 **Issues:** [Abra uma issue](https://github.com/seu-usuario/repo/issues)
- 📚 **Documentação:** [MongoDB Atlas Docs](https://docs.atlas.mongodb.com/)

---

<div align="center">

**⭐ Se este projeto te ajudou, considere dar uma estrela!**

*Desenvolvido com ❤️ usando Flask e MongoDB Atlas*

</div>
