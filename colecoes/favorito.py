import crudBD
from crudBD import produto, usuario
import colecoes.usuario as colUsuario
from pprint import pprint

def insertFavorito(idProduto):
    favoritos = []
    docProduto = list(crudBD.docCompleto(produto, idProduto))
    favoritos.append(docProduto)
    
    return favoritos

def adicionarFavoritos(idUsuario, idProduto):
    docProduto = crudBD.docCompleto(produto, idProduto)

    colUsuario.atualizaUsuario(idUsuario, "favoritos", docProduto)

def excluirFavorito(idUsuario):
    docUsuario = crudBD.docCompleto(usuario, idUsuario)
    listaFavs = [docUsuario['favoritos']]

    print('\nSeus favoritos:\n')

    for i in range(len(listaFavs)):
        print('{}. favorito: \n'.format(i+1))
        pprint(listaFavs[i])
    
    delFav = int(input('\nEscolha qual deseja deletar: '))
    prodFav = listaFavs[delFav-1]
    listaFavs.remove(prodFav)
    
    colUsuario.atualizaUsuario(idUsuario, 'favoritos', listaFavs)
    print('\nProduto desfavoritado!')