# /home/ubuntu/PixelExploraBackend/src/main.py

import os
from flask import Flask, jsonify
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)

# Configurações do aplicativo (exemplo)
# app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your_default_secret_key")
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///pixelexplora.db")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Aqui você inicializaria extensões como SQLAlchemy, Migrate, LoginManager, etc.
# Exemplo:
# from .models import db # Supondo que db está definido em models.py
# db.init_app(app)

# Rotas de exemplo
@app.route("/")
def home():
    return jsonify(message="Bem-vindo à API do PixelExplora Backend!")

@app.route("/api/health")
def health_check():
    return jsonify(status="ok", message="API está funcionando.")

# Importar e registrar blueprints para rotas
# Correção: Usar imports relativos, pois main.py está dentro do pacote 'src'
from .routes.profile_routes import profile_bp
from .routes.post_routes import post_bp
from .routes.analytics_routes import analytics_bp
# from .routes.auth_routes import auth_bp # Auth routes não foram criadas ainda nesta fase

app.register_blueprint(profile_bp, url_prefix="/api/profiles")
app.register_blueprint(post_bp, url_prefix="/api/posts")
app.register_blueprint(analytics_bp, url_prefix="/api/analytics")
# app.register_blueprint(auth_bp, url_prefix="/api/auth")

if __name__ == "__main__":
    # Para executar diretamente o main.py de dentro do diretório src, 
    # o Python pode ter problemas com imports relativos de pacotes irmãos ou pais
    # se o diretório pai (PixelExploraBackend) não estiver no PYTHONPATH.
    # A execução via `python -m src.main` (a partir do diretório PixelExploraBackend)
    # geralmente lida melhor com isso. No entanto, a correção acima com imports relativos
    # deve funcionar se o script for executado como parte do pacote src.
    app.run(host="0.0.0.0", port=5000, debug=True)

