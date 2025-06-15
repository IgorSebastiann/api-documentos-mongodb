from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId # Importar ObjectId para lidar com IDs do MongoDB
from dotenv import load_dotenv # Para carregar variáveis do .env
import os # Para acessar variáveis de ambiente

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# --- CONFIGURAÇÃO DO MONGODB ATLAS ---
# Obtém a URI de conexão, o nome do banco e da coleção das variáveis de ambiente
MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGODB_DB_NAME")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")

# Verifica se a URI foi carregada
if not MONGO_URI:
    raise ValueError("MONGODB_URI não configurado no arquivo .env ou ambiente. Por favor, adicione sua string de conexão do Atlas.")
if not DB_NAME:
    raise ValueError("MONGODB_DB_NAME não configurado no arquivo .env. Por favor, adicione o nome do seu banco de dados.")
if not COLLECTION_NAME:
    raise ValueError("MONGODB_COLLECTION_NAME não configurado no arquivo .env. Por favor, adicione o nome da sua coleção.")

# Conecta ao MongoDB Atlas
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
        data = request.get_json() # Tenta obter o JSON do corpo da requisição
        if not data:
            return jsonify({"erro": "Requisição inválida. Envie um JSON no corpo da requisição."}), 400

        # O MongoDB gera automaticamente um _id único se você não fornecer um.
        result = collection.insert_one(data)
        return jsonify({
            "mensagem": "Documento cadastrado com sucesso!",
            "id_inserido": str(result.inserted_id) # Converte ObjectId para string para JSON
        }), 201 # 201 Created

    except Exception as e:
        # Captura qualquer erro inesperado e retorna uma mensagem de erro
        return jsonify({"erro": f"Erro ao cadastrar documento: {str(e)}"}), 500 # 500 Internal Server Error

@app.route('/pesquisar_nome', methods=['GET'])
def pesquisar_nome():
    """
    Recebe 'nome' como parâmetro na URL e retorna documentos que contenham esse nome.
    Ex: /pesquisar_nome?nome=Ana
    """
    nome = request.args.get('nome') # Obtém o valor do parâmetro 'nome' da URL
    if not nome:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório na URL."}), 400

    try:
        # Pesquisa no campo 'nome' do seu documento
        documentos = list(collection.find({"nome": {"$regex": nome, "$options": "i"}}))

        # Converte ObjectId para string para poder serializar em JSON
        for doc in documentos:
            doc['_id'] = str(doc['_id'])

        if documentos:
            return jsonify(documentos), 200 # 200 OK
        else:
            return jsonify({"mensagem": "Nenhum documento encontrado com o nome fornecido."}), 404 # 404 Not Found

    except Exception as e:
        return jsonify({"erro": f"Erro ao pesquisar por nome: {str(e)}"}), 500

@app.route('/pesquisar_rua', methods=['GET'])
def pesquisar_rua():
    """
    Recebe 'rua' como parâmetro na URL e retorna documentos que contenham essa rua.
    Ex: /pesquisar_rua?rua=Acacias
    """
    rua = request.args.get('rua')
    if not rua:
        return jsonify({"erro": "Parâmetro 'rua' é obrigatório na URL."}), 400

    try:
        # Pesquisa no campo 'endereco.rua' do seu documento
        # IMPORTANTE: Garanta que seus documentos tenham um campo 'rua' dentro do subdocumento 'endereco'.
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
    Ex: /pesquisar_compras?produto=Livro
    """
    produto = request.args.get('produto')
    if not produto:
        return jsonify({"erro": "Parâmetro 'produto' é obrigatório na URL."}), 400

    try:
        # Pesquisa no campo 'historico_compras.descricao' do seu documento
        documentos = list(collection.find({"historico_compras.descricao": {"$regex": produto, "$options": "i"}}))
        for doc in documentos:
            doc['_id'] = str(doc['_id'])

        if documentos:
            return jsonify(documentos), 200
        else:
            return jsonify({"mensagem": "Nenhum documento encontrado com o produto fornecido."}), 404
    except Exception as e:
        return jsonify({"erro": f"Erro ao pesquisar por produto: {str(e)}"}), 500

    # Novo endpoint para deletar um documento
@app.route('/deletar/<string:document_id>', methods=['DELETE'])
def deletar_documento(document_id):
        """
        Deleta um documento do MongoDB com base no seu _id.
        O _id é passado como parte da URL.
        Ex: DELETE /deletar/60c... (o ID que você obteve ao cadastrar)
        """
        try:
            # Tenta converter o ID da string para um ObjectId do MongoDB
            # Isso é crucial porque o _id no MongoDB é um ObjectId, não uma string simples
            object_id = ObjectId(document_id)
        except Exception:
            # Se o ID não for um ObjectId válido, retorna erro 400
            return jsonify({"erro": "ID de documento inválido."}), 400

        try:
            # Tenta deletar o documento usando o ObjectId
            result = collection.delete_one({"_id": object_id})

            if result.deleted_count == 1:
                return jsonify({"mensagem": f"Documento com ID {document_id} deletado com sucesso!"}), 200
            else:
                return jsonify({"mensagem": "Nenhum documento encontrado com o ID fornecido para exclusão."}), 404

        except Exception as e:
            return jsonify({"erro": f"Erro ao deletar documento: {str(e)}"}), 500

# Garante que o servidor Flask rode apenas quando o script é executado diretamente
if __name__ == '__main__':
    # debug=True: o servidor reinicia automaticamente a cada alteração no código.
    # Não use debug=True em produção!
    app.run(debug=True, port=5000) # Opcional: defina uma porta diferente, se 5000 estiver ocupada