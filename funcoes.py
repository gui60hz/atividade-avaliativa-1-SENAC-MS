#--------------------------IMPORTS-------------------------------------------------------------------
import json
import save as s
from pathlib import Path
from datetime import datetime

base = Path(__file__).parent

#--------------------------ADMINISTRADOR-------------------------------------------------------------------

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
    print("2 - Recepcionista")
    print("3 - Médico")
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
    print("6 - Sair")

def Menu_admin_medicos():
    print("-----MENU DE MÉDICOS-----")
    print("1 - Cadastrar médicos")
    print("2 - Editar médicos")
    print("3 - Excluir médicos")
    print("4 - Listar médicos cadastrados")
    print("5 - Sair")

def Menu_admin_pacientes():
    print("-----MENU DE PACIENTES-----")
    print("1 - Visualizar todos pacientes")
    print("2 - Buscar Pacientes")
    print("3 - Ver histórico completo")
    print("4 - Sair")

def Menu_admin_consultas():
    print("-----MENU DE CONSULTAS-----")
    print("1 - Visualizar todas as consultas")
    print("2 - Consultar agenda geral")
    print("3 - Sair")

def Menu_admin_relatorios():
    print("-----MENU DE RELATÓRIOS-----")
    print("1 - Total de consultas realizadas por período")
    print("2 - Total de consultas canceladas")
    print("3 - Quantidade de pacientes cadastrados")
    print("4 - Quantidade de médicos ativos")
    print("5 - Consultas por médico")
    print("6 - Atendimentos realizados no dia")
    print("7 - Pacientes mais atendidos")
    print("8 - Sair")


#--------------------------RECEPCIONISTA-------------------------------------------------------------------

def Data_hoje():
    data_hoje = datetime.now().date()
    print(f"Data: {data_hoje}")

def Validar_login_recepionista():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    with open(base / "arquivos json/usuarios.json", "r", encoding="utf-8") as f:
        conteudo = json.load(f)

    lista_usuarios = conteudo

    login_sucesso = False

    for i in lista_usuarios:
        if usuario == i["usuario"] and senha == i["senha"]:
            if i["nivel"] == "recepcionista":
                print("Login bem-sucedido!")
                login_sucesso = True
                return True
            
    if not login_sucesso:
            print("Você não possui acesso a essa informação!")
  
def Consultas_hoje():
    lista_consultas = s.Carregar_arquivo_consultas() 

    data_hoje = datetime.now().date()

    consultas_hoje = 0

    for consulta in lista_consultas:
        data_consulta = datetime.strptime(consulta["data"], "%d/%m/%Y").date()
        
        if data_consulta == data_hoje:
            consultas_hoje += 1

    print(f"Consultas hoje: {consultas_hoje}")

def Pacientes_cadastrados():
    lista_pacientes = s.Carregar_arquivo_pacientes()

    total = len(lista_pacientes)

    print(f"Total de pacientes cadastrados: {total}")

def Medicos_ativos():
    lista_medicos = s.Carregar_arquivo_medicos()

    total = 0

    for i in lista_medicos:
        total += 1

    print(f"Total de médicos ativos: {total}")

def Atendimentos_finalizados_hoje():
    lista_consultas = s.Carregar_arquivo_consultas() 

    data_hoje = datetime.now().date()

    atendi_fim_hoje = 0

    for consulta in lista_consultas:
        data_consulta = datetime.strptime(consulta["data"], "%d/%m/%Y").date()
        
        if data_consulta == data_hoje and consulta["status"] == "Finalizada":
            atendi_fim_hoje += 1
    
    print(f"Atendimentos finalizados hoje: {atendi_fim_hoje}")

def Consultas_canceladas_hoje():
    lista_consultas = s.Carregar_arquivo_consultas() 

    data_hoje = datetime.now().date()

    cons_cancel_hoje = 0

    for consulta in lista_consultas:
        data_consulta = datetime.strptime(consulta["data"], "%d/%m/%Y").date()
        
        if data_consulta == data_hoje and consulta["status"] == "Cancelada":
            cons_cancel_hoje += 1
    
    print(f"Consultas finalizadas hoje: {cons_cancel_hoje} ")

def Menu_recepcionista():
    print("-----MENU RECEPÇÃO-----")
    print("1 - Pacientes")
    print("2 - Consultas")
    print("3 - Histórico")
    print("4 - Relatórios")
    print("5 - Sair")