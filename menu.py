import colecoes.vendedor as vendedor, colecoes.produto as produto, colecoes.usuario as usuario, colecoes.compra as compra

print('Bem vindo ao Mercado Livre! :)')

deslogar = False

while (deslogar == False) :
    print('\nCategorias: \n' + 
          '1. Vendedor\n' + 
          '2. Produto\n' + 
          '3. Usuário\n' + 
          '4. Compra\n' +
          '6. Sair')
    categoria = int(input('Escolha uma categoria: '))
    
    match categoria :
        case 1:
            voltar = False

            while (voltar == False) :
                print('\n------ VENDEDOR ------')
                print('1. Criar novo\n' + 
                    '2. Listar todos\n' + '3. Vendedor específico (ID)\n' + 
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
        
        case 2:
            voltar = False
            while (voltar == False):
                print('------ PRODUTO ------')
                print('1. Criar novo\n' + 
                    '2. Listar todos\n' + '3. Produto específico (ID)\n' + 
                    '4. Atualizar\n' +
                    '5. Deletar\n' +
                    '6. Voltar')
                opProd = int(input('O que deseja fazer hoje? '))

                match opProd:
                    case 1:
                        print('\n------ Novo Produto ------')
                        prodNome = input('Nome: ')
                        prodValor = float(input('Valor: '))
                        
                        print('\nEscolha um vendedor para atribuir a este produto: ')
                        vendedor.todosVendedor()

                        idVendP = input('\nId do vendedor: ')
                        
                        produto.insertProduto(prodNome, prodValor, idVendP)

                    case 2:
                        produto.todosProduto()
                    
                    case 3:
                        print('\n------ Produto específico ------')
                        idProd = input('Digite o ID do produto: ')

                        print("\n------ PRODUTO ESCOLHIDO ------")
                        produto.idProduto(idProd)
                    
                    case 4:
                        print('\n------ Atualizar produto ------')
                        idProd = input('Digite o ID do produto: ')

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

        case 3:
            voltar = False
            while (voltar == False) :
                print('\n------ USUÁRIO ------')
                print('1. Criar novo\n' + 
                    '2. Listar todos\n' + '3. Usuário específico (ID)\n' + 
                    '4. Atualizar informações do usuário\n' + 
                    '5. Adicionar favoritos\n' +
                    '6. Excluir favoritos\n' +
                    '6. Deletar')
                opUser = int(input('O que deseja fazer hoje?  '))

                match opUser:
                    case 1:
                        print('\n------ Novo Usuário ------\n')
                        userNome = input('Nome: ')
                        userSobrenome = input('Sobrenome: ')

                        userEndereco = []
                        opEnd = 'S'

                        while (opEnd == 'N'):
                            print('\nNovo endereço\n')
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
                            userEndereco.append(endereco)
                            opEnd = input('Deseja cadastrar mais um endereço? (S/N)  ')
                        
                        userFavoritos = []
                        opFav = input('Cadastrar produtos favoritos? (S/N)  ')
                        
                        while (opFav != 'N'):
                            print('\nNovo produto favorito\n')
                            produto.todosProduto()
                            
                            input('\nPasse o ID do produto que deseja:  ')
                            

                            userFavoritos.append(favorito)
                            opFav = input('Quer cadastrar mais produtos favoritos? (S/N)  ')
                        
                        usuario.insertUsuario(userNome, userSobrenome, userEndereco, userFavoritos)
                    
                    case 2:
                        usuario.todosUsuario()
                    
                    case 3:
                        print('\n------ Usuário específico ------')
                        idUs = input('Digite o ID do usuário: ')

                        print("\n------ USUÁRIO ESCOLHIDO ------")
                        usuario.idUsuario(idUs)

                    case 4:
                        print('\n------ Atualizar usuário ------')
                        idUsr = input('Digite o ID do usuário: ')

                        print("\n------ USUÁRIO ESCOLHIDO ------")
                        usuario.idUsuario(idUsr)

                        opAtu = 'S'

                        while (opAtu != 'N'):
                            campoUsr = input('\nO que deseja atualizar? ')
                            novoUsr = input('Digite o novo valor: ')

                            print('\nCampo {} atualizado'.format(campoUsr))
                            usuario.atualizaUsuario(idUsr, campoUsr, novoUsr)
                            opAtu = input('Deseja atualizar mais algum campo? (S/N) ')

                    case 6:
                        print('\n------ Deletar usuário ------')
                        idUsr = input('Digite o ID do usuário: ')

                        print("\n------ USUÁRIO DELETADO ------")
                        usuario.deletarUsuario(idUsr)
                    case _:
                        print('\nNão entendi :(')
        
        case 4:
            voltar = False
            while (voltar == False) :
                print('\n------ COMPRAR ------')
                print('1. Nova compra\n' + 
                    '2. Listar todas\n' + '3. Compra específica (ID)\n' + 
                    '4. Atualizar\n' +
                    '5. Deletar\n')
                opComp = int(input('O que deseja fazer hoje? '))

                match opComp:
                    case 1:
                        print('\n------ Nova Compra ------\n')
                        print('--> Quem está realizando a compra?\n')
                        idUser = input('Id usuáiro: ')
                        nomeUser = input('Nome usuario: ')
                        sobrenomeUser = input('Sobrenome usuario: ')
                        crompUsuario = {
                            'id' : idUser,
                            'nome' : nomeUser,
                            'sobrenome' : sobrenomeUser
                        }

                        print('--> De quem você está comprando?\n')
                        idVend = input('Id vendedor: ')
                        nomeVend = input('Nome vendedor: ')
                        sobrenomeVend = input('Sobrenome vendedor: ')
                        empresaVend = input('Empresa vendedor: ')
                        crompVendedor = {
                            'id' : idVend,
                            'nome' : nomeVend,
                            'sobrenome' : sobrenomeVend,
                            'empresa' : empresaVend
                        }


                        print('--> O que você está comprando?\n')
                        crompProdutos = []
                        crompTotal = 0
                        opProd = 'S'
                        while (opProd != 'N'):
                            idProd = input('Id produto: ')
                            nomeProd = input('Nome produto: ')
                            valorProd = int(input('Valor Produto: '))
                            produto = {
                                'nome' : nomeProd,
                                'produto' : valorProd
                            }

                            crompProdutos.append(produto)
                            crompTotal += valorProd
                            opProd = print('Deseja adicionar mais produtos? (S/N) ')


                        print('--> Quando está comprando? Para quando é?\n')
                        crompDataInicio = input('Data inicial: ')
                        crompDataFinal = input('Data final: ')
                        
                        
                        print('\nEndereço de entrega\n')
                        rua = input('Rua: ')
                        numero = input('Numero: ')
                        complemento = input('Complemento: ')
                        bairro = input('Bairro: ')
                        cidade = input('Cidade: ')
                        estado = input('Estado: ')    
                        crompEndereco = {
                            'rua' : rua,
                            'numero' : numero,
                            'complemento' : complemento,
                            'bairro' : bairro,
                            'cidade' : cidade,
                            'estado' : estado
                        }

                        compra.insertCompra(crompUsuario, crompVendedor, crompProdutos, crompTotal, crompDataInicio, crompDataFinal, crompEndereco)

                    case 2:
                        compra.todosCompra()
                    
                    case 3:
                        print('\n------ Compra específica ------')
                        idComp = input('Digite o ID da compra: ')

                        print("\n------ COMPRA ESCOLHIDO ------")
                        compra.idCompra(idComp)
                    
                    case 4:
                        print('\n------ Atualizar compra ------')
                        idComp = input('Digite o ID da compra: ')

                        print("\n------ COMPRA ESCOLHIDA ------")
                        compra.idCompra(idComp)

                        opAtu = 'S'

                        while (opAtu != 'N'):
                            campoComp = input('\nO que deseja atualizar? ')
                            novoComp = input('Digite o novo valor: ')

                            print('\nCampo {} atualizado'.format(campoComp))
                            compra.atualizaCompra(idComp, campoComp, novoComp)
                            opAtu = input('Deseja atualizar mais algum campo? (S/N) ')
                    
                    case 5:
                        print('\n------ Deletar compra ------')
                        idComp = input('Digite o ID da compra: ')

                        print("\n------ COMPRA DELETADA ------")
                        compra.deletarCompra(idComp)
                    case _:
                        print('\nNão entendi :(')
        
        case 6:
            break
        
        case _:
            print('Não entendi :(')


print('\nAté logo!')