# Import needed modules
import os


# Define a class to pass keys to access the app DB as well as the stripe keys
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///app.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STRIPE_SECRET_KEY = os.environ.get(
        "STRIPE_SECRET_KEY", "sk_test_your_key_here"
    )
    STRIPE_PUBLISHABLE_KEY = os.environ.get(
        "STRIPE_PUBLISHABLE_KEY", "pk_test_your_key_here"
    )
