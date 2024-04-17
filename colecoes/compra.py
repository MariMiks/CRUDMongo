import crudBD
from crudBD import compra, vendedor, produto, usuario

def insertCompra(usuario, vendedor, produtos, valorTotal, dataInicial, dataEntrega, endereco):
    print("\n------ INSERT COMPRA ------")
    mydict = {
        "usuario" : usuario,
        "vendedor" : vendedor,
        "produtos" : produtos,
        "valorTotal" : valorTotal,
        "dataInicial" : dataInicial,
        "dataEntrega" : dataEntrega,
        "endereco" : endereco
    }

    

    novoCompra = compra.insert_one(mydict)
    print('\nCompra cadastrada com sucesso\n' + "\nCompra ID: {}".format(novoCompra.inserted_id))

def todosCompra():
    crudBD.readTodos(compra, 'Compra')

def idCompra(id):
    crudBD.readID(compra, id)

def deletarCompra(id):
    crudBD.deletePadrao(compra, id)