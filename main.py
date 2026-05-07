import json
import funcoes as func
import save as s
from datetime import datetime
from pathlib import Path

base = Path(__file__).parent

while True:
    func.Menu_login_usuarios()

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        if func.Validar_usuarios_admin():
            
            while True:
                func.Menu_admin()

                op = int(input("Digite uma opção: "))

                encontrado = False

                if op == 1:
                    func.Menu_admin_usuarios()

                    op = int(input("Digite uma opção: "))

                    if op == 1:
                        lista_usuarios = s.Carregar_arquivo_usuarios()
                        lista_medicos = s.Carregar_arquivo_medicos()

                        usuario = input("Digite o usuário: ")
                        senha = input("Digite a senha: ")
                        nivel = input("Digite o nível do usuário: ")

                        novo_id = func.Gerar_proximo_id(lista_usuarios)
                        new_dict_medico = None

                        if nivel == "medico":
                            nome_medico = input("Digite o nome do médico: ")
                            especialidade = input("Digite a especialidade do médico: ")
                            crm_medico = input("Digite o CRM do médico: ")

                            new_dict_medico = {
                                    "id": novo_id,
                                    "nome": nome_medico,
                                    "especialidade": especialidade,
                                    "crm": crm_medico
                                }

                        new_dict = {
                                "id": novo_id,
                                "usuario": usuario,
                                "senha": senha,
                                "nivel": nivel
                            }
                        lista_usuarios.append(new_dict)
                        s.Salvar_arquivo_usuarios(lista_usuarios)

                        if new_dict_medico is not None:
                            lista_medicos.append(new_dict_medico)
                            s.Salvar_arquivo_medicos(lista_medicos)
                        
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
                        print("Voltando!")
                        break

                elif op == 2:
                        while True:
                            func.Menu_admin_medicos()

                            op = int(input("Digite um opção: "))

                            if op == 1:
                                lista_medicos = s.Carregar_arquivo_medicos()
                                lista_usuarios = s.Carregar_arquivo_usuarios()
                                novo_id = func.Gerar_proximo_id(lista_usuarios)
                                usuario = input("Digite o usuario do medico: ")
                                senha = input("Digite a senha do medico: ")
                                nome_medico = input("Digite o nome do médico: ")
                                especialidade = input("Digite a especialidade do médico: ")
                                crm_medico = input("Digite o CRM do médico: ")
                                new_dict_usuario = {
                                    "id": novo_id,
                                    "usuario": usuario,
                                    "senha": senha,
                                    "nivel": "medico"
                                }
                                new_dict = {
                                    "id": novo_id,
                                    "nome": nome_medico,
                                    "especialidade": especialidade,
                                    "crm": crm_medico
                                }
                                lista_usuarios.append(new_dict_usuario)
                                lista_medicos.append(new_dict)
                                s.Salvar_arquivo_usuarios(lista_usuarios)
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
                            
                            elif op == 5:
                                print("Voltando!")
                                break

                elif op == 3:
                    while True:
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
                            print("Voltando!")
                            break

                elif op == 4:
                    while True:
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

                        elif op == 3:
                            print("Voltando!")
                            break

                elif op == 5:
                    while True:
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
                        
                        elif op == 3:
                            lista_pacientes = s.Carregar_arquivo_pacientes()

                            total = 0

                            for i in lista_pacientes:
                                total += 1

                            print(f"Total de pacientes cadastrados: {total}")

                        elif op == 4:
                            lista_medicos = s.Carregar_arquivo_medicos()

                            total = 0

                            for i in lista_medicos:
                                total += 1

                            print(f"Total de médicos ativos: {total}")
                        
                        elif op == 5:
                            lista_consultas = s.Carregar_arquivo_consultas()
                            lista_medicos = s.Carregar_arquivo_medicos()

                            for i in lista_medicos:
                                print(f"ID do médico: {i["id"]} | Nome do médico: {i["nome"]}")

                            busca_id_medico = int(input("Digite o id do médico: "))
                            
                            total = 0

                            for i in lista_consultas:
                                if i["id_medico"] == busca_id_medico:
                                    total += 1
                            
                            print(f"Total de consultas: {total} ")

                        elif op == 6:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            busca_data = input("Digite a data que deseja (dia/mês/ano): ")

                            total = 0

                            for i in lista_consultas:
                                if i["data"] == busca_data and i["status"] == "Finalizada":
                                    total += 1

                            print(f"Total de atendimentos realizados no dia {busca_data}: {total}")

                        elif op == 7:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            ids = [i["id_paciente"] for i in lista_consultas]

                            mais_repetido = max(set(ids), key=ids.count)
                            quantidade = ids.count(mais_repetido)

                            print(f"O paciente mais atendido é o ID {mais_repetido} e aparece {quantidade} vezes")
                        
                        elif op == 8:
                            print("Voltando!")
                            break

    elif opcao == 2:
        if func.Validar_login_recepionista():
            func.Data_hoje()
            func.Consultas_hoje()
            func.Pacientes_cadastrados()
            func.Medicos_ativos()
            func.Atendimentos_finalizados_hoje()
            func.Consultas_canceladas_hoje()

            while True:
                func.Menu_recepcionista()

                op = int(input("Digite a opção que deseja acessar: "))

                if op == 1:
                    while True:
                        print("-----MENU RECEPÇÃO PACIENTES-----")
                        print("1 - Cadastrar paciente")
                        print("2 - Editar paciente")
                        print("3 - Buscar paciente específico")
                        print("4 - Listar todos os pacientes")
                        print("5 - Visualizar dados completos")
                        print("6 - Sair")

                        op = int(input("Digite a opção que deseja acessar: "))

                        if op == 1:
                            lista_pacientes = s.Carregar_arquivo_pacientes()
                            
                            nome = input("Digite o nome do paciente: ")
                            idade = int(input("Digite a idade do paciente: "))
                            cpf = input("Digite o CPF do paciente: ")
                            telefone = input("Digite o telefone do paciente: ")
                            endereco = input("Digite o endereço do paciente: ")

                            new_dict = {
                                "id": len(lista_pacientes) + 1,
                                "nome": nome,
                                "idade": idade,
                                "cpf": cpf,
                                "telefone": telefone,
                                "endereco": endereco
                            }
                            
                            lista_pacientes.append(new_dict)

                            s.Salvar_arquivo_pacientes(lista_pacientes)

                            print("Paciente cadastrado com sucesso!")
                            break

                        elif op == 2:
                            lista_pacientes = s.Carregar_arquivo_pacientes()

                            for i in lista_pacientes:
                                print(f"ID: {i["id"]} - Nome: {i["nome"]}")

                            op = int(input("Digite o ID que deseja editar: "))

                            encontrado = False

                            for i in lista_pacientes:
                                if i["id"] == op:
                                    print(f"1 - Nome: {i["nome"]}")
                                    print(f"2 - Idade: {i["idade"]}")
                                    print(f"3 - CPF: {i["cpf"]}")
                                    print(f"4 - Telefone: {i["telefone"]}")
                                    print(f"5 - Endereço: {i["endereco"]}")

                                    op = int(input("Digite a opção que deseja editar: "))

                                    if op == 1:
                                        i["nome"] = input("Digite o novo nome: ")
                                    elif op == 2:
                                        i["idade"] = int(input("Digite a nova idade: "))
                                    elif op == 3:
                                        i["cpf"] = input("Digite o novo CPF: ")
                                    elif op == 4:
                                        i["telefone"] = input("Digite o novo telefone: ")
                                    elif op == 5:
                                        i["endereco"] = input("Digite o novo endereço: ")
                                    
                                    s.Salvar_arquivo_pacientes(lista_pacientes)

                                    encontrado = True
                                    
                                    print("Alteração salva com sucesso!")
                                    break
                                
                            if not encontrado:
                                print("ID não encontrado!")

                        elif op == 3:
                            lista_pacientes = s.Carregar_arquivo_pacientes()

                            busca_paciente = int(input("Digite o ID do paciente: "))

                            encontrado = False

                            for i in lista_pacientes:
                                if i["id"] == busca_paciente:
                                    print(f"1 - Nome: {i["nome"]}")
                                    print(f"2 - Idade: {i["idade"]}")
                                    print(f"3 - CPF: {i["cpf"]}")
                                    print(f"4 - Telefone: {i["telefone"]}")
                                    print(f"5 - Endereço: {i["endereco"]}")
                                    
                                    encontrado = True
                                    break
                            if not encontrado:
                                print("ID não localizado!")

                        elif op == 4:
                            lista_pacientes = s.Carregar_arquivo_pacientes()

                            for i in lista_pacientes:
                                print(f"ID: {i["id"]} - {i["nome"]}")

                        elif op == 5:
                            lista_pacientes = s.Carregar_arquivo_pacientes()

                            for i in lista_pacientes:
                                print(f"ID: {i["id"]} - {i["nome"]}")

                            busca_paciente = int(input("Digite o ID do paciente: "))

                            encontrado = False

                            for i in lista_pacientes:
                                if i["id"] == busca_paciente:
                                    print(f"1 - Nome: {i["nome"]}")
                                    print(f"2 - Idade: {i["idade"]}")
                                    print(f"3 - CPF: {i["cpf"]}")
                                    print(f"4 - Telefone: {i["telefone"]}")
                                    print(f"5 - Endereço: {i["endereco"]}")
                                    
                                    encontrado = True
                                    break

                            if not encontrado:
                                print("ID não localizado!")

                        elif op == 6:
                            print("Voltando!")
                            break

                elif op == 2:
                    while True:
                        print("-----MENU RECEPÇÃO CONSULTAS-----")
                        print("1 - Marcar consulta para médico específico")
                        print("2 - Reagendar consulta")
                        print("3 - Cancelar consulta")
                        print("4 - Confirmar presença")
                        print("5 - Listar todas as consultas do dia")
                        print("6 - Listar consultas futuras")
                        print("7 - Sair")

                        op = int(input("Digite a opção que deseja acessar: "))

                        if op == 1:
                            lista_consultas = s.Carregar_arquivo_consultas()
                            lista_medicos = s.Carregar_arquivo_medicos()

                            data = input("Digite a data da consulta: ")
                            hora = input("Digite a hora da consulta: ")

                            for i in lista_medicos:
                                print(f"ID médico: {i["id"]} - {i["nome"]}")

                            op = int(input("Digite o ID do médico: "))

                            encontrado = False

                            for i in lista_consultas:
                                if i["id_medico"] == op and i["data"] == data and i["hora"] == hora:
                                    print("Nesse horário e dia esse médico já tem consulta!")
                                    encontrado = True

                                if not encontrado:
                                    new_dict = {
                                        "id": len(lista_consultas) + 1,
                                        "id_paciente": int(input("Digite o ID do paciente: ")),
                                        "id_medico": op,
                                        "data": data,
                                        "hora": hora,
                                        "status": "Agendada"
                                        }
                                    
                                    lista_consultas.append(new_dict)

                                    s.Salvar_arquivo_consultas(lista_consultas)

                                    print("Consulta agendada com sucesso!")
                                    break
                        
                        elif op == 2:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            for i in lista_consultas:
                                if i["status"] == "Agendada":
                                    print(f"ID: {i["id"]} | DATA: {i["data"]} | HORÁRIO: {i["hora"]}")

                            id_consulta = int(input("Digite o id da consulta: "))

                            encontrado = False

                            for i in lista_consultas:
                                if i["id"] == id_consulta:
                                    data = input("Digite a nova data:")
                                    hora= input("Digite o horário da nova consulta: ")
                    
                                    for a in lista_consultas:
                                        if a["id"] == i["id"] and a["data"] == data and a["hora"] == hora:
                                            print("já tem cosulta nesse horário!")
                                            encontrado = True

                                    if not encontrado:
                                        i["data"] = data
                                        i["hora"] = hora

                                    s.Salvar_arquivo_consultas(lista_consultas)

                                    print("Consulta reagendada com sucesso!")

                        elif op == 3:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            id_consulta = int(input("Digite o id da consulta que deseja cancelar: "))

                            for i in lista_consultas:
                                if id_consulta == i["id"]:
                                    i["status"] = "Cancelada"

                            s.Salvar_arquivo_consultas(lista_consultas)

                            print("Consulta cancelada com sucesso!")

                        elif op == 4:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            id_consulta = int(input("Digite o id da consulta que deseja confirmar: "))

                            encontrado = False

                            for i in lista_consultas:
                                if id_consulta == i["id"] and i["status"] == "Agendada":
                                    print(f"ID médico: {i["id_medico"]}")
                                    print(f"ID paciente: {i["id_paciente"]}")
                                    print(f"Data: {i["data"]}")
                                    print(f"Hora: {i["hora"]}")
                                    print(f"Status: {i["status"]}")

                                    i["status"] = "Confirmada"
                                    
                                    print("Consultada confirmada!")

                                    encontrado = True
                            s.Salvar_arquivo_consultas(lista_consultas)

                            if not encontrado:
                                print("Essa consulta não pode ser confirmada!")

                        elif op == 5:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            data_hoje = datetime.now().date()

                            encontrado = False

                            for i in lista_consultas:
                                data_consulta = datetime.strptime(i["data"], "%d/%m/%Y").date()

                                if data_consulta == data_hoje:
                                
                                    if i["status"] == "Agendada" or i["status"] == "Confirmada" or i["status"] == "Em atendimento" or i["status"] == "Finalizada":
                                        print(f"ID consulta: {i["id"]}")
                                        print(f"ID médico: {i["id_medico"]}")
                                        print(f"ID paciente: {i["id_paciente"]}")
                                        print(f"Data: {i["data"]}")
                                        print(f"Hora: {i["hora"]}")
                                        print(f"Status: {i["status"]}")
                                        print("---------------------------------------------")

                                        encontrado = True

                            if not encontrado:
                                print("Sem consultas hoje!")

                        elif op == 6:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            data_hoje = datetime.now().date()

                            encontrado = False

                            for i in lista_consultas:
                                data_consulta = datetime.strptime(i["data"], "%d/%m/%Y").date()

                                if data_consulta != data_hoje and data_consulta > data_hoje:
                                
                                    if i["status"] == "Agendada" or i["status"] == "Confirmada":
                                        print(f"ID consulta: {i["id"]}")
                                        print(f"ID médico: {i["id_medico"]}")
                                        print(f"ID paciente: {i["id_paciente"]}")
                                        print(f"Data: {i["data"]}")
                                        print(f"Hora: {i["hora"]}")
                                        print(f"Status: {i["status"]}")
                                        print("---------------------------------------------")

                                        encontrado = True

                            if not encontrado:
                                print("Sem consultas futuras!")

                        elif op == 7:
                            print("Voltando!")
                            break

                elif op == 3:
                    while True:
                        print("-----MENU RECEPÇÃO HISTÓRICO-----")
                        print("1 - Visualizar consultas anteriores do paciente")
                        print("2 - Ver datas de atendimentos anteriores")
                        print("3 - Sair")

                        op = int(input("Digite a opção que deseja acessar: "))

                        if op == 1:
                            lista_consultas = s.Carregar_arquivo_consultas()
                            lista_pacientes = s.Carregar_arquivo_pacientes()

                            for i in lista_pacientes:
                                print(f"ID paciente: {i["id"]} | Nome: {i["nome"]}")

                            id_paciente = int(input("Digite o id do paciente que deseja acessar: "))

                            data_hoje = datetime.now().date()

                            encontrado = False

                            for i in lista_consultas:
                                data_consulta = datetime.strptime(i["data"], "%d/%m/%Y").date()

                                if data_consulta != data_hoje and data_consulta < data_hoje:

                                    if i["id_paciente"] == id_paciente:
                                        print(f"Data: {i["data"]} | Hora: {i["hora"]}")
                                        print(f"ID médico: {i["id_medico"]} | Status: {i["status"]}")
                                        print("--------------------------------------------------------")
                                        encontrado = True

                            if not encontrado:
                                print("Paciente não possue consultas anteriores!")

                        elif op == 2:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            data_hoje = datetime.now().date()

                            encontrado = False

                            for i in lista_consultas:
                                data_consulta = datetime.strptime(i["data"], "%d/%m/%Y").date()

                                if data_consulta != data_hoje and data_consulta < data_hoje:
                                    print(f"ID consulta: {i["id"]} - Data: {i["data"]} - Hora: {i["hora"]} - Status: {i["status"]}")
                                    encontrado = True

                            if not encontrado:
                                print("Sem consultas anteriores!")

                        elif op == 3:
                            print("Voltando!")
                            break

                elif op == 4:
                    while True:
                        print("-----MENU RECEPÇÃO RELATÒRIOS-----")
                        print("1 - Agenda do dia")
                        print("2 - Consultas por data")
                        print("3 - Consultas canceladas por período")
                        print("4 - Pacientes atendidos por dia")
                        print("5 - Sair")

                        op = int(input("Digite a opção que deseja acessar: "))

                        if op == 1:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            data_hoje = datetime.now().date()

                            encontrado = False
                            
                            print(f"Data: {data_hoje}")

                            for i in lista_consultas:
                                data_consulta = datetime.strptime(i["data"], "%d/%m/%Y").date()

                                if data_consulta == data_hoje:
                                    print(f"ID consulta: {i["id"]} - Hora: {i["hora"]} - Status: {i["status"]}")
                                    encontrado = True

                            if not encontrado:
                                print("Sem consultas hoje!")

                        elif op == 2:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            data = input("Digite a data que deseja buscar: ")

                            consultas_data = 0

                            for i in lista_consultas:
                                if i["data"] == data:
                                    consultas_data += 1

                            print(f"Total de consultas nessa data: {consultas_data}")

                        elif op == 3:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            data_inicio = datetime.strptime(input("Data início (dd/mm/aaaa): "), "%d/%m/%Y")
                            data_fim = datetime.strptime(input("Data fim (dd/mm/aaaa): "), "%d/%m/%Y")

                            total = 0

                            for i in lista_consultas:
                                if i["status"] == "Cancelada":
                                    data_consulta = datetime.strptime(i["data"], "%d/%m/%Y")

                                    if data_inicio <= data_consulta <= data_fim:
                                        total += 1

                            print(f"Total de consultas canceladas: {total}")

                        elif op == 4:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            contagem = {}

                            for i in lista_consultas:
                                data = i["data"]
                                
                                if data in contagem:
                                    contagem[data] += 1
                                else:
                                    contagem[data] = 1

                            for data in sorted(contagem):
                                print(f"{data}: {contagem[data]} atendimentos")

                        elif op == 5:
                            print("Voltando!")
                            break
                
                elif op == 5:
                    print("Voltando!")
                    break

    elif opcao == 3:
        if func.Validar_login_medico():
            func.mostrar_consultas_hoje()
            
            while True:
                print("-----MENU MÉDICO-----")
                print("1 - Agenda")
                print("2 - Atendimento")
                print("3 - Prontuário / Laudo")
                print("4 - Histórico Médico")
                print("5 - Relatórios")
                print("6 - Sair")

                op = int(input("Digite a opção que deseja acessar: "))

                if op == 1:
                    while True:
                        print("-----MENU AGENDA MÉDICO-----")
                        print("1 - Listar consultar marcadas")
                        print("2 - Agenda do dia")
                        print("3 - Agenda futura")
                        print("4 - Voltar")

                        op = int(input("Digite a opção que deseja acessar: "))

                        if op == 1:
                            lista_consultas = s.Carregar_arquivo_consultas()

                            id_medico = func.obter_id_medico_logado()

                            encontrado = False

                            for i in lista_consultas:
                                if id_medico == i["id_medico"]:
                                    if i["status"] == "Agendada" or i["status"] == "Confirmada":
                                        print(f"ID consulta: {i["id"]}")
                                        print(f"Data: {i["data"]}")
                                        print(f"Hora: {i["hora"]}")
                                        print(f"Status: {i["status"]}")
                                        print(f"ID paciente: {i["id_paciente"]}")
                                        encontrado = True
                            
                            if not encontrado:
                                print("Sem consultas localizadas!")
                                break
                        
                        elif op == 2:
                            lista_consultas = s.Carregar_arquivo_consultas()
                            id_medico = func.obter_id_medico_logado()
                            data_hoje = datetime.now().date()

                            encontrado = False

                            for i in lista_consultas:
                                data_consulta = datetime.strptime(i["data"], "%d/%m/%Y").date()

                                if i["id_medico"] == id_medico and data_consulta == data_hoje:
                                    print(f"ID consulta: {i["id"]}")
                                    print(f"Data: {i['data']}")
                                    print(f"Hora: {i['hora']}")
                                    print(f"Status: {i['status']}")
                                    print(f"ID paciente: {i['id_paciente']}")
                                    print("----------------------------------")
                                    encontrado = True

                            if not encontrado:
                                print("Você não possui consultas hoje!")
                        
                        elif op == 3:
                            lista_consultas = s.Carregar_arquivo_consultas()
                            id_medico = func.obter_id_medico_logado()
                            data_hoje = datetime.now().date()

                            encontrado = False

                            for i in lista_consultas:
                                data_consulta = datetime.strptime(i["data"], "%d/%m/%Y").date()

                                if i["id_medico"] == id_medico and data_consulta != data_hoje:
                                    if i["status"] == "Agendada" or i["status"] == "Confirmada":
                                        print(f"ID consulta: {i["id"]}")
                                        print(f"Data: {i['data']}")
                                        print(f"Hora: {i['hora']}")
                                        print(f"Status: {i['status']}")
                                        print(f"ID paciente: {i['id_paciente']}")
                                        print("----------------------------------")
                                        encontrado = True

                            if not encontrado:
                                print("Você não possui consultas hoje!")

                        elif op == 4:
                            print("Voltando!")
                        break


                elif op == 2:
                    while True:
                        print("-----MENU ATENDIMENTO MÉDICO-----")
                        print("1 - Iniciar atendimento")
                        print("2 - Finalizar atendimento")
                        print("3 - Voltar")

                        op = int(input("Digite a opção que deseja acessar: "))

                        if op == 1:
                            lista_consultas = s.Carregar_arquivo_consultas()
                            
                            id_consulta_confirmar = int(input("Digite o ID da consulta: "))

                            encontrado = False

                            for i in lista_consultas:
                                if i["id"] == id_consulta_confirmar:
                                    i["status"] = "Em Atendimento"
                                    encontrado = True

                            if not encontrado:
                                print("Consulta não encontrada!")
                                break

                            s.Salvar_arquivo_consultas(lista_consultas)
                            print("Status da consulta alterado com sucesso!")
                        
                        elif op == 2:
                            lista_consultas = s.Carregar_arquivo_consultas()
                            
                            id_consulta_finalizar = int(input("Digite o ID da consulta: "))

                            encontrado = False

                            for i in lista_consultas:
                                if i["id"] == id_consulta_finalizar:
                                    if i["status"] == "Em Atendimento":
                                        i["status"] = "Finalizada"
                                        encontrado = True

                            if not encontrado:
                                print("Consulta não encontrada!")
                                break

                            s.Salvar_arquivo_consultas(lista_consultas)
                            print("Consulta finalizada com sucesso!")
                        
                        elif op == 3:
                            print("Voltando!")
                            break

                elif op == 3:
                        

    else:
        print("Informação não permitida para esse usuários")
        
