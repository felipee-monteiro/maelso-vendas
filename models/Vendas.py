from pydantic import BaseModel
from typing import Optional

from create_tables import get_connection

class Venda(BaseModel):
    id: Optional[int] = None
    id_usuario: int
    data_venda: str

def create_venda(venda: Venda):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Venda (id_usuario, data_venda)
            VALUES (?, ?)
        ''', (venda.id_usuario, venda.data_venda))
        conn.commit()
        return cursor.lastrowid

def get_vendas():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Venda')
        return cursor.fetchall()

def get_venda(venda_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Venda WHERE id = ?', (venda_id,))
        return cursor.fetchone()

def update_venda(venda_id: int, venda: Venda):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Venda
            SET id_usuario = ?, data_venda = ?
            WHERE id = ?
        ''', (venda.id_usuario, venda.data_venda, venda_id))
        conn.commit()
        return cursor.rowcount

def delete_venda(venda_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Venda WHERE id = ?', (venda_id,))
        conn.commit()
        return cursor.rowcount
