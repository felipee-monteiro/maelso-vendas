from pydantic import BaseModel
from typing import Optional
from datetime import date

from create_tables import get_connection

class Contato(BaseModel):
    id: Optional[int] = None
    email: str
    telefone: str
    id_usuario: int

def create_contato(contato: Contato):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Contato (email, telefone, id_usuario)
            VALUES (?, ?, ?)
        ''', (contato.email, contato.telefone, contato.id_usuario))
        conn.commit()
        return cursor.lastrowid

def get_contatos():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Contato')
        return cursor.fetchall()

def get_contato(contato_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Contato WHERE id = ?', (contato_id,))
        return cursor.fetchone()

def update_contato(contato_id: int, contato: Contato):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Contato
            SET email = ?, telefone = ?, id_usuario = ?
            WHERE id = ?
        ''', (contato.email, contato.telefone, contato.id_usuario, contato_id))
        conn.commit()
        return cursor.rowcount

def delete_contato(contato_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Contato WHERE id = ?', (contato_id,))
        conn.commit()
        return cursor.rowcount