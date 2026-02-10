import os

class Config:
    
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    
    INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
    
    os.makedirs(INSTANCE_DIR, exist_ok=True)
    
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", 
        f"sqlite:///{os.path.join(INSTANCE_DIR, 'reviews.db')}"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False