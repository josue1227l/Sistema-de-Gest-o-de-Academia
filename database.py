import sqlite3  # Importa a biblioteca SQLite para trabalhar com banco de dados

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect("academia.db")


# Cria as tabelas caso elas ainda não existam
def criar_tabelas():

    conexao = conectar()  # Abre conexão com o banco
    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL

    # Cria a tabela de alunos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        matricula TEXT,
        peso REAL,
        altura REAL
    )
    """)

    # Cria a tabela de instrutores
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS instrutores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        cref TEXT
    )
    """)

    conexao.commit()  # Salva as alterações
    conexao.close()   # Fecha a conexão


# Insere um novo aluno no banco
def inserir_aluno(nome, email, telefone, matricula, peso, altura):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO alunos
    (nome,email,telefone,matricula,peso,altura)
    VALUES (?,?,?,?,?,?)
    """, (nome, email, telefone, matricula, peso, altura))

    conexao.commit()  # Salva a inserção
    conexao.close()


# Lista todos os alunos cadastrados
def listar_alunos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")  # Busca todos os alunos

    alunos = cursor.fetchall()  # Armazena os resultados

    conexao.close()

    return alunos  # Retorna a lista de alunos


# Exclui um aluno pelo ID
def excluir_aluno(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM alunos WHERE id=?",
        (id,)
    )

    conexao.commit()  # Salva a exclusão
    conexao.close()


# Busca um aluno específico pelo ID
def buscar_aluno(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM alunos WHERE id=?",
        (id,)
    )

    aluno = cursor.fetchone()  # Retorna apenas um registro

    conexao.close()

    return aluno


# Atualiza os dados de um aluno existente
def atualizar_aluno(
    id,
    nome,
    email,
    telefone,
    matricula,
    peso,
    altura
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE alunos
    SET nome=?,
        email=?,
        telefone=?,
        matricula=?,
        peso=?,
        altura=?
    WHERE id=?
    """,
    (
        nome,
        email,
        telefone,
        matricula,
        peso,
        altura,
        id
    ))

    conexao.commit()  # Salva as alterações
    conexao.close()


# Insere um novo instrutor
def inserir_instrutor(nome, email, telefone, cref):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO instrutores (nome, email, telefone, cref)
     VALUES (?, ?, ?, ?)
     """, (nome, email, telefone, cref))

    conexao.commit()
    conexao.close()


# Lista todos os instrutores cadastrados
def listar_instrutores():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM instrutores")

    instrutores = cursor.fetchall()

    conexao.close()

    return instrutores


# Exclui um instrutor pelo ID
def excluir_instrutor(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM instrutores WHERE id=?",
        (id,)
    )

    conexao.commit()
    conexao.close()