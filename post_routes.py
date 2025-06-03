# /home/ubuntu/PixelExploraBackend/src/routes/post_routes.py

from flask import Blueprint, jsonify, request
from datetime import datetime

post_bp = Blueprint("post_bp", __name__)

# Dados mockados para simular um banco de dados de postagens
# Em uma aplicação real, isso viria de um banco de dados e usaria os models definidos
mock_posts = {
    1: {
        "id": 1, "title": "Primeira Postagem sobre IA", "content": "Conteúdo detalhado sobre IA...", 
        "author_id": 1, "category": "Tecnologia", "tags": ["IA", "Machine Learning"], 
        "status": "published", "created_at": datetime.utcnow().isoformat(), 
        "updated_at": datetime.utcnow().isoformat(), "published_at": datetime.utcnow().isoformat(),
        "featured_image_url": "/static/images/ia_post.jpg", "youtube_video_id": "dQw4w9WgXcQ",
        "view_count": 150
    },
    2: {
        "id": 2, "title": "Review do Novo Jogo X", "content": "Análise completa do jogo X...", 
        "author_id": 2, "category": "Jogos", "tags": ["Review", "RPG"], 
        "status": "draft", "created_at": datetime.utcnow().isoformat(), 
        "updated_at": datetime.utcnow().isoformat(), "published_at": None,
        "featured_image_url": "/static/images/jogo_x.jpg", "youtube_video_id": "",
        "view_count": 0
    }
}
next_post_id = 3

@post_bp.route("/", methods=["GET"])
def get_all_posts():
    """Retorna todas as postagens."""
    # Adicionar filtros no futuro, ex: ?status=published&category=Tecnologia
    return jsonify(list(mock_posts.values())), 200

@post_bp.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
    """Retorna uma postagem específica."""
    post = mock_posts.get(post_id)
    if post:
        return jsonify(post), 200
    return jsonify(message="Postagem não encontrada."), 404

@post_bp.route("/", methods=["POST"])
def create_post():
    """Cria uma nova postagem (simulado)."""
    global next_post_id
    data = request.get_json()
    if not data or not data.get("title") or not data.get("content") or not data.get("author_id") or not data.get("category"):
        return jsonify(message="Dados incompletos para criar postagem."), 400

    new_post = {
        "id": next_post_id,
        "title": data["title"],
        "content": data["content"],
        "author_id": data["author_id"],
        "category": data["category"],
        "tags": data.get("tags", []),
        "status": data.get("status", "draft"),
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat(),
        "published_at": datetime.utcnow().isoformat() if data.get("status") == "published" else None,
        "featured_image_url": data.get("featured_image_url", ""),
        "youtube_video_id": data.get("youtube_video_id", ""),
        "view_count": 0
    }
    mock_posts[next_post_id] = new_post
    next_post_id += 1
    return jsonify(message="Postagem criada com sucesso!", post=new_post), 201

@post_bp.route("/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    """Atualiza uma postagem existente (simulado)."""
    if post_id not in mock_posts:
        return jsonify(message="Postagem não encontrada para atualização."), 404
    
    data = request.get_json()
    if not data:
        return jsonify(message="Dados não fornecidos."), 400

    post = mock_posts[post_id]
    post["title"] = data.get("title", post["title"])
    post["content"] = data.get("content", post["content"])
    post["category"] = data.get("category", post["category"])
    post["tags"] = data.get("tags", post["tags"])
    post["status"] = data.get("status", post["status"])
    post["featured_image_url"] = data.get("featured_image_url", post["featured_image_url"])
    post["youtube_video_id"] = data.get("youtube_video_id", post["youtube_video_id"])
    post["updated_at"] = datetime.utcnow().isoformat()

    if "status" in data and data["status"] == "published" and not post["published_at"]:
        post["published_at"] = datetime.utcnow().isoformat()
    elif "status" in data and data["status"] != "published":
        post["published_at"] = None # Se mudar de publicado para rascunho, por exemplo
        
    return jsonify(message="Postagem atualizada com sucesso!", post=post), 200

@post_bp.route("/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    """Exclui uma postagem (simulado)."""
    if post_id in mock_posts:
        deleted_post = mock_posts.pop(post_id)
        return jsonify(message="Postagem excluída com sucesso!", post=deleted_post), 200
    return jsonify(message="Postagem não encontrada para exclusão."), 404

