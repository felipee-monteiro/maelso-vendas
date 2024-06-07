from typing import Annotated
from fastapi import FastAPI, Body
from create_tables import create_tables
from models.Usuario import create_usuario, get_usuarios, update_usuario, get_usuario, delete_usuario, Usuario

from models.Produto import create_produto, get_produtos, update_produto, get_produto, delete_produto, Produto

from models.Vendas import create_venda, get_vendas, update_venda, get_venda, delete_venda, Venda

app = FastAPI()

create_tables()

@app.post("/usuarios/")
def create_user_controller(dados_usuario: Annotated[Usuario, Body(embed=True)]):
    create_usuario(dados_usuario)
    return {"message": "User created"}

@app.get("/usuarios/")
def create_user_controller():
    all_users = get_usuarios()
    return all_users

@app.get("/usuarios/{usuario_id}")
def create_user_controller(usuario_id: int):
    usuario = get_usuario(usuario_id=usuario_id)
    return usuario

@app.put("/usuarios/{usuario_id}")
def update_user_controller(usuario_id: int, dados_usuario: Annotated[Usuario, Body(embed=True)]):
    update_usuario(
        usuario_id=usuario_id,
        usuario=dados_usuario,
    )
    return {"message": "Usuário Atualizado !"}

@app.delete("/usuarios/{usuario_id}")
def delete_user_controller(usuario_id: int):
    delete_usuario(usuario_id)
    return {"message": "Usuário Excluído !"}






@app.post("/produtos/")
def create_product(dados_produto: Annotated[Produto, Body(embed=True)]):
    create_produto(dados_produto)
    return {"message": "Produto Criado !"}

@app.get("/produtos/")
def get_products_controller():
    return get_produtos()

@app.get("/produtos/{produto_id}")
def get_product_controller(produto_id: int):
    return get_produto(produto_id=produto_id)

@app.put("/produtos/{produto_id}")
def update_product_controller(produto_id: int, dados_produto: Annotated[Produto, Body(embed=True)]):
    update_produto(
        produto_id=produto_id,
        produto=dados_produto,
    )
    return {"message": "Produto Atualizado !"}

@app.delete("/produtos/{produto_id}")
def delete_product_controller(produto_id: int):
    delete_produto(produto_id)
    return {"message": "Produto Excluído !"}



@app.post("/vendas/")
def create_venda_controller(dados_venda: Annotated[Venda, Body(embed=True)]):
    create_venda(dados_venda)
    return {"message": "Venda Criada !"}

@app.get("/vendas/")
def get_vendas_controller():
    return get_vendas()

@app.get("/vendas/{venda_id}")
def get_venda_controller(venda_id: int):
    return get_venda(venda_id=venda_id)

@app.put("/vendas/{venda_id}")
def update_venda_controller(venda_id: int, dados_venda: Annotated[Venda, Body(embed=True)]):
    update_venda(
        venda_id=venda_id,
        venda=dados_venda,
    )
    return {"message": "Venda Atualizada !"}

@app.delete("/vendas/{venda_id}")
def delete_venda_controller(venda_id: int):
    delete_venda(venda_id)
    return {"message": "Venda Excluída !"}