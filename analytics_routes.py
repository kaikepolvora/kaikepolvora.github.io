# /home/ubuntu/PixelExploraBackend/src/routes/analytics_routes.py

from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
import random

analytics_bp = Blueprint("analytics_bp", __name__)

# Mock data para simular métricas de analytics
# Em uma aplicação real, isso viria de um sistema de analytics ou banco de dados

# Simula visualizações diárias para os últimos 30 dias
def get_daily_views_mock():
    data = []
    today = datetime.utcnow()
    for i in range(30):
        date = today - timedelta(days=i)
        views = random.randint(50, 500) # Visualizações aleatórias
        data.append({"date": date.strftime("%Y-%m-%d"), "views": views})
    return sorted(data, key=lambda x: x["date"])

# Simula posts mais populares
def get_popular_posts_mock(limit=5):
    # Supondo que temos acesso aos mock_posts de post_routes (não diretamente aqui)
    # Para este exemplo, vamos criar alguns posts mockados aqui
    all_posts_titles = [
        "Primeira Postagem sobre IA", 
        "Review do Novo Jogo X", 
        "Tecnologias Emergentes em 2025", 
        "Guia Completo de Realidade Virtual",
        "Os Segredos do Desenvolvimento Web Moderno",
        "Curiosidades do Mundo Animal",
        "A História da Computação Gráfica"
    ]
    popular_posts = []
    # Seleciona 'limit' posts aleatórios e atribui visualizações
    selected_titles = random.sample(all_posts_titles, min(limit, len(all_posts_titles)))
    for i, title in enumerate(selected_titles):
        popular_posts.append({"id": i + 100, "title": title, "views": random.randint(1000, 5000)})
    return sorted(popular_posts, key=lambda x: x["views"], reverse=True)

@analytics_bp.route("/views/daily", methods=["GET"])
def daily_views_data():
    """Retorna dados de visualizações diárias (mock)."""
    return jsonify(get_daily_views_mock()), 200

@analytics_bp.route("/posts/popular", methods=["GET"])
def popular_posts_data():
    """Retorna os posts mais populares (mock)."""
    limit = request.args.get("limit", 5, type=int)
    return jsonify(get_popular_posts_mock(limit=limit)), 200

@analytics_bp.route("/summary", methods=["GET"])
def analytics_summary():
    """Retorna um resumo das métricas (mock)."""
    summary = {
        "total_posts": random.randint(50, 200),
        "total_views_last_30_days": sum(item["views"] for item in get_daily_views_mock()),
        "active_journalists": random.randint(5, 15),
        "comments_pending_moderation": random.randint(0, 20) # Exemplo de outra métrica
    }
    return jsonify(summary), 200

