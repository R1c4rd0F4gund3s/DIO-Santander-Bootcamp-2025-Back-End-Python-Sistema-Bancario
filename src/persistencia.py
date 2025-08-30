import os
import pickle
import config

def carregar_dados():
    if os.path.exists(config.DATA_FILE):
        try:
            with open(config.DATA_FILE, "rb") as f:
                dados = pickle.load(f)
                if isinstance(dados, (list, tuple)) and len(dados) == 2 and isinstance(dados[0], list) and isinstance(dados[1], list):
                    return dados[0], dados[1]
        except (pickle.UnpicklingError, EOFError, TypeError) as e:
            print(f"\n@@@ Erro ao carregar dados: o arquivo pode estar corrompido. Começando uma nova sessão. ({e}) @@@")
            os.remove(config.DATA_FILE)
    return [], []

def salvar_dados(clientes, contas):
    try:
        with open(config.DATA_FILE, "wb") as f:
            pickle.dump((clientes, contas), f)
        print("\n=== Dados salvos com sucesso! ===")
    except Exception as e:
        print(f"\n@@@ Erro ao salvar dados: {e} @@@")