agenda = {
    "Paulo": {
        "endereco": "Rua dos Bobos, 0",
        "telefone": "(11) 99999-9999",
    },
    "Ana": {
        "endereco": "Rua das Flores, 1",
        "telefone": "(11) 88888-8888",
    },
}

def lerdados():
    usuario = input("Digite o nome do usuário: ")
    if usuario in agenda:
        print(f"Endereço: {agenda[usuario]['endereco']}")
        print(f"Telefone: {agenda[usuario]['telefone']}")
    else:
        print("Usuário não encontrado na agenda.")