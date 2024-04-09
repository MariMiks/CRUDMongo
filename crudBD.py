import pymongo
from pprint import pprint
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://marianasilva155:marianasilva155@fatecnosql.vyamlgr.mongodb.net/?retryWrites=true&w=majority&appName=FatecNoSQL")

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
compra = mybd.Compra

# ------  CRUD  ------
# ------ CREATE ------
def docCompleto(colecao, id):
    doc = colecao.find( {'_id' : ObjectId(id)} )
    return doc

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
    mydoc = colecao.find( {'_id' : ObjectId(id)} )
    for x in mydoc:
        pprint(x)
    
# ------ UPDATE ------
def atualizaPadrao(colecao, id, campo, novoValor):
    colecao.update_one({'_id' : ObjectId(id)}, {'$set': {campo : novoValor}})

# ------ DELETE ------
def deletePadrao(colecao, id):
    colecao.delete_one({ '_id' : ObjectId(id) })

