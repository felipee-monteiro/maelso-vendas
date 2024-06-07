from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

from create_tables import get_connection

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    data_de_nascimento: date
    cpf: str
    id_contato: Optional[int]
    id_endereco: Optional[int]

def create_usuario(usuario: Usuario):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Usuario (nome, data_de_nascimento, cpf, id_contato, id_endereco)
            VALUES (?, ?, ?, ?, ?)
        ''', (usuario.nome, usuario.data_de_nascimento, usuario.cpf, usuario.id_contato, usuario.id_endereco))
        conn.commit()
        return cursor.lastrowid

def get_usuarios():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Usuario')
        return cursor.fetchall()

def get_usuario(usuario_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Usuario WHERE id = ?', (usuario_id,))
        return cursor.fetchone()

def update_usuario(usuario_id: int, usuario: Usuario):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Usuario
            SET nome = ?, data_de_nascimento = ?, cpf = ?, id_contato = ?, id_endereco = ?
            WHERE id = ?
        ''', (usuario.nome, usuario.data_de_nascimento, usuario.cpf, usuario.id_contato, usuario.id_endereco, usuario_id))
        conn.commit()
        return cursor.rowcount

def delete_usuario(usuario_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Usuario WHERE id = ?', (usuario_id,))
        conn.commit()
        return cursor.rowcount
