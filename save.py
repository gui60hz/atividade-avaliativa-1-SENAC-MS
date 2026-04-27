import json
from pathlib import Path

base = Path(__file__).parent

def Carregar_arquivo_usuarios():
    with open(base / "arquivos json/usuarios.json", "r", encoding="utf-8") as f:
        conteudo = json.load(f)
        return conteudo
    
def Carregar_arquivo_consultas():
    with open(base / "arquivos json/consultas.json", "r", encoding="utf-8") as f:
        conteudo = json.load(f)
        return conteudo
    
def Carregar_arquivo_medicos():
    with open(base / "arquivos json/medicos.json", "r", encoding="utf-8") as f:
        conteudo = json.load(f)
        return conteudo
    
def Carregar_arquivo_pacientes():
    with open(base / "arquivos json/pacientes.json", "r", encoding="utf-8") as f:
        conteudo = json.load(f)
        return conteudo
    
def Carregar_arquivo_prontuarios():
    with open(base / "arquivos json/prontuarios.json", "r", encoding="utf-8") as f:
        conteudo = json.load(f)
        return conteudo

def Salvar_arquivo_usuarios(dados):
    with open(base / "arquivos json/usuarios.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)

def Salvar_arquivo_consultas(dados):
    with open(base / "arquivos json/consultas.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)

def Salvar_arquivo_medicos(dados):
    with open(base / "arquivos json/medicos.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)

def Salvar_arquivo_pacientes(dados):
    with open(base / "arquivos json/pacientes.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)

def Salvar_arquivo_prontuarios(dados):
    with open(base / "arquivos json/prontuarios.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)