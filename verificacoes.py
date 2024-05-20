import re


def verify_data(valor: str):
    while True:
        dado = input(f"{valor}: ")
        if len(dado) > 0:
            return dado
        print(f"{valor} inválido, tente novamente!")


def verificar_cpf():
    while True:
        cpf = input("CPF: ")
        if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf):
            return cpf
        print("CPF inválido, tente novamente!")


def verificar_email():
    while True:
        email = input("Email: ")
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return email
        print("Email inválido, tente neste formato xxx@yyy.zzz")


def verificar_nfuncionarios():
    while True:
        nr_funcionarios = int(input("Nº de Funcionários: "))
        if nr_funcionarios > 0:
            return nr_funcionarios
        print("Valor inválido")
