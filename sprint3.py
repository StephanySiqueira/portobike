print("Seguro da sua bicicleta com a Porto!!!!")
cliente = dict()
bicicletas = []

def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return True

def validar_senha(senha):
    maiuscula = False
    minuscula = False
    numero = False

    for c in senha:
        if c.isupper():
            maiuscula = True
        if c.islower():
            minuscula = True
        if c.isdigit():
            numero = True

    return maiuscula and minuscula and numero

def validar_cep(cep):
    if len(cep) != 8 or not cep.isdigit():
        return False
    return True

def validar_email(email):
    return "@" in email


def cadastro():
    cliente['nome'] = input("Nome:")
    while True:
        cliente['cpf'] = input("CPF:")
        if validar_cpf(cliente['cpf']):
            break
        else:
            print("CPF inválido. Deve conter 11 dígitos numéricos.")

    cliente['dataNascimento'] = input("Data de nascimento (ex: 30102004):")

    while True:
        cliente['cep'] = input("CEP:")
        if validar_cep(cliente['cep']):
            break
        else:
            print("CEP inválido. Deve conter 8 dígitos numéricos.")

    cliente['genero'] = input("Digite o seu genero:")

    while True:
        cliente['email'] = input("Email:")
        if validar_email(cliente['email']):
            break
        else:
            print("Email inválido.")

    while True:
        cliente['senha'] = input("Senha:")
        if validar_senha(cliente['senha']):
            break
        else:
            print("Senha inválida. Deve conter pelo menos: \n* uma letra maiúscula \n* uma letra minúscula \n* um número")

    print("\n*Confirme seus dados*\n")
    for campo, valor in cliente.items():
        print(f"{campo}.........: {valor}")
    while True:
        finalizando = input("Os seus dados estão corretos (N / S)? \n").upper()
        if finalizando == "N":
            print("Refazer cadastro, selecione o número 1 novamente e preencha as informações.")
            break
        if finalizando == "S":
            print(f"{cliente['nome']} seu cadastro foi realizado!\n")
            break
        else:
            print('Opção inválida')


def listar_bicicletas():
    if not bicicletas:
        print("Não há bicicletas cadastradas.")
    else:
        print("Bicicletas cadastradas:")
        for i in range(len(bicicletas)):
            print(f"{i + 1}. Modelo: {bicicletas[i]['modelo']}, Ano de Fabricação: {bicicletas[i]['ano_fabricação']}, Nota fiscal: {bicicletas[i]['nota_fiscal']}, Numero de série: {bicicletas[i]['numero_serie']}, Parte importada: {bicicletas[i]['parte_importada']}, Tipo de seguro:{bicicletas[i]['tipo_seguro']}")


def editar_bicicleta():
    if not bicicletas:
        print("Não há bicicletas cadastradas.")
        return

    listar_bicicletas()

    opcao = input("Escolha o número da bicicleta que deseja editar: ")

    if opcao.isdigit():
        opcao = int(opcao)
        if 1 <= opcao <= len(bicicletas):
            bike_atual = bicicletas[opcao - 1]
            print(
                f"Editando bicicleta: Modelo: {bike_atual['modelo']}, Ano de Fabricação: {bike_atual['ano_fabricação']}, Nota fiscal: {bike_atual['nota_fiscal']}, Numero de série: {bike_atual['numero_serie']}, Parte importada: {bike_atual['parte_importada']}\n")

            novo_modelo = input("Novo modelo (deixe em branco para manter o mesmo): ")
            if novo_modelo:
                bike_atual['modelo'] = novo_modelo

            novo_ano = input("Novo ano de fabricação (deixe em branco para manter o mesmo): ")
            if novo_ano.isdigit():
                bike_atual['ano_fabricação'] = int(novo_ano)

            nova_nota_fiscal = input("Nova nota fiscal (deixe em branco para manter o mesmo): ")
            if nova_nota_fiscal.isdigit():
                bike_atual['nota_fiscal'] = int(nova_nota_fiscal)

            novo_numero_serie = input("Novo número de série (deixe em branco para manter o mesmo): ")
            if novo_numero_serie.isdigit():
                bike_atual['numero_serie'] = int(novo_numero_serie)

            nova_parte_importada = input("Nova parte importada (deixe em branco para manter o mesmo): ")
            if nova_parte_importada:
                bike_atual['parte_importada'] = nova_parte_importada

            print("Bicicleta atualizada com sucesso!")
        else:
            print("Opção inválida.")
    else:
        print("Opção inválida.")


