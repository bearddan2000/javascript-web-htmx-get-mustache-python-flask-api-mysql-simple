from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mariadb+pymysql://maria:pass@db/animal"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class DogModel(db.Model):
    __tablename__ = 'dog'

    id = db.Column(db.Integer, primary_key=True)
    breed = db.Column(db.String())
    color = db.Column(db.String())

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        
@app.route('/dog')
def handle_beverage():
        dogs = DogModel.query.all()
        results = [
            {
                "id": dog.id,
                "breed": dog.breed,
                "color": dog.color
            } for dog in dogs]

        return {"count": len(results), "dog": results, "message": "success"}


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
