# ===============================
# app/database.py
# ===============================
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()


class Database:
    client: AsyncIOMotorClient = None
    database = None


# Configuração da conexão MongoDB
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "documentos_db")


async def connect_to_mongo():
    """Conecta ao MongoDB"""
    Database.client = AsyncIOMotorClient(MONGODB_URL)
    Database.database = Database.client[DATABASE_NAME]
    print(f"🍃 Conectado ao MongoDB: {DATABASE_NAME}")


async def close_mongo_connection():
    """Fecha conexão com MongoDB"""
    if Database.client:
        Database.client.close()
        print("🔌 Conexão MongoDB fechada")


def get_database():
    """Retorna instância do banco de dados"""
    return Database.database


# ===============================
# app/models.py
# ===============================
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class DocumentoCreate(BaseModel):
    """Modelo para criação de documento"""
    nome: str = Field(..., min_length=1, max_length=100)
    rua: str = Field(..., min_length=1, max_length=200)
    numero: Optional[str] = Field(None, max_length=20)
    cidade: Optional[str] = Field(None, max_length=100)
    cep: Optional[str] = Field(None, max_length=20)
    produtos_comprados: List[str] = Field(..., min_items=1)

    class Config:
        schema_extra = {
            "example": {
                "nome": "João Silva",
                "rua": "Rua das Flores",
                "numero": "123",
                "cidade": "São Paulo",
                "cep": "01234-567",
                "produtos_comprados": ["Notebook", "Mouse", "Teclado"]
            }
        }


class DocumentoResponse(BaseModel):
    """Modelo para resposta de documento"""
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    nome: str
    rua: str
    numero: Optional[str]
    cidade: Optional[str]
    cep: Optional[str]
    produtos_comprados: List[str]
    data_cadastro: datetime

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "nome": "João Silva",
                "rua": "Rua das Flores",
                "numero": "123",
                "cidade": "São Paulo",
                "cep": "01234-567",
                "produtos_comprados": ["Notebook", "Mouse", "Teclado"],
                "data_cadastro": "2025-06-15T10:30:00"
            }
        }


# ===============================
# app/routers/documents.py
# ===============================
from fastapi import APIRouter, HTTPException, Query
from typing import List
import re
from datetime import datetime
from app.database import get_database
from app.models import DocumentoCreate, DocumentoResponse

router = APIRouter(prefix="/api", tags=["documentos"])


@router.post("/cadastrar", response_model=dict)
async def cadastrar_documento(documento: DocumentoCreate):
    """Cadastra um novo documento no MongoDB"""
    try:
        db = get_database()
        collection = db.documentos

        # Preparar documento para inserção
        doc_dict = documento.dict()
        doc_dict["data_cadastro"] = datetime.now()

        # Inserir no MongoDB
        result = await collection.insert_one(doc_dict)

        if result.inserted_id:
            return {
                "message": "Documento cadastrado com sucesso!",
                "id": str(result.inserted_id),
                "data_cadastro": doc_dict["data_cadastro"].isoformat()
            }
        else:
            raise HTTPException(status_code=500, detail="Erro ao inserir documento")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar documento: {str(e)}")


@router.get("/pesquisar_nome", response_model=List[DocumentoResponse])
async def pesquisar_por_nome(nome: str = Query(..., min_length=1, description="Nome para pesquisa")):
    """Pesquisa documentos por nome (busca parcial, case-insensitive)"""
    try:
        db = get_database()
        collection = db.documentos

        # Query MongoDB com regex para busca case-insensitive
        query = {"nome": {"$regex": re.escape(nome), "$options": "i"}}
        cursor = collection.find(query)

        documentos = []
        async for doc in cursor:
            doc["id"] = doc["_id"]
            documentos.append(DocumentoResponse(**doc))

        return documentos

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao pesquisar por nome: {str(e)}")


@router.get("/pesquisar_rua", response_model=List[DocumentoResponse])
async def pesquisar_por_rua(rua: str = Query(..., min_length=1, description="Nome da rua para pesquisa")):
    """Pesquisa documentos por nome da rua (busca parcial, case-insensitive)"""
    try:
        db = get_database()
        collection = db.documentos

        # Query MongoDB com regex
        query = {"rua": {"$regex": re.escape(rua), "$options": "i"}}
        cursor = collection.find(query)

        documentos = []
        async for doc in cursor:
            doc["id"] = doc["_id"]
            documentos.append(DocumentoResponse(**doc))

        return documentos

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao pesquisar por rua: {str(e)}")


@router.get("/pesquisar_compras", response_model=List[DocumentoResponse])
async def pesquisar_por_compras(produto: str = Query(..., min_length=1, description="Produto para pesquisa")):
    """Pesquisa documentos por produto comprado (busca parcial, case-insensitive)"""
    try:
        db = get_database()
        collection = db.documentos

        # Query MongoDB para buscar em array
        query = {"produtos_comprados": {"$regex": re.escape(produto), "$options": "i"}}
        cursor = collection.find(query)

        documentos = []
        async for doc in cursor:
            doc["id"] = doc["_id"]
            documentos.append(DocumentoResponse(**doc))

        return documentos

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao pesquisar por produto: {str(e)}")


