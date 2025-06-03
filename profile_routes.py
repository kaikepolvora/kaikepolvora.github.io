# /home/ubuntu/PixelExploraBackend/src/routes/profile_routes.py

from flask import Blueprint, jsonify, request

profile_bp = Blueprint("profile_bp", __name__)

# Dados mockados para simular um banco de dados
# Em uma aplicação real, isso viria de um banco de dados e usaria os models definidos
mock_profiles = {
    1: {"user_id": 1, "full_name": "Alice Wonder", "bio": "Jornalista investigativa com foco em tecnologia.", "photo_url": "/static/images/alice.jpg", "status": "active", "public_email": "alice@example.com", "social_links": {"twitter": "@alicew"}},
    2: {"user_id": 2, "full_name": "Bob The Builder", "bio": "Especialista em hardware e reviews de gadgets.", "photo_url": "/static/images/bob.jpg", "status": "active", "public_email": "bob@example.com", "social_links": {"linkedin": "/in/bobthebuilder"}}
}
next_profile_id = 3

@profile_bp.route("/", methods=["GET"])
def get_all_profiles():
    """Retorna todos os perfis de jornalistas."""
    return jsonify(list(mock_profiles.values())), 200

@profile_bp.route("/<int:user_id>", methods=["GET"])
def get_profile(user_id):
    """Retorna o perfil de um jornalista específico."""
    profile = mock_profiles.get(user_id)
    if profile:
        return jsonify(profile), 200
    return jsonify(message="Perfil não encontrado."), 404

@profile_bp.route("/<int:user_id>", methods=["PUT"])
def update_profile(user_id):
    """Atualiza o perfil de um jornalista. (Simulado)"""
    if user_id not in mock_profiles:
        return jsonify(message="Perfil não encontrado para atualização."), 404
    
    data = request.get_json()
    if not data:
        return jsonify(message="Dados não fornecidos."), 400

    # Atualiza os campos permitidos
    profile = mock_profiles[user_id]
    profile["full_name"] = data.get("full_name", profile["full_name"])
    profile["bio"] = data.get("bio", profile["bio"])
    profile["photo_url"] = data.get("photo_url", profile["photo_url"])
    profile["status"] = data.get("status", profile["status"])
    profile["public_email"] = data.get("public_email", profile["public_email"])
    profile["social_links"] = data.get("social_links", profile["social_links"])
    
    # Em um cenário real, você validaria os dados e salvaria no banco
    # mock_profiles[user_id].update(data) # Cuidado com a atualização direta sem validação
    
    return jsonify(message="Perfil atualizado com sucesso!", profile=profile), 200

# Outras rotas como POST para criar novos perfis (associados a novos usuários)
# e DELETE podem ser adicionadas aqui.
# A criação de perfil geralmente estaria atrelada à criação de um usuário jornalista.

# Exemplo de rota para criar um perfil (simplificado, sem criação de usuário associado)
@profile_bp.route("/", methods=["POST"])
def create_profile():
    """Cria um novo perfil de jornalista (simulado)."""
    global next_profile_id
    data = request.get_json()
    if not data or not data.get("full_name") or not data.get("user_id"):
        return jsonify(message="Dados incompletos para criar perfil."), 400
    
    user_id = data["user_id"]
    if user_id in mock_profiles:
        return jsonify(message=f"Perfil para user_id {user_id} já existe."), 409 # Conflict

    new_profile = {
        "user_id": user_id,
        "full_name": data["full_name"],
        "bio": data.get("bio", ""),
        "photo_url": data.get("photo_url", ""),
        "status": data.get("status", "active"),
        "public_email": data.get("public_email"),
        "social_links": data.get("social_links", {})
    }
    mock_profiles[user_id] = new_profile
    # next_profile_id += 1 # Se user_id não fosse o ID principal do mock_profiles
    return jsonify(message="Perfil criado com sucesso!", profile=new_profile), 201

