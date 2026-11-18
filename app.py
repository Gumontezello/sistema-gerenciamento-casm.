
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/jogadores")
def jogadores():
    return "Área de gerenciamento de jogadores do CASM"

@app.route("/partidas")
def partidas():
    return "Área de gerenciamento de partidas do CASM"

@app.route("/resultados")
def resultados():
    return "Área de resultados do CASM"

if __name__ == "__main__":
    app.run(debug=True)
