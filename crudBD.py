import pymongo
from pprint import pprint
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://izumifatec:n68oXixu0jEow8iy@cluster0.wawlm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

global mybd
mybd = client.MercadoLivre

# Coleções
global vendedor
vendedor = mybd.Vendedor

global produto
produto = mybd.Produto

global usuario
usuario = mybd.Usuário

global compra
compra = mybd.Compra


def docCompleto(colecao, id):
    doc = colecao.find_one( {'_id' : ObjectId(id)} )
    return doc

# ------ INSERT ------
def novoEndereco():
    rua = input('Rua: ')
    numero = input('Número: ')
    complemento = input('Complemento: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')
    endereco = {
        'rua': rua,
        'numero': numero,
        'complemento' : complemento,
        'bairro' : bairro,
        'cidade' : cidade,
        'estado' : estado
    }

    return endereco

# ------  READ  ------
def readTodos(colecao, titulo):
    if (titulo == 'Vendedor'):
        print("\n------ {}ES ------".format(titulo.upper()))
    else:
        print("\n------ {}S ------".format(titulo.upper()))
    
    mydoc = colecao.find().sort('_id')
    num = 1
    for d in mydoc:
        print('\n{}. {}:'.format(num, titulo))
        pprint(d)
        num += 1

def readID(colecao, id):
    mydoc = colecao.find_one( {'_id' : ObjectId(id)} )
    pprint(mydoc)

# ------ UPDATE ------
def atualizaPadrao(colecao, id, campo, novoValor):
    colecao.update_one({'_id' : ObjectId(id)}, {'$set': {campo : novoValor}})

# ------ DELETE ------
def deletePadrao(colecao, id):
    colecao.delete_one({ '_id' : ObjectId(id) })
