from src.database import db
class Car (db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key = True)
    model = db.Column(db.String(200), nullable = False)

    def __init__(self, id, model):
        self.id = id
        self.model = model

    def add_to_database(self):
        db.session.add(self)
        db.session.commit()