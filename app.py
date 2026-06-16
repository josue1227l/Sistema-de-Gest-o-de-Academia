from flask import Flask
from controlador import registrar_rotas
from database import criar_tabelas

app = Flask(__name__)
app.secret_key = "academia123"

criar_tabelas()

registrar_rotas(app)

if __name__ == "__main__":
    app.run(debug=True)