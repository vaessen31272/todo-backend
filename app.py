import os
from flask import Flask
from flask_cors import CORS
from models import db
from routes import routes

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(os.getcwd(), "tasks.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# @app.before_first_request
def create_db_tables():
    print("Creating database tables...")
    db.create_all()

# Register the routes blueprint
app.register_blueprint(routes)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
    
    


