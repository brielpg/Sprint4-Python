def verificar_nome():
    nome = input("Nome: ")
    if len(nome) > 1:
        return nome


def verificar_sobrenome():
    sobrenome = input("Sobrenome: ")
    if len(sobrenome) > 1:
        return sobrenome


def verificar_cpf():
    cpf = input("CPF: ")
    if len(cpf) == 11:
        return cpf


def verificar_cargo():
    cargo = input("Cargo: ")
    if len(cargo) > 1:
        return cargo
