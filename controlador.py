from flask import render_template, request, redirect, url_for, session
from functools import wraps

from database import (
    inserir_aluno,
    listar_alunos,
    excluir_aluno,
    buscar_aluno,
    atualizar_aluno,

    inserir_instrutor,
    listar_instrutores,
    excluir_instrutor
)

# =====================================
# DECORADOR
# =====================================

def login_obrigatorio():

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if "logado" not in session:
                return redirect(url_for("login"))

            return func(*args, **kwargs)

        return wrapper

    return decorator


# =====================================
# REGISTRAR ROTAS
# =====================================

def registrar_rotas(app):

    # ==========================
    # LOGIN
    # ==========================

    @app.route("/")
    def login():
        return render_template("login.html")

    @app.route("/autenticar", methods=["POST"])
    def autenticar():

        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == "admin" and senha == "123":

            session["logado"] = True
            session["usuario"] = usuario

            return redirect(url_for("painel"))

        return render_template(
            "login.html",
            mensagem="Usuário ou senha inválidos!"
        )

    @app.route("/logout")
    def logout():

        session.clear()

        return redirect(url_for("login"))

    # ==========================
    # PAINEL VISUAL
    # ==========================

    @app.route("/painel")
    @login_obrigatorio()
    def painel():

        lista = listar_alunos()

        return render_template(
            "painel.html",
            total_alunos=len(lista)
        )

    # ==========================
    # LISTAR ALUNOS
    # ==========================

    @app.route("/alunos")
    @login_obrigatorio()
    def alunos():

        lista = listar_alunos()

        return render_template(
            "alunos.html",
            alunos=lista
        )

    # ==========================
    # CADASTRAR ALUNO
    # ==========================

    @app.route("/cadastrar_aluno", methods=["POST"])
    @login_obrigatorio()
    def cadastrar_aluno():

        try:

            inserir_aluno(
                request.form.get("nome"),
                request.form.get("email"),
                request.form.get("telefone"),
                request.form.get("matricula"),
                request.form.get("peso"),
                request.form.get("altura")
            )

            return redirect(url_for("alunos"))

        except Exception as erro:

            return render_template(
                "alunos.html",
                alunos=listar_alunos(),
                mensagem=f"Erro ao cadastrar: {erro}"
            )

    # ==========================
    # EXCLUIR ALUNO
    # ==========================

    @app.route("/excluir_aluno/<int:id>")
    @login_obrigatorio()
    def excluir(id):

        try:
            excluir_aluno(id)
        except:
            pass

        return redirect(url_for("alunos"))


    # ==========================
    # EDITAR ALUNO
    # ==========================

    @app.route("/editar_aluno/<int:id>")
    @login_obrigatorio()
    def editar_aluno(id):

        aluno = buscar_aluno(id)

        if not aluno:
            return redirect(url_for("alunos"))

        return render_template(
            "editar_aluno.html",
            aluno=aluno
        )


    # ==========================
    # ATUALIZAR ALUNO
    # ==========================

    @app.route("/atualizar_aluno/<int:id>", methods=["POST"])
    @login_obrigatorio()
    def atualizar(id):

        atualizar_aluno(
            id,
            request.form.get("nome"),
            request.form.get("email"),
            request.form.get("telefone"),
            request.form.get("matricula"),
            request.form.get("peso"),
            request.form.get("altura")
        )

        return redirect(url_for("alunos"))

    # ==========================
    # CADASTRAR INSTRUTOR
    # ==========================

    @app.route("/instrutores")
    @login_obrigatorio()
    def instrutores():

        lista = listar_instrutores()

        return render_template(
            "instrutores.html",
            instrutores=lista
        )


    @app.route("/cadastrar_instrutor", methods=["POST"])
    @login_obrigatorio()
    def cadastrar_instrutor():

        inserir_instrutor(
            request.form.get("nome"),
            request.form.get("email"),
            request.form.get("telefone"),
            request.form.get("cref")
        )

        return redirect(url_for("instrutores"))


    @app.route("/excluir_instrutor/<int:id>")
    @login_obrigatorio()
    def excluir_instrutor_rota(id):

        excluir_instrutor(id)

        return redirect(url_for("instrutores"))