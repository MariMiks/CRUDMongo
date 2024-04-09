import crudBD
from crudBD import produto, vendedor

def insertProduto(nome, valor, idVend):
    print("\n------ INSERT PRODUTO ------")

    docVendedor = list(crudBD.docCompleto(vendedor, idVend))

    mydict = {"nome": nome, "valor" : valor, "vendedor" : docVendedor}

    novoProduto = produto.insert_one(mydict)
    print("Produto criado com sucesso" + "\nProduto ID: {}".format(novoProduto.inserted_id))

def todosProduto():
    crudBD.readTodos(produto, 'Produto')

def idProduto(id):
    crudBD.readID(produto, id)

def atualizaProduto(id, campo, novoValor):
    crudBD.atualizaPadrao(produto, id, campo, novoValor)

def deletarProduto(id):
    crudBD.deletePadrao(produto, id)