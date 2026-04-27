import json
from pathlib import Path

base = Path(__file__).parent

def Validar_usuarios_admin():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    with open(base / "arquivos json/usuarios.json", "r", encoding="utf-8") as f:
        conteudo = json.load(f)

    login_sucesso = False

    for i in conteudo:
        if usuario == i["usuario"] and senha == i["senha"]:
            if i["nivel"] == "admin":
                print("Login bem-sucedido!")
                return True

    if not login_sucesso:
            print("Você não possui acesso a essa informação!")
            return login_sucesso

def Menu_login_usuarios():
    print("-----MENU DE LOGIN-----")
    print("1 - Administrador")
    print("2 - Medico")
    print("3 - Recepcionista")
    print("4 - Sair")

def Menu_admin():
    print("-----MENU DE ADMINISTRADOR-----")
    print("1 - Usuários")
    print("2 - Médicos")
    print("3 - Pacientes")
    print("4 - Consultas")
    print("5 - Relatórios")
    print("6 - Sair")

def Menu_admin_usuarios():
    print("-----MENU DE USUÁRIOS-----")
    print("1 - Cadastrar usuários no sistema")
    print("2 - Editar usuários")
    print("3 - Excluir usuários")
    print("4 - Resetar senha de usuários")
    print("5 - Listar todos os usuários")
    print("6 - Voltar")

def Menu_admin_medicos():
    print("-----MENU DE MÉDICOS-----")
    print("1 - Cadastrar médicos")
    print("2 - Editar médicos")
    print("3 - Excluir médicos")
    print("4 - Listar médicos cadastrados")

def Menu_admin_pacientes():
    print("-----MENU DE PACIENTES-----")
    print("1 - Visualizar todos pacientes")
    print("2 - Buscar Pacientes")
    print("3 - Ver histórico completo")

def Menu_admin_consultas():
    print("-----MENU DE CONSULTAS-----")
    print("1 - Visualizar todas as consultas")
    print("2 - Consultar agenda geral")

def Menu_admin_relatorios():
    print("-----MENU DE RELATÓRIOS-----")
    print("1 - Total de consultas realizadas por período")
    print("2 - Total de consultas canceladas")
    print("3 - Quantidade de pacientes cadastrados")
    print("4 - Quantidade de médicos ativos")
    print("5 - Consultas por médico")
    print("6 - Atendimentos realizados no dia")
    print("7 - Pacientes mais atendidos")




