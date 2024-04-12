import crudBD
from crudBD import usuario, produto

def insertFavorito(idProduto):
    favoritos = []
    docProduto = list(crudBD.docCompleto(produto, idProduto))
    favoritos.append(docProduto)
    
    return favoritos

def adicionarFavoritos(idUsuario, idProduto):
    docUsuario = crudBD.docCompleto(usuario, idUsuario)
    docProduto = crudBD.docCompleto(produto, idProduto)

    if idProduto in docUsuario['favoritos']:
        return print('Produto já favoritado!')

    else:
        docUsuario['favoritos']
