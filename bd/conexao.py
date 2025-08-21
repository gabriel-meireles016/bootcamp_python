import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?);', dados)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (1,)
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute('SELECT * FROM clientes WHERE id=?;', (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    cursor.execute('SELECT * FROM clientes ORDER BY nome;')
    return cursor.fetchall()

#atualizar_registro(conexao, cursor, 'Thayná', 'thayna@gmail.com', 2)
#excluir_registro(conexao, cursor, 1)

dados = [
    ('Dante','dante@gmail.com'),
    ('Jett','@gmail.com'),
    ('Frida','@gmail.com'),
]
#inserir_muitos(conexao, cursor, dados)

#print(recuperar_cliente(cursor, 2))

#print(listar_clientes(cursor))

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))
print(cliente['id'], cliente['nome'], cliente['email'])