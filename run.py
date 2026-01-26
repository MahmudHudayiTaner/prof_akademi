import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    environment = os.getenv('FLASK_ENV', 'development')
    app.run(debug=True)