# /home/ubuntu/PixelExploraBackend/src/models/user_models.py

from datetime import datetime

class User:
    def __init__(self, id, username, password_hash, email, role="journalist", created_at=None, updated_at=None):
        self.id = id
        self.username = username
        self.password_hash = password_hash # Store hashed passwords only
        self.email = email
        self.role = role  # e.g., "admin", "journalist"
        self.created_at = created_at if created_at else datetime.utcnow()
        self.updated_at = updated_at if updated_at else datetime.utcnow()

    def __repr__(self):
        return f"<User {self.username} ({self.role})>"

class JournalistProfile:
    def __init__(self, user_id, full_name, bio="", photo_url="", status="active", public_email=None, social_links=None):
        self.user_id = user_id # Foreign key to User.id
        self.full_name = full_name
        self.bio = bio
        self.photo_url = photo_url # URL to the profile picture
        self.status = status # e.g., "active", "on_leave"
        self.public_email = public_email
        self.social_links = social_links if social_links else {} # e.g., {"twitter": "url", "linkedin": "url"}
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<JournalistProfile for User ID {self.user_id}>"

# Exemplo de como isso seria usado (em um contexto de ORM ou banco de dados)
# db_users = {}
# db_profiles = {}

# def create_user(username, password, email, role="journalist"):
#     # Hash password before storing
#     hashed_password = "hashed_" + password # Placeholder for actual hashing
#     new_id = len(db_users) + 1
#     user = User(id=new_id, username=username, password_hash=hashed_password, email=email, role=role)
#     db_users[new_id] = user
#     if role == "journalist":
#         profile = JournalistProfile(user_id=new_id, full_name=username) # Default full_name to username
#         db_profiles[new_id] = profile
#     return user

