agenda = {}

def menu():
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Listar contatos")
    print("4 - Limpar agenda")
    print("5 - Buscar contato")
    print("6 - Ver agenda completa")
    print("7 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha
while True:
    escolha = menu()
    if escolha == "1":
        nome = input("Nome do contato: ")
        endereco = input("Endereço do contato: ")
        telefone = input("Telefone do contato: ")
        agenda[nome] = {"endereco": endereco, "telefone": telefone}
        print(f"Contato {nome} adicionado.")
    elif escolha == "2":
        nome = input("Nome do contato a remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato {nome} removido.")
        else:
            print("Contato não encontrado.")
    elif escolha == "3":
        for nome, info in agenda.items():
            print(f"Nome: {nome}, Endereço: {info['endereco']}, Telefone: {info['telefone']}")
    elif escolha == "4":
        agenda.clear()
        print("Agenda limpa.")
    elif escolha == "5":
        usuario = input("Digite o nome do usuário: ")
        if usuario in agenda:
            print(f"Endereço: {agenda[usuario]['endereco']}")
            print(f"Telefone: {agenda[usuario]['telefone']}")
        else:
            print("Usuário não encontrado na agenda.")
    elif escolha == "6":
        for nome, info in agenda.items():
            print(f"Nome: {nome}, Endereço: {info['endereco']}, Telefone: {info['telefone']}")
    elif escolha == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")