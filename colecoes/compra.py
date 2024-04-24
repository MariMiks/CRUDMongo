import crudBD
from crudBD import compra, usuario, vendedor, produto, docCompleto

def insertCompra(idUsuario, vendedor, produtos, valorTotal, dataInicial, endereco):
    docUsuario = list(docCompleto(usuario, idUsuario))
    
    print("\n------ INSERT COMPRA ------")
    mydict = {
        "usuario" : docUsuario,
        "vendedor" : vendedor,
        "produtos" : produtos,
        "valorTotal" : valorTotal,
        "dataInicial" : dataInicial,
        "endereco" : endereco
    }
    
    novoCompra = compra.insert_one(mydict)
    print('\nCompra cadastrada com sucesso\n' + "\nCompra ID: {}".format(novoCompra.inserted_id))

def todosCompra():
    crudBD.readTodos(compra, 'Compra')

def idCompra(id):
    crudBD.readID(compra, id)