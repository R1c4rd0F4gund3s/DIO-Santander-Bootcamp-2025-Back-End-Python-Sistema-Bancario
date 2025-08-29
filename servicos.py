from modelos import Deposito, Saque, Transferencia, PessoaFisica, ContaCorrente, ContaPoupanca, ContaInvestimento, Conta
from excecoes import RegraDeNegocioError

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def _encontrar_cc_pai(cliente, conta_vinculada):
    """Encontra a Conta Corrente à qual uma conta está vinculada."""
    for conta in cliente.contas:
        if isinstance(conta, ContaCorrente) and conta_vinculada in conta.contas_vinculadas:
            return conta
    return None

def realizar_deposito(conta, valor):
    deposito = Deposito(valor)
    conta.cliente.realizar_transacao(conta, deposito)

def realizar_saque(conta, valor):
    saque = Saque(valor)
    conta.cliente.realizar_transacao(conta, saque)

def realizar_transferencia(cliente, conta_origem, conta_destino, valor):
    if isinstance(conta_destino, ContaInvestimento):
        cc_pai = _encontrar_cc_pai(cliente, conta_destino)
        origem_eh_cc_pai = (conta_origem == cc_pai)
        origem_eh_poupanca_vinculada = (
            isinstance(conta_origem, ContaPoupanca) and 
            cc_pai and 
            conta_origem in cc_pai.contas_vinculadas
        )
        if not (origem_eh_cc_pai or origem_eh_poupanca_vinculada):
            raise RegraDeNegocioError("Transferências para Contas de Investimento devem partir da Conta Corrente principal ou de uma Poupança vinculada a ela.")

    transferencia = Transferencia(valor, conta_destino)
    cliente.realizar_transacao(conta_origem, transferencia)

def criar_novo_cliente(clientes, **kwargs):
    novo_cliente = PessoaFisica(**kwargs)
    clientes.append(novo_cliente)
    return novo_cliente

def criar_nova_conta(cliente, contas, tipo_conta, **kwargs):
    numero_conta = len(contas) + 1
    if tipo_conta == "corrente":
        nova_conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    elif tipo_conta == "poupanca":
        nova_conta = ContaPoupanca.nova_conta(cliente=cliente, numero=numero_conta)
    elif tipo_conta == "investimento":
        nova_conta = ContaInvestimento.nova_conta(cliente=cliente, numero=numero_conta, ativo=kwargs.get("ativo"))
    else:
        return None
    
    cliente.adicionar_conta(nova_conta)
    contas.append(nova_conta)
    return nova_conta