import crudBD
from crudBD import vendedor, produto

def insertVendedor(nome, sobrenome, empresa):
    print("\n------ INSERT VENDEDOR ------")
    produtos = []
    mydict = {"nome" : nome, "sobrenome" : sobrenome, "empresa" : empresa, "produtos" : produtos}

    novoVendedor = vendedor.insert_one(mydict)
    print("Vendedor criado com sucesso" + "\nVendor ID: {}".format(novoVendedor.inserted_id))

def todosVendedor():
    crudBD.readTodos(vendedor, 'Vendedor')

def idVendedor(id):
    crudBD.readID(vendedor, id)

def atualizaVendedor(id, campo, novoValor):
    crudBD.atualizaPadrao(vendedor, id, campo, novoValor)

def deletarVendedor(id):
    crudBD.deletePadrao(vendedor, id)