from datetime import datetime

def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def validar_telefone(label):
    while True:
        numero = input(f"{label} (somente números com DDD): ")
        if numero.isdigit() and 10 <= len(numero) <= 11:
            return numero
        else:
            print("@@@ Número de telefone/celular inválido! Por favor, informe apenas os 10 ou 11 dígitos numéricos, incluindo o DDD. @@@")

def _obter_valor_monetario(mensagem_prompt):
    while True:
        try:
            valor = float(input(mensagem_prompt))
            if valor > 0:
                return valor
            else:
                print("@@@ Operação falhou! O valor deve ser positivo. @@@")
        except ValueError:
            print("@@@ Operação falhou! O valor informado é inválido. @@@")

def _obter_nome_completo():
    return input("Informe o nome completo: ")

def _obter_data_nascimento_valida():
    while True:
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        try:
            datetime.strptime(data_nascimento, "%d-%m-%Y")
            return data_nascimento
        except ValueError:
            print("@@@ Data inválida! Por favor, use o formato dd-mm-aaaa e uma data real. @@@")

def _obter_endereco_completo():
    return input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

def _obter_cpf_valido():
    while True:
        cpf = input("Informe o CPF (somente número): ")
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        else:
            print("@@@ CPF inválido! Por favor, informe apenas os 11 dígitos do CPF. @@@")
