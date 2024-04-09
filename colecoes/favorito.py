import crudBD
from crudBD import usuario, produto

def insertFavorito(idProduto):
    favoritos = []
    docProduto = list(crudBD.docCompleto(produto, idProduto))
    favoritos.append(docProduto)
    
    return favoritos
