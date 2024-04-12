import crudBD
from crudBD import usuario, produto, vendedor

def insertUsuario(nome, sobrenome, endereco, favoritos):
    print("\n------ INSERT USUARIO ------")
    
    mydict = {
        "nome" : nome,
        "sobrenome" : sobrenome,
        "endereco" : endereco,
        "favoritos" : [favoritos]
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