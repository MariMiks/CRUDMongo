import crudBD 
from crudBD import novoEndereco, usuario as colUsuario, produto as colProduto
import colecoes.vendedor as vendedor
import colecoes.produto as produto
import colecoes.usuario as usuario
import colecoes.compra as compra
import colecoes.favorito as favorito


print('Bem vindo ao Mercado Livre! :)')

deslogar = False

while (deslogar != True) :
    print('\nCategorias: \n' + 
          '1. Vendedor\n' + 
          '2. Produto\n' + 
          '3. Usuário\n' + 
          '4. Compra\n' +
          '5. Sair')
    categoria = int(input('Escolha uma categoria: '))
    
    match categoria :
        case 1: #vendedor
            voltar = False

            while (voltar == False) :
                print('\n------ VENDEDOR ------')
                print('1. Criar novo\n' + 
                    '2. Listar todos\n' + 
                    '3. Vendedor específico (ID)\n' + 
                    '4. Atualizar\n' +
                    '5. Deletar\n' +
                    '6. Voltar')
                
                opVend = int(input('O que deseja fazer hoje? '))
                
                match opVend :
                    case 1:
                        print('\n------ Novo Vendedor ------')
                        vendNome = input('Nome: ')
                        vendSobrenome = input('Sobrenome: ')
                        vendEmpresa = input('Empresa: ')
                        vendedor.insertVendedor(vendNome, vendSobrenome, vendEmpresa)
                    
                    case 2:
                        vendedor.todosVendedor()
                    
                    case 3:
                        vendedor.todosVendedor()
                        
                        print('\n------ Vendedor específico ------')
                        idVend = input('Digite o ID do vendedor: ')

                        print("\n------ VENDEDOR ESCOLHIDO ------")
                        vendedor.idVendedor(idVend)
                    
                    case 4:
                        vendedor.todosVendedor()
                        
                        print('\n------ Atualizar vendedor ------')
                        idVend = input('Digite o ID do vendedor: ')

                        print("\n------ VENDEDOR ESCOLHIDO ------")
                        vendedor.idVendedor(idVend)

                        opAtu = 'S'

                        while (opAtu != 'N'):
                            campoVend = input('\nO que deseja atualizar? ')
                            novoVend = input('Digite o novo valor: ')

                            print('\nCampo {} atualizado'.format(campoVend))
                            vendedor.atualizaVendedor(idVend, campoVend, novoVend)
                            opAtu = input('Deseja atualizar mais algum campo? (S/N) ')
                    
                    case 5:
                        vendedor.todosVendedor()

                        print('\n------ Deletar vendedor ------')
                        idUsr = input('Digite o ID do vendedor: ')

                        print("\n------ VENDEDOR DELETADO ------")
                        vendedor.deletarVendedor(idUsr)
            
                    case 6:
                        break
                    case _:
                        print('Não entendi :(')
        
        case 2: #produto
            voltar = False
            while (voltar == False):
                print('------ PRODUTO ------')
                print('1. Criar novo\n' + 
                    '2. Listar todos\n' + 
                    '3. Produto específico (ID)\n' + 
                    '4. Atualizar\n' +
                    '5. Deletar\n' +
                    '6. Voltar')
                opProd = int(input('O que deseja fazer hoje? '))

                match opProd:
                    case 1:
                        print('\n------ Novo Produto ------')
                        prodNome = input('Nome: ')
                        prodValor = float(input('Valor: '))
                        
                        print('\nEscolha um vendedor para atribuir a este produto')
                        vendedor.todosVendedor()

                        idVendProd = input('\nId do vendedor: ')
                        
                        produto.insertProduto(prodNome, prodValor, idVendProd)

                    case 2:
                        produto.todosProduto()
                    
                    case 3:
                        print('\n------ Produto específico ------')
                        idProd = input('Digite o ID do produto: ')

                        print("\n------ PRODUTO ESCOLHIDO ------")
                        produto.idProduto(idProd)
                    
                    case 4:
                        print('\n------ Atualizar produto ------')
                        produto.todosProduto()
                        idProd = input('\n\nDigite o ID do produto: ')

                        print("\n------ PRODUTO ESCOLHIDO ------")
                        produto.idProduto(idProd)
                        
                        opAtu = 'S'

                        while (opAtu != 'N'):
                            campoProd = input('\nO que deseja atualizar? ')
                            novoProd = input('Digite o novo valor: ')

                            print('\nCampo {} atualizado'.format(campoProd))
                            produto.atualizaProduto(idProd, campoProd, novoProd)
                            opAtu = input('Deseja atualizar mais algum campo? (S/N) ')

                    case 5:
                        print('\n------ Deletar produto ------')
                        idProd = input('Digite o ID do produto: ')

                        print("\n------ PRODUTO DELETADO ------")
                        produto.deletarProduto(idProd)
                    
                    case 6:
                        break

                    case _:
                        print('\nNão entendi :(')

        case 3: #usuario
            voltar = False
            while (voltar == False) :
                print('\n------ USUÁRIO ------')
                print('1. Criar novo\n' + 
                    '2. Listar todos\n' + 
                    '3. Usuário específico (ID)\n' + 
                    '4. Atualizar informações do usuário\n' +
                    '5. Deletar usuário\n' +
                    '6. Voltar')
                opUser = int(input('O que deseja fazer hoje?  '))

                match opUser:
                    case 1:
                        print('\n------ Novo Usuário ------\n')
                        userNome = input('Nome: ')
                        userSobrenome = input('Sobrenome: ')

                        print('\nNovo endereço:')
                        userEndereco = novoEndereco()
                        
                        usuario.insertUsuario(userNome, userSobrenome, userEndereco)
                    
                    case 2:
                        usuario.todosUsuario()
                    
                    case 3:
                        print('\n------ Usuário específico ------')
                        usuario.todosUsuario()

                        idUs = input('\nDigite o ID do usuário: ')

                        print("\n------ USUÁRIO ESCOLHIDO ------")
                        usuario.idUsuario(idUs)

                    case 4:
                        print('\n------ Atualizar usuário ------')
                        idUsr = input('Digite o ID do usuário: ')

                        print("\n------ USUÁRIO ESCOLHIDO ------")
                        usuario.idUsuario(idUsr)

                        opAtu = 'S'

                        while (opAtu != 'N'):
                            print('\n------ O que deseja atualizar ------')
                            print('\n1. Dados gerais do usuário' + 
                                  '\n2. Adicionar favoritos' + 
                                  '\n3. Excluir favoritos' +
                                  '\n4. Voltar')
                            opUsrCat = int(input('\nEscolha a opção: '))
                            

                            match opUsrCat:
                                case 1:
                                    dataUsr = 'S'
                                    while dataUsr != 'N':
                                        campoUsr = input('\nCampo que deseja atualizar: ').lower()
                                        if campoUsr != 'endereco':
                                            novoUsr = input('Digite o novo valor: ')
                                        else:
                                            novoUsr = crudBD.novoEndereco()

                                        print('\nCampo {} atualizado'.format(campoUsr))
                                        usuario.atualizaUsuario(idUsr, campoUsr, novoUsr)
                                        dataUsr = input('Deseja atualizar mais algum campo? (S/N)').upper()
                                case 2:
                                    opFav = 'S'
                                    while (opFav != 'N'):
                                        print('\n------ Novo produto favorito ------\n')
                                        produto.todosProduto()
                            
                                        idNewFav = input('\nPasse o ID do produto que deseja: ')
                                        
                                        favorito.adicionarFavoritos(idUsr, idNewFav)
                                        print('\nProduto adicionado aos seus favoritos!')
                                        opFav = input('Quer cadastrar mais produtos favoritos? (S/N)  ').upper()
                                case 3:
                                    print('\n------ Excluir favorito ------\n')
                                    favorito.excluirFavorito(idUsr)


                            opAtu = input('Deseja atualizar algo mais? (S/N) ').upper()

                    case 5:
                        print('\n------ Deletar usuário ------')
                        idUsr = input('Digite o ID do usuário: ')

                        print("\n------ USUÁRIO DELETADO ------")
                        usuario.deletarUsuario(idUsr)
                    
                    case 6:
                        break

                    case _:
                        print('\nNão entendi :(')
        
        case 4: #compra
            voltar = False
            while (voltar == False) :
                print('\n------ COMPRAR ------')
                print('1. Nova compra\n' + 
                    '2. Listar todas\n' + 
                    '3. Compra específica (ID)\n' + 
                    '4. Voltar\n')
                opComp = int(input('O que deseja fazer hoje? '))

                match opComp:
                    case 1:
                        print('\n------ Nova Compra ------\n')
                        print('--> Quem está realizando a compra?\n')
                        usuario.todosUsuario()
                        idUser = input('Id usuário: ')
                        user = crudBD.docCompleto(colUsuario, idUser)
                        
                        print('--> O que deseja comprar?\n')
                        produto.todosProduto()
                        crompProdutos = []
                        crompTotal = 0
                        opProd = 'S'
                        while (opProd != 'N'):
                            idProd = input('Id produto: ')
                            prod = crudBD.docCompleto(colProduto, idProd)
                            
                            crompProdutos.append(prod)
                            valorProd = float(prod["valor"])
                            crompTotal += valorProd
                            
                            opProd = input('Deseja adicionar mais produtos? (S/N) ').upper()


                        print('--> Quando está comprando?\n')
                        crompDataInicio = input('Data de hoje: ')
                        
                        
                        print('--> Escolha seu endereço de entrega:\n')
                        print(user['endereco'])

                        opEndereco = input('\nDeseja utilizar este endereco? (S/N) ').upper()

                        if opEndereco == 'N':
                            print('\n---- Novo endereco ----')
                            crompOutroEndereco = crudBD.novoEndereco()

                            compra.insertCompra(idUser, prod["vendedor"], crompProdutos, crompTotal, crompDataInicio, crompOutroEndereco)
                        
                        else:
                            compra.insertCompra(idUser, prod["vendedor"], crompProdutos, crompTotal, crompDataInicio, user["endereco"])


                    case 2:
                        compra.todosCompra()
                    
                    case 3:
                        print('\n------ Compra específica ------')
                        idComp = input('Digite o ID da compra: ')

                        print("\n------ COMPRA ESCOLHIDO ------")
                        compra.idCompra(idComp)
                    
                    case 4:
                        break

                    case _:
                        print('\nNão entendi :(')
        
        case 5:
            break
        
        case _:
            print('Não entendi :(')


print('\nAté logo!')