def cadastrarBike():
    print(
        'Temos 3 tipos de seguro:\n 1- Pedal Essencial: \n * Coberturas Reparo de câmaras de ar \n * Reparo ou troca de correntes\n * Substituição ou regulagem de selim e canote de selim \n * Substituição e regulagem manetes de freios e cabo de aço \n * Substituição ou regulagem de freio dianteiro e traseiro \n ')
    print(
        '2- Pedal Leve: \n * Reparo de câmaras de ar \n * Reparo ou troca de correntes \n * Substituição ou regulagem de selim e canote de selim \n * Substituição e regulagem manetes de freios e cabo de aço \n * Substituição ou regulagem de freio dianteiro e traseiro \n * Lubrificação de correntes e coroas \n Diferencial:\n * Transporte do segurado e Bike - limite de 50km, em caso de quebra ou acidente \n')
    print(
        '3- Pedal Elite: \n * Reparo de câmaras de ar \n * Reparo ou troca de correntes \n * Substituição ou regulagem de selim e canote de selim \n * Substituição e regulagem manetes de freios e cabo de aço \n * Substituição ou regulagem de freio dianteiro e traseiro \n * Lubrificação de correntes e coroas \n * Transporte do segurado e Bike - limite de 50km, em caso de quebra ou acidente \n Diferencial: \n * Transporte do segurado e Bike - limite de 150km, em caso de quebra ou acidente \n * Instalação de suporte de parede e chão para bike \n * Serviço de Leva e Traz, com limite de 50km, mediante agendamento prévio \n')

    while True:
        seguro = input('Digite a opção de seguro que deseja: ')
        if seguro.isdigit():
            seguro = int(seguro)
            if seguro > 0 and seguro <= 3:
                print(f'Certo opção {seguro} selecionada!')
                print('Precisamos de algumas informações, vamos cadastrar a sua bike agora! \n')
                bike_info = {}  # Dicionário para armazenar informações da bicicleta

                bike_info['modelo'] = str(input('Modelo: '))
                bike_info['ano_fabricação'] = int(input('Ano de Fabricação: '))
                bike_info['nota_fiscal'] = int(input('Nota Fiscal: '))

                print('Informações adicionais (Se não tiver, coloque "0"): ')
                bike_info['numero_serie'] = int(input('Número de série: '))
                bike_info['parte_importada'] = str(input('Partes importadas: '))

                bike_info['tipo_seguro'] = seguro  # Adiciona o tipo de seguro à informação da bicicleta

                bicicletas.append(bike_info)  # Adiciona as informações da bicicleta à lista de bicicletas

                print('*Dados bike*\n')
                for campo, valor in bike_info.items():
                    print(f"{campo}.........: {valor}")
                break
            else:
                print("Opção inválida")
        else:
            print('Opção inválida. Digite um número.')

def bike():
    if not cliente:
        print("Se cadastre primeiro!")
    else:
        email_bike = input("Email: ")
        senha_bike = input("Senha: ")

        if email_bike == cliente['email'] and senha_bike == cliente['senha']:
            print("Bem-vindo ao menu de bicicletas!")
            while True:
                print("""
                          1- Cadastrar Bike
                          2- Listar Bicicletas Cadastradas
                          3- Editar Informações da Bicicleta
                          4- Voltar ao Menu Principal
                      """)

                opcao = input("Opção:")

                if opcao == "1":
                    cadastrarBike()
                elif opcao == "2":
                    listar_bicicletas()
                elif opcao == "3":
                    editar_bicicleta()
                elif opcao == "4":
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Email ou senha incorretos.")


def refazer():
    if not cliente:
        print("Não há cadastros")
    else:
        email = input("Email: ")
        senha = input("Senha: ")

        if email == cliente['email'] and senha == cliente['senha']:
            for campo, valor in cliente.items():
                print(f"{campo}.........: {valor}")

            campos = input("\nO que deseja editar (exemplo: nome): ")
            if campos in cliente:
                novo_valor = input(f"Digite um novo valor para '{campos}': ")
                cliente[campos] = novo_valor
            else:
                print("Campo não encontrado")
        else:
            print("Email ou senha incorretos.")

def verificar():
    if not cliente:
        print("Não há cadastros!")
    else:
        for campo, valor in cliente.items():
            print(f"{campo}.........: {valor}")

def cancelar():
    if not cliente:
        print("Não há cadastros")
    else:
        email = input("Email: ")
        senha = input("Senha: ")
        if email == cliente['email'] and senha == cliente['senha']:
            print("""
                   Motivos para cancelamento:
                   1 - Vendi minha bicicleta
                   2 - Comprei um seguro com outra empresa
                   3 - Não uso mais a bicicleta
                   4 - Outro motivo
               """)
            motivo_opcao = input("Escolha o motivo para cancelar: ")
            if motivo_opcao == "1":
                motivo = "Vendi minha bicicleta"
            elif motivo_opcao == "2":
                motivo = "Comprei um seguro com outra empresa"
            elif motivo_opcao == "3":
                motivo = "Não uso mais a bicicleta"
            elif motivo_opcao == "4":
                motivo = input("Digite o motivo: ")
            else:
                print("Opção inválida.")
                return
            print(f"Pedido de cancelamento recebido. Motivo: {motivo}")
            print('Iremos encaminhá-lo para nosso atendente para ajudar melhor...')
        else:
            print("Email ou senha incorretos.")


while True:
    print("""
        1- Cadastrar
        2- Dados Bike
        3- Refazer cadastro
        4- Verificar Cadastro
        5- Cancelar Seguro
        0- Sair
    """)
    opcao = input("Opção:")

    if opcao == "0":
        print('Obrigado por entrar em contato com a Porto!!')
        break
    elif opcao == "1":
        cadastro()
    elif opcao == "2":
        bike()
    elif opcao == "3":
        refazer()
    elif opcao == "4":
        verificar()
    elif opcao == "5":
        cancelar()
    else:
        print("Opção inválida")