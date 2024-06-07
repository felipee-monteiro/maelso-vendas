import sqlite3

def get_connection():
    db_conn = sqlite3.connect('database.db')
    return db_conn

def create_tables():
    db_conn = get_connection()
    cursor = db_conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_de_nascimento DATE NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        id_contato INTEGER NOT NULL,
        id_endereco INTEGER NOT NULL,
        FOREIGN KEY (id_contato) REFERENCES Contato(id),
        FOREIGN KEY (id_endereco) REFERENCES Endereco(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Contato (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        id_usuario INTEGER,
        FOREIGN KEY (id_usuario) REFERENCES Usuario(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Endereco (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rua TEXT NOT NULL,
        numero TEXT NOT NULL,
        complemento TEXT,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        pais TEXT NOT NULL DEFAULT 'Brasil'
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Venda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        data_venda DATE NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES Usuario(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ItemVenda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_venda INTEGER,
        id_produto INTEGER,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (id_venda) REFERENCES Venda(id),
        FOREIGN KEY (id_produto) REFERENCES Produto(id)
    )
    ''')

    db_conn.commit()
    db_conn.close()
