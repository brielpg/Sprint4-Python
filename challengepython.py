import oracledb
import json


def exportar_json(dados):
    nome_arquivo = input("Digite o nome do arquivo JSON para exportar: ")
    if not nome_arquivo:
        nome_arquivo = "dados_exportados"
    nome_arquivo += ".json"
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f)
    print(f"Dados exportados para {nome_arquivo} com sucesso!")


def verificar_login_senha_corretos():
    try:
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        senha = str(input("Senha: "))
        cursor.execute(f"SELECT * FROM {TABELA} WHERE nome = '{nome}' AND email_usuario = '{email}' AND senha = '{senha}'")
        for i in cursor:
            if i[1] == nome and i[5] == email and i[12] == senha:
                print("Logado com sucesso!\n")
                return True, i[1], i[5], i[12]
        return False
    except Exception as e:
        print("Erro: ", e)


def create():
    try:
        nome = str(input("Nome: "))
        sobrenome = str(input("Sobrenome: "))
        cpf_usuario = str(input("CPF: "))
        cargo = str(input("Cargo: "))
        email_usuario = str(input("Email: "))
        telefone = str(input("Telefone: "))
        empresa = str(input("Empresa: "))
        nr_funcionario = int(input("Nº de Funcionários: "))
        pais = str(input("País: "))
        idioma = str(input("Idioma: "))
        senha_usuario = str(input("Senha: "))

        cursor.execute(
            f"INSERT INTO {TABELA} "
            f"(nome, sobrenome, cpf_usuario, cargo, email_usuario, telefone, empresa, nr_funcionarios, pais, idioma, senha) "
            f"VALUES "
            f"('{nome}', '{sobrenome}', '{cpf_usuario}', '{cargo}', '{email_usuario}', '{telefone}', '{empresa}', {nr_funcionario}, '{pais}', '{idioma}', '{senha_usuario}')")
        conn.commit()

        print("Dado adicionado ao database com sucesso!")
    except ValueError:
        print("Número de funcionários inválido!")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        input("Pressione \"ENTER\" para retornar ao menu")


def read():
    try:
        informacao = int(input("O que deseja verificar?\n1. Todos os cadastros\n2. Um cadastro específico\nOpcao: "))
        if informacao == 1:
            cursor.execute(f"SELECT * FROM {TABELA}")
            for i in cursor:
                print(i)
            dados = cursor.fetchall()

            deseja_exportar = str(input("Deseja exportar os dados para um arquivo Json? S/N ")).lower()
            if deseja_exportar == "s" or deseja_exportar == "sim":
                exportar_json(dados)
        elif informacao == 2:
            index = int(input("Digite o index (valor referente a posição do dado) que deseja verificar: "))
            cursor.execute(f"SELECT * FROM {TABELA} WHERE id_usuario = {index}")
            for i in cursor:
                print(i)
            dados = cursor.fetchall()

            deseja_exportar = str(input("Deseja exportar os dados para um arquivo Json? S/N ")).lower()
            if deseja_exportar == "s" or deseja_exportar == "sim":
                exportar_json(dados)
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        input("Pressione \"ENTER\" para retornar ao menu")


def update():
    try:
        print("Antes de realizar a atualização dos dados precisamos verificar se é você mesmo.")
        login_realizado, nome, email, senha = verificar_login_senha_corretos()
        if login_realizado:
            nome_novo = input("Novo nome: ")
            sobrenome = input("Novo sobrenome: ")
            cpf_usuario = input("Novo CPF: ")
            cargo = input("Novo cargo: ")
            email_usuario = input("Novo email: ")
            telefone = input("Novo telefone: ")
            empresa = input("Nova empresa: ")
            nr_funcionario = int(input("Novo Nº de Funcionário: "))
            pais = input("Novo país: ")
            idioma = input("Novo idioma: ")
            senha_nova = input("Nova senha: ")

            cursor.execute(f"UPDATE {TABELA} SET nome='{nome_novo}', sobrenome='{sobrenome}', cpf_usuario='{cpf_usuario}', "
                           f"cargo='{cargo}', email_usuario='{email_usuario}', telefone='{telefone}', empresa='{empresa}', "
                           f"nr_funcionarios={nr_funcionario}, pais='{pais}', idioma='{idioma}', senha='{senha_nova}' WHERE nome = '{nome}' AND email_usuario = '{email}' AND senha = '{senha}'")
            conn.commit()
            print("Dados atualizados com sucesso!")
    except ValueError:
        print("Número de funcionários inválido!")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        input("Pressione ENTER para retornar ao menu")


def delete():
    try:
        print("Obs: você só pode deletar os usuários que tem acesso, ou seja, somente os usuários que você tem login e senha.")
        print("Antes de realizar o delete dos dados precisamos verificar se é você mesmo.")
        login_realizado, nome, email, senha = verificar_login_senha_corretos()
        if login_realizado:
            certeza = str(input(f"Tem certeza que deseja deletar o usuário \"{nome}\" da tabela? (Sim/Nao) ")).lower()
            if certeza == "sim" or certeza == "s":
                cursor.execute(f"DELETE FROM {TABELA} WHERE nome = '{nome}' AND email_usuario = '{email}' AND senha = '{senha}'")
                print("Dado deletado com sucesso!")
                conn.commit()
    except ValueError:
        print("Número de funcionários inválido!")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        input("Pressione ENTER para retornar ao menu")


def menu():
    print("Escolha a opção desejada!")
    print("1. Criar (CREATE)")
    print("2. Ler (READ)")
    print("3. Atualizar (UPDATE)")
    print("4. Deletar (DELETE)")
    print("5. Sair")


TABELA = "T_PS_USUARIO"
usuarioOracle = 'RM552798'
senhaOracle = '050803'

try:
    dsnStr = oracledb.makedsn("oracle.fiap.com.br", 1521, "ORCL")
    conn = oracledb.connect(user=usuarioOracle, password=senhaOracle, dsn=dsnStr)
    cursor = conn.cursor()
except Exception as e:
    print("Erro: ", e)


while True:
    menu()
    try:
        opcao = int(input("Opção: "))
    except ValueError:
        print("Valor Inválido!")
    else:
        if opcao == 1:
            create()
        elif opcao == 2:
            read()
        elif opcao == 3:
            update()
        elif opcao == 4:
            delete()
        elif opcao == 5:
            cursor.close()
            conn.close()
            break
        else:
            print("Opção Inválida!")
    finally:
        pass
