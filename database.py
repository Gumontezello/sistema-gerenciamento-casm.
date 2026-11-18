
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.Integer)
    telefone = db.Column(db.String(20))

    def __repr__(self):
        return f"<Jogador {self.nome}>"
