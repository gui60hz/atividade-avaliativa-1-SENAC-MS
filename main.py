import json
import funcoes as func
import save as s
from datetime import datetime
from pathlib import Path

base = Path(__file__).parent

while True:
    func.Menu_login_usuarios()

    opicao = int(input("Digite uma opção: "))

    if opicao == 1:
        if func.Validar_usuarios_admin():
            
            func.Menu_admin()

            op = int(input("Digite uma opção: "))

            encontrado = False

            if op == 1:
                func.Menu_admin_usuarios()

                op = int(input("Digite uma opção: "))

                if op == 1:
                    lista_usuarios = s.Carregar_arquivo_usuarios()
                    usuario = input("Digite o usuário: ")
                    senha = input("Digite a senha: ")
                    nivel = input("Digite o nível do usuário: ")
                    new_dict = {
                            "id": len(lista_usuarios) + 1,
                            "usuario": usuario,
                            "senha": senha,
                            "nivel": nivel
                        }
                    lista_usuarios.append(new_dict)
                    s.Salvar_arquivo_usuarios(lista_usuarios)
                    
                    print("Cadastro realizado com sucesso!")

                elif op == 2:
                    lista_usuarios = s.Carregar_arquivo_usuarios()
                    usuario = input("Digite o usuário: ")
                    for i in lista_usuarios:
                        if usuario == i["usuario"]:
                            print(f"1 - Usuario: {i["usuario"]}")
                            print(f"2 - Senha: {i["senha"]}")
                            print(f"3 - Nível de acesso: {i["nivel"]}")

                            op = int(input("Qual informação deseja editar: "))

                            if op == 1:
                                i["usuario"] = input("Digite o novo usuário: ")
                            elif op == 2:
                                i["senha"] = input("Digite a nova senha: ")
                            elif op == 3:
                                i["nivel"] = input("Digite o novo nível: ")

                            s.Salvar_arquivo_usuarios(lista_usuarios)

                            print("Alteração salva com sucesso!")

                elif op == 3:
                    lista_usuarios = s.Carregar_arquivo_usuarios()
                    usuario = input("Digite o usuário: ")
                    for i in lista_usuarios:
                        if usuario == i["usuario"]:
                            lista_usuarios.remove(i)
                            s.Salvar_arquivo_usuarios(lista_usuarios)
                            print("Usuário removido!")
                
                elif op == 4:
                    lista_usuarios = s.Carregar_arquivo_usuarios()
                    usuario = input("Digite o usuário: ")
                    for i in lista_usuarios:
                        if usuario == i["usuario"]:
                            print(f"Senha atual: {i["senha"]}")
                            nova_senha = input("Digite a nova senha: ")
                            i["senha"] = nova_senha
                            s.Salvar_arquivo_usuarios(lista_usuarios)
                            print(f"Alteração concluida!\nNova senha: {i["senha"]}")

                elif op == 5:
                    lista_usuarios = s.Carregar_arquivo_usuarios()
                    print("-----LISTA DE USUÁRIOS-----")
                    for i in lista_usuarios:
                        print(f"{i["id"]} - {i["usuario"]}")

                elif op == 6:
                    func.Menu_admin()

            elif op == 2:
                    func.Menu_admin_medicos()

                    op = int(input("Digite um opção: "))

                    if op == 1:
                        lista_medicos = s.Carregar_arquivo_medicos()
                        nome_medico = input("Digite o nome do médico: ")
                        especialidade = input("Digite a especialidade do médico: ")
                        crm_medico = input("Digite o CRM do médico: ")
                        new_dict = {
                            "id": len(lista_medicos) + 1,
                            "nome": nome_medico,
                            "especialidade": especialidade,
                            "crm": crm_medico
                        }
                        lista_medicos.append(new_dict)
                        s.Salvar_arquivo_medicos(lista_medicos)
                        print("Cadastro realizado com sucesso!")
                    
                    elif op == 2:
                        lista_medicos = s.Carregar_arquivo_medicos()

                        for i in lista_medicos:
                            print(f"{i['id']} - {i['nome']}")
                            
                        id_medico = int(input("Digite a opção desejada: "))

                        for i in lista_medicos:
                            if id_medico == i["id"]:
                                print(f"1 - Nome: {i["nome"]}")
                                print(f"2 - Especialidade: {i["especialidade"]}")
                                print(f"3 - CRM: {i["crm"]}")

                                op = int(input("Qual informação deseja editar: "))

                                if op == 1:
                                    i["nome"] = input("Digite o novo nome: ")
                                elif op == 2:
                                    i["especialidade"] = input("Digite a nova especialidade: ")
                                elif op == 3:
                                    i["crm"] = input("Digite o novo CRM: ")

                                s.Salvar_arquivo_medicos(lista_medicos)

                                print("Alteração salva com sucesso!")

                    elif op == 3:
                        lista_medicos = s.Carregar_arquivo_medicos()

                        for i in lista_medicos:
                            print(f"{i['id']} - {i['nome']}")

                        id_medico = int(input("Digite a opção que deseja excluir: "))

                        for i in lista_medicos:
                            if i["id"] == id_medico:
                                lista_medicos.remove(i)
                                s.Salvar_arquivo_medicos(lista_medicos)
                                print("Usuário removido!")

                    elif op == 4:
                        lista_medicos = s.Carregar_arquivo_medicos()
                        print("-----LISTA DE MÉDICOS-----")
                        for i in lista_medicos:
                            print(f"{i['id']} - {i['nome']}")

            elif op == 3:
                func.Menu_admin_pacientes()

                op = int(input("Digite a opção desejada: "))

                if op == 1:
                    lista_pacientes = s.Carregar_arquivo_pacientes()

                    for i in lista_pacientes:
                        print(f"{i["id"]} - {i["nome"]}")

                elif op == 2:
                    lista_pacientes = s.Carregar_arquivo_pacientes()

                    busca_id = int(input("Digite o id do paciente: "))

                    for i in lista_pacientes:
                        if i["id"] == busca_id:
                            print(f"Nome: {i["nome"]}")
                            print(f"Idade: {i["idade"]}")
                            print(f"CPF: {i["cpf"]}")
                            print(f"Telefone: {i["telefone"]}")
                            print(f"Endereço: {i["endereco"]}")

                elif op == 3:
                    lista_consultas = s.Carregar_arquivo_consultas()
                    lista_pacientes = s.Carregar_arquivo_pacientes()

                    for i in lista_pacientes:
                        print(f"{i["id"]} - {i["nome"]}")

                    busca_historico = int(input("Digite o id do paciente: "))

                    for i in lista_consultas:
                        if i["id_paciente"] == busca_historico:
                            print(f"ID do médico: {i["id_medico"]}")
                            print(f"Data da consulta: {i["data"]}")
                            print(f"Horário: {i["hora"]}")
                            print(f"Status: {i["status"]}")
                            print("\n-------------------------------")

            elif op == 4:
                func.Menu_admin_consultas()

                op = int(input("Digite a opção desejada: "))

                if op == 1:
                    lista_consultas = s.Carregar_arquivo_consultas()

                    for i in lista_consultas:
                        print(f"ID do paciente: {i["id_paciente"]}")
                        print(f"ID do médico: {i["id_medico"]}")
                        print(f"Data da consulta: {i["data"]}")
                        print(f"Horário: {i["hora"]}")
                        print(f"Status: {i["status"]}")
                        print("\n-------------------------------")

                elif op == 2:
                    lista_consultas = s.Carregar_arquivo_consultas()

                    print(f"-----CONSULTAS AGENDADAS-----")

                    for i in lista_consultas:
                        if i["status"] == "Agendada":
                            print(f"Data: {i["data"]} | Horário: {i["hora"]} | ID do médico: {i["id_medico"]}")
                            print("\n--------------------------------------------------------------------------")

            elif op == 5:
                func.Menu_admin_relatorios()

                op = int(input("Digite a opção desejada: "))

                if op == 1:
                    lista_consultas = s.Carregar_arquivo_consultas()

                    data_inicio = datetime.strptime(input("Data início (dd/mm/aaaa): "), "%d/%m/%Y")
                    data_fim = datetime.strptime(input("Data fim (dd/mm/aaaa): "), "%d/%m/%Y")

                    total = 0

                    for i in lista_consultas:
                        if i["status"] == "Finalizada":
                            data_consulta = datetime.strptime(i["data"], "%d/%m/%Y")

                            if data_inicio <= data_consulta <= data_fim:
                                total += 1

                    print("Total de consultas realizadas:", total)

                elif op == 2:
                    lista_consultas = s.Carregar_arquivo_consultas()

                    total = 0

                    for i in lista_consultas:
                        if i["status"] == "Cancelada":
                            total += 1
                        
                    print(f"Total de consultas canceladas: {total}")

    else:
        print("Informação não permitida para esse usuários")