@router.get("/listar_todos", response_model=List[DocumentoResponse])
async def listar_todos_documentos():
    """Lista todos os documentos cadastrados"""
    try:
        db = get_database()
        collection = db.documentos

        cursor = collection.find({}).sort("data_cadastro", -1)

        documentos = []
        async for doc in cursor:
            doc["id"] = doc["_id"]
            documentos.append(DocumentoResponse(**doc))

        return documentos

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar documentos: {str(e)}")


# ===============================
# app/main.py
# ===============================
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv

from app.database import connect_to_mongo, close_mongo_connection
from app.routers import documents

# Carregar variáveis de ambiente
load_dotenv()

# Configurar FastAPI
app = FastAPI(
    title="📋 API de Documentos",
    description="API REST para gerenciar documentos com MongoDB",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(documents.router)


# Eventos de inicialização e encerramento
@app.on_event("startup")
async def startup_event():
    """Conecta ao MongoDB na inicialização"""
    await connect_to_mongo()
    print("🚀 API iniciada com sucesso!")


@app.on_event("shutdown")
async def shutdown_event():
    """Fecha conexão MongoDB no encerramento"""
    await close_mongo_connection()
    print("👋 API encerrada")


@app.get("/")
async def root():
    """Endpoint raiz com informações da API"""
    return {
        "message": "📋 API de Documentos v2.0",
        "description": "API REST para gerenciar documentos com MongoDB",
        "endpoints": {
            "POST /api/cadastrar": "Cadastra um novo documento",
            "GET /api/pesquisar_nome?nome=<nome>": "Pesquisa por nome",
            "GET /api/pesquisar_rua?rua=<rua>": "Pesquisa por nome da rua",
            "GET /api/pesquisar_compras?produto=<produto>": "Pesquisa por produto comprado",
            "GET /api/listar_todos": "Lista todos os documentos"
        },
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
async def health_check():
    """Endpoint para verificar saúde da API"""
    return {"status": "healthy", "database": "MongoDB", "version": "2.0.0"}


if __name__ == "__main__":
    # Configurações do servidor
    HOST = os.getenv("API_HOST", "0.0.0.0")
    PORT = int(os.getenv("API_PORT", 8000))
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    print(f"🚀 Iniciando API de Documentos...")
    print(f"📖 Documentação: http://{HOST}:{PORT}/docs")
    print(f"🔍 Teste a API: http://{HOST}:{PORT}")
    print(f"🍃 Banco: MongoDB")

    uvicorn.run(
        "app.main:app",
        host=HOST,
        port=PORT,
        reload=DEBUG,
        log_level="info"
    )

# ===============================
# tests/test_api.py
# ===============================
import asyncio
import httpx
import pytest
from app.main import app

BASE_URL = "http://localhost:8000"


@pytest.fixture
def client():
    with httpx.Client(app=app, base_url=BASE_URL) as client:
        yield client


def test_root_endpoint(client):
    """Testa endpoint raiz"""
    response = client.get("/")
    assert response.status_code == 200
    assert "API de Documentos" in response.json()["message"]


def test_health_endpoint(client):
    """Testa endpoint de saúde"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


async def test_cadastrar_documento():
    """Testa cadastro de documento"""
    async with httpx.AsyncClient(app=app, base_url=BASE_URL) as client:
        documento = {
            "nome": "João Silva",
            "rua": "Rua das Flores",
            "numero": "123",
            "cidade": "São Paulo",
            "cep": "01234-567",
            "produtos_comprados": ["Notebook", "Mouse", "Teclado"]
        }

        response = await client.post("/api/cadastrar", json=documento)
        assert response.status_code == 200
        assert "sucesso" in response.json()["message"]


if __name__ == "__main__":
    # Script de teste manual
    async def testar_api():
        async with httpx.AsyncClient(base_url=BASE_URL) as client:
            print("🧪 Testando API com MongoDB\n")

            # Testar cadastro
            documento = {
                "nome": "Maria Santos",
                "rua": "Avenida Brasil",
                "numero": "456",
                "cidade": "Rio de Janeiro",
                "cep": "12345-678",
                "produtos_comprados": ["Smartphone", "Fone", "Carregador"]
            }

            response = await client.post("/api/cadastrar", json=documento)
            print(f"Cadastro: {response.status_code} - {response.json()}")

            # Testar pesquisa
            response = await client.get("/api/pesquisar_nome?nome=Maria")
            print(f"Pesquisa nome: {len(response.json())} resultado(s)")

            response = await client.get("/api/listar_todos")
            print(f"Total documentos: {len(response.json())}")


    asyncio.run(testar_api())