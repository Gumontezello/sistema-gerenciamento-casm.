
from flask import Flask, request, redirect, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///casm.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.Integer)

with app.app_context():
    db.create_all()

pagina = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CASM - Gestão Esportiva</title>
<style>
body {font-family:Arial;background:#eee;margin:0;color:#222}
header {background:#171717;color:white;text-align:center;padding:25px;border-bottom:5px solid #c90024}
main {max-width:700px;margin:25px auto;padding:15px}
.card {background:white;padding:20px;border-radius:10px;margin:15px 0}
input,button {padding:12px;margin:5px 0;width:100%;box-sizing:border-box}
button {background:#bd0025;color:white;border:0;border-radius:5px}
a {color:#bd0025}
</style>
</head>
<body>
<header>
<h1>CASM</h1>
<p>Clube Atlético São Mateus</p>
<p>Sistema de Gerenciamento Esportivo</p>
</header>
<main>
<div class="card">
<h2>Cadastrar jogador</h2>
<form action="/cadastrar" method="POST">
<input name="nome" placeholder="Nome do jogador" required>
<input name="posicao" placeholder="Posição" required>
<input name="numero" type="number" placeholder="Número da camisa">
<button type="submit">Cadastrar jogador</button>
</form>
</div>
<div class="card">
<h2>Elenco cadastrado</h2>
{% for jogador in jogadores %}
<p><strong>{{ jogador.nome }}</strong> - {{ jogador.posicao }}
{% if jogador.numero %} - Camisa {{ jogador.numero }}{% endif %}
<a href="/excluir/{{ jogador.id }}">Excluir</a></p>
{% else %}
<p>Nenhum jogador cadastrado.</p>
{% endfor %}
</div>
</main>
</body>
</html>
"""

@app.route("/")
def inicio():
    jogadores = Jogador.query.order_by(Jogador.nome).all()
    return render_template_string(pagina, jogadores=jogadores)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome", "").strip()
    posicao = request.form.get("posicao", "").strip()
    numero = request.form.get("numero")

    if nome and posicao:
        jogador = Jogador(
            nome=nome,
            posicao=posicao,
            numero=int(numero) if numero else None
        )
        db.session.add(jogador)
        db.session.commit()

    return redirect("/")

@app.route("/excluir/<int:id>")
def excluir(id):
    jogador = db.session.get(Jogador, id)
    if jogador:
        db.session.delete(jogador)
        db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=False)
