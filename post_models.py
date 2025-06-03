# /home/ubuntu/PixelExploraBackend/src/models/post_models.py

from datetime import datetime

class Post:
    def __init__(self, id, title, content, author_id, category, tags=None, status="draft", created_at=None, updated_at=None, published_at=None, featured_image_url="", youtube_video_id=""):
        self.id = id
        self.title = title
        self.content = content  # HTML or Markdown content
        self.author_id = author_id  # Foreign key to User.id (journalist)
        self.category = category # e.g., "Tecnologia", "Jogos", "Curiosidades"
        self.tags = tags if tags else [] # List of tags
        self.status = status  # e.g., "draft", "published", "archived"
        self.created_at = created_at if created_at else datetime.utcnow()
        self.updated_at = updated_at if updated_at else datetime.utcnow()
        self.published_at = published_at
        self.featured_image_url = featured_image_url
        self.youtube_video_id = youtube_video_id # For automatic video playback
        self.view_count = 0

    def __repr__(self):
        return f"<Post '{self.title}' by User ID {self.author_id}>"

    def publish(self):
        self.status = "published"
        self.published_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def unpublish(self):
        self.status = "draft"
        self.updated_at = datetime.utcnow()

    def increment_view_count(self):
        self.view_count += 1

class PostAnalytics:
    def __init__(self, post_id, date, views, unique_visitors=0, comments_count=0, shares_count=0):
        self.post_id = post_id # Foreign key to Post.id
        self.date = date # Date of the analytics record (e.g., YYYY-MM-DD)
        self.views = views
        self.unique_visitors = unique_visitors
        self.comments_count = comments_count
        self.shares_count = shares_count

    def __repr__(self):
        return f"<PostAnalytics for Post ID {self.post_id} on {self.date} - Views: {self.views}>"

# Placeholder for a simple in-memory store or database interaction
# db_posts = {}
# db_post_analytics = {}

# def create_post(title, content, author_id, category, tags=None, featured_image_url="", youtube_video_id=""):
#     new_id = len(db_posts) + 1
#     post = Post(id=new_id, title=title, content=content, author_id=author_id, category=category, tags=tags, featured_image_url=featured_image_url, youtube_video_id=youtube_video_id)
#     db_posts[new_id] = post
#     return post

# def record_daily_analytics(post_id, views, unique_visitors=0, comments=0, shares=0):
#     today = datetime.utcnow().strftime('%Y-%m-%d')
#     # In a real scenario, you'd likely update an existing record for the day or create a new one.
#     # This is a simplified example.
#     analytics_id = f"{post_id}_{today}"
#     if analytics_id in db_post_analytics:
#         db_post_analytics[analytics_id].views += views
#         db_post_analytics[analytics_id].unique_visitors += unique_visitors # Simplified aggregation
#         db_post_analytics[analytics_id].comments_count += comments
#         db_post_analytics[analytics_id].shares_count += shares
#     else:
#         analytics_entry = PostAnalytics(
#             post_id=post_id,
#             date=today,
#             views=views,
#             unique_visitors=unique_visitors,
#             comments_count=comments,
#             shares_count=shares
#         )
#         db_post_analytics[analytics_id] = analytics_entry
#     # Also update the main post view count
#     if post_id in db_posts:
#         db_posts[post_id].increment_view_count() # This might be redundant if daily views are summed up
#     return db_post_analytics.get(analytics_id)

