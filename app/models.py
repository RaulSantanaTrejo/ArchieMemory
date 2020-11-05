from app import db

class Memory(db.Model):
    __tablename__ = 'memories'

    id = db.Column(db.Integer, primary_key=True)
    memory_content = db.Column(db.String())
    memory_category = db.Column(db.String())

    def __init__(self, memory_content, memory_category):
        self.memory_content = memory_content
        self.memory_category = memory_category

    def __repr__(self):
        return '<id {}>'.format(self.id)
