from models.db import initialize_db
from app import create_app

app = create_app()
initialize_db(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)