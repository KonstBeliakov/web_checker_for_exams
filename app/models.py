from app import db


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    repository_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Test {self.id} - {self.name}>"
