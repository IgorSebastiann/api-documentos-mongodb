from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGODB_DB_NAME")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")

if not MONGO_URI or not DB_NAME or not COLLECTION_NAME:
    raise ValueError("Configure MONGODB_URI, MONGODB_DB_NAME e MONGODB_COLLECTION_NAME no .env")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# ------------------------
# MODELOS Pydantic
# ------------------------

class CadastroModel(BaseModel):
    nome: str
    email: str
    telefone: str
    data_nascimento: str
    endereco: dict
    ativo: bool
    tags: List[str]
    historico_compras: List[dict]

class NomeModel(BaseModel):
    nome: str

class RuaModel(BaseModel):
    rua: str

class ProdutoModel(BaseModel):
    produto: str

# ------------------------
# ENDPOINTS
# ------------------------

@app.get("/")
def home():
    return {"mensagem": "API de Documentos FastAPI - Teste /cadastrar, /pesquisar_nome, etc."}

@app.post("/cadastrar")
def cadastrar_documento(doc: CadastroModel):
    try:
        result = collection.insert_one(doc.dict())
        return {"mensagem": "Documento cadastrado com sucesso!", "id_inserido": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar: {str(e)}")

@app.post("/pesquisar_nome")
def pesquisar_nome(filtro: NomeModel):
    try:
        documentos = list(collection.find({"nome": {"$regex": filtro.nome, "$options": "i"}}))
        for doc in documentos:
            doc["_id"] = str(doc["_id"])
        return documentos if documentos else {"mensagem": "Nenhum documento encontrado."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na busca: {str(e)}")

@app.post("/pesquisar_rua")
def pesquisar_rua(filtro: RuaModel):
    try:
        documentos = list(collection.find({"endereco.rua": {"$regex": filtro.rua, "$options": "i"}}))
        for doc in documentos:
            doc["_id"] = str(doc["_id"])
        return documentos if documentos else {"mensagem": "Nenhum documento encontrado."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na busca: {str(e)}")

@app.post("/pesquisar_compras")
def pesquisar_compras(filtro: ProdutoModel):
    try:
        documentos = list(collection.find({"historico_compras.descricao": {"$regex": filtro.produto, "$options": "i"}}))
        for doc in documentos:
            doc["_id"] = str(doc["_id"])
        return documentos if documentos else {"mensagem": "Nenhum documento encontrado."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na busca: {str(e)}")

@app.delete("/deletar/{document_id}")
def deletar_documento(document_id: str):
    try:
        object_id = ObjectId(document_id)
    except Exception:
        raise HTTPException(status_code=400, detail="ID inválido.")

    try:
        result = collection.delete_one({"_id": object_id})
        if result.deleted_count == 1:
            return {"mensagem": f"Documento com ID {document_id} deletado com sucesso!"}
        else:
            raise HTTPException(status_code=404, detail="Documento não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar: {str(e)}")
