from app import app
from decouple import config

if __name__ == "__main__":
    app.secret_key = config("SECRET_KEY")
    app.run()
