# 📋 API de Documentos com MongoDB

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-Latest-brightgreen.svg)](https://mongodb.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> API REST moderna para gerenciamento de documentos usando FastAPI e MongoDB

## 🚀 Quick Start

\```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/api-documentos-mongodb.git
cd api-documentos-mongodb

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env

# Execute a API
python app/main.py
\```

**🎯 Acesse:** http://localhost:8000/docs

## ✨ Funcionalidades

- ✅ **Cadastro de documentos** com validação automática
- 🔍 **Pesquisa por nome** (busca parcial, case-insensitive)
- 🏠 **Pesquisa por endereço** (nome da rua)
- 🛒 **Pesquisa por produtos** comprados
- 📊 **Documentação automática** com Swagger UI
- 🍃 **MongoDB** como banco de dados
- ⚡ **Async/Await** para alta performance

## 🛠️ Stack Tecnológica

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.8+ | Linguagem principal |
| **FastAPI** | 0.104+ | Framework web |
| **MongoDB** | Latest | Banco de dados |
| **Motor** | 3.3+ | Driver async MongoDB |
| **Pydantic** | 2.5+ | Validação de dados |

## 📋 Endpoints da API

### POST `/api/cadastrar`
Cadastra um novo documento

\```json
{
  "nome": "João Silva",
  "rua": "Rua das Flores",
  "numero": "123", 
  "cidade": "São Paulo",
  "cep": "01234-567",
  "produtos_comprados": ["Notebook", "Mouse", "Teclado"]
}
\```

### GET `/api/pesquisar_nome?nome={nome}`
Pesquisa documentos por nome

### GET `/api/pesquisar_rua?rua={rua}`  
Pesquisa documentos por nome da rua

### GET `/api/pesquisar_compras?produto={produto}`
Pesquisa documentos por produto comprado

### GET `/api/listar_todos`
Lista todos os documentos cadastrados

## 🔧 Configuração

### MongoDB Local
\```bash
# Instalar MongoDB
# Windows: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
# macOS: brew install mongodb-community
# Linux: https://docs.mongodb.com/manual/administration/install-on-linux/

# Iniciar MongoDB
mongod
\```

### MongoDB Atlas (Cloud)
1. Crie conta gratuita: https://www.mongodb.com/atlas
2. Crie cluster gratuito
3. Configure usuário e senha
4. Obtenha string de conexão
5. Configure no `.env`

### Docker (Mais Fácil)
\```bash
docker-compose up -d
\```

## 🧪 Testando

\```bash
# Instalar dependências de teste
pip install pytest httpx

# Executar testes
python -m pytest tests/

# Teste manual
python tests/test_api.py
\```

## 📖 Documentação Completa

- 📖 [Guia de Setup](docs/SETUP.md)
- 🔧 [Documentação da API](docs/API_GUIDE.md)
- 🚀 [Guia de Deploy](docs/DEPLOYMENT.md)
- 🤝 [Como Contribuir](docs/CONTRIBUTING.md)

## 🎯 Para a Apresentação

### Demonstração Sugerida:
1. **Mostrar documentação automática** (`/docs`)
2. **Cadastrar documentos** via interface Swagger
3. **Demonstrar todas as pesquisas**
4. **Mostrar persistência** dos dados
5. **Explicar arquitetura** MongoDB + FastAPI

### Pontos Fortes:
- 🔥 **Performance**: Async/await + MongoDB
- 📱 **Documentação**: Auto-gerada e interativa
- 🔍 **Busca flexível**: Case-insensitive em todos os campos
- 🏗️ **Arquitetura**: Modular e escalável
- 🛡️ **Validação**: Automática com Pydantic

## 👥 Desenvolvido por

- **Seu Nome** - [@seu_github](https://github.com/seu_usuario)
- **Nome do Parceiro** - [@parceiro_github](https://github.com/parceiro_usuario)

> 🎓 **Projeto da disciplina de Banco de Dados**

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

---

⭐ **Se este projeto foi útil, deixe uma estrela!**
\```

## 📋 docs/SETUP.md

\```markdown
# 🛠️ Guia de Setup Completo

## 📋 Pré-requisitos

- Python 3.8 ou superior
- MongoDB (local, Atlas ou Docker)
- Git
- PyCharm (recomendado)

## 🔧 Configuração Passo a Passo

### 1. Clone o Repositório
\