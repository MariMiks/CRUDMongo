import crudBD
from crudBD import usuario, produto, vendedor

def insertUsuario(nome, sobrenome, endereco, idProduto):
    print("\n------ INSERT USUARIO ------")
    
    docProdFav = list(crudBD.docCompleto(produto, idProduto))
    
    mydict = {
        "nome" : nome,
        "sobrenome" : sobrenome,
        "endereco" : endereco,
        "favoritos" : favoritos
    }

    novoUsuario = usuario.insert_one(mydict)
    print("\nUsuário cadastrado com sucesso" + "\nUsuario ID: {}".format(novoUsuario.inserted_id))

def todosUsuario():
    crudBD.readTodos(usuario, 'Usuário')

def idUsuario(id):
    crudBD.readID(usuario, id)

def atualizaUsuario(id, campo, novoValor):
    crudBD.atualizaPadrao(usuario, id, campo, novoValor)

def deletarUsuario(id):
    crudBD.deletePadrao(usuario, id)