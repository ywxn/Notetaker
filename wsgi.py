from notetaker import app
from flask_cors import CORS

if __name__ == "__main__":
    app.run()
    CORS(app)  # Enable CORS for all routes