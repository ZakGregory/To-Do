from application import db

class Tasks(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    complete=db.Column(db.Boolean, default=False)
