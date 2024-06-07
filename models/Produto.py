from pydantic import BaseModel
from typing import Optional

from create_tables import get_connection

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: str
    preco: float
    estoque: int

def create_produto(produto: Produto):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Produto (nome, descricao, preco, estoque)
            VALUES (?, ?, ?, ?)
        ''', (produto.nome, produto.descricao, produto.preco, produto.estoque))
        conn.commit()
        return cursor.lastrowid

def get_produtos():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Produto')
        return cursor.fetchall()

def get_produto(produto_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Produto WHERE id = ?', (produto_id,))
        return cursor.fetchone()

def update_produto(produto_id: int, produto: Produto):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Produto
            SET nome = ?, descricao = ?, preco = ?, estoque = ?
            WHERE id = ?
        ''', (produto.nome, produto.descricao, produto.preco, produto.estoque, produto_id))
        conn.commit()
        return cursor.rowcount

def delete_produto(produto_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Produto WHERE id = ?', (produto_id,))
        conn.commit()
        return cursor.rowcount
