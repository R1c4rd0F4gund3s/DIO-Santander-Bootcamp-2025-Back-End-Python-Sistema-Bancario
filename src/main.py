import textwrap
import os
from gerenciador_senhas import GerenciadorDeSenhas
import persistencia
import servicos
import utils
import config
from modelos import ContaCorrente, ContaInvestimento, ContaPoupanca, ContasIterador
from excecoes import SaldoInsuficienteError, LimiteDeSaquesError, LimiteDeValorError, RegraDeNegocioError

def menu():
    menu_str = """

    ================ MENU PRINCIPAL ================ 
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [t]\tTransferir
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [lu]\tListar Usuários
    [cf]\tConfigurações
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_str))

def menu_configuracoes(salvar_ao_sair_status):
    status = "Ativado" if salvar_ao_sair_status else "Desativado"
    menu_str = f"""

    ================ CONFIGURAÇÕES ================ 
    [1]\tSalvar dados ao sair: [{status}]
    [v]\tVoltar ao menu principal
    => """
    return input(textwrap.dedent(menu_str))

def gerenciar_configuracoes(salvar_ao_sair):
    while True:
        opcao = menu_configuracoes(salvar_ao_sair[0])
        if opcao == "1":
            salvar_ao_sair[0] = not salvar_ao_sair[0]
            status = "ativado" if salvar_ao_sair[0] else "desativado"
            print(f"\n=== Salvamento automático ao sair foi {status}. ===")
        elif opcao == "v":
            break
        else:
            print("\n@@@ Opção inválida! @@@")

def ui_obter_cliente(clientes):
    cpf = utils._obter_cpf_valido()
    cliente = servicos.filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return None
    return cliente

def ui_selecionar_conta(cliente, contas_disponiveis=None):
    contas_a_mostrar = contas_disponiveis if contas_disponiveis is not None else cliente.contas

    if not contas_a_mostrar:
        print("\n@@@ Cliente não possui contas para esta operação. @@@")
        return None

    if len(contas_a_mostrar) == 1:
        return contas_a_mostrar[0]

    while True:
        print("\n--- Selecione uma Conta ---")
        for i, conta in enumerate(contas_a_mostrar):
            print(f"[{i + 1}] {conta}")
        
        try:
            escolha_str = input(f"Digite o número da conta (1-{len(contas_a_mostrar)}): ")
            escolha_int = int(escolha_str)
            
            if 1 <= escolha_int <= len(contas_a_mostrar):
                return contas_a_mostrar[escolha_int - 1]
            else:
                print(f"\n@@@ Opção inválida! Escolha um número entre 1 e {len(contas_a_mostrar)}. @@@")
        except ValueError:
            print("\n@@@ Entrada inválida! Por favor, digite apenas o número da conta. @@@")

def ui_depositar(clientes):
    cliente = ui_obter_cliente(clientes)
    if not cliente:
        return

    contas_elegiveis = [c for c in cliente.contas if not isinstance(c, ContaInvestimento)]
    if not contas_elegiveis:
        print("\n@@@ Cliente não possui contas que aceitam depósito. @@@")
        return

    print("\nSelecione a conta para o depósito:")
    conta = ui_selecionar_conta(cliente, contas_disponiveis=contas_elegiveis)
    if not conta:
        return

    valor = utils._obter_valor_monetario("Informe o valor do depósito: ")
    if valor is None:
        return

    try:
        servicos.realizar_deposito(conta, valor)
        print("\n=== Depósito realizado com sucesso! ===")
    except (ValueError, RegraDeNegocioError) as e:
        print(f"\n@@@ {e} @@@")

def ui_sacar(clientes):
    cliente = ui_obter_cliente(clientes)
    if not cliente:
        return

    print("\nDe qual conta deseja sacar?")
    conta = ui_selecionar_conta(cliente)
    if not conta:
        return

    valor = utils._obter_valor_monetario("Informe o valor do saque: ")
    if valor is None:
        return

    try:
        servicos.realizar_saque(conta, valor)
        print("\n=== Saque realizado com sucesso! ===")
    except (ValueError, SaldoInsuficienteError, LimiteDeSaquesError, LimiteDeValorError) as e:
        print(f"\n@@@ {e} @@@")

def ui_exibir_extrato(clientes):
    cliente = ui_obter_cliente(clientes)
    if not cliente:
        return

    print("\nDe qual conta deseja exibir o extrato?")
    conta = ui_selecionar_conta(cliente)
    if not conta:
        return

    print("\n================ EXTRATO =============...")
    
    filtro = input("Deseja filtrar por tipo de transação? (s/d/t para saque/depósito/transferência ou deixe em branco para todas): ").lower()
    tipo_filtro = None
    if filtro == 's':
        tipo_filtro = 'saque'
    elif filtro == 'd':
        tipo_filtro = 'deposito'
    elif filtro == 't':
        tipo_filtro = 'transferencia'

    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio(tipo_transacao=tipo_filtro):
        tem_transacao = True
        tipo_transacao_str = transacao['tipo'] + ":"
        valor_transacao = f"R$ {transacao['valor']:.2f}"
        extrato += f"\n{tipo_transacao_str:<25} {valor_transacao:>15}\t{transacao['data']}"

    if not tem_transacao:
        extrato = "\nNão foram realizadas movimentações" 
        if tipo_filtro:
            extrato += f" do tipo '{tipo_filtro}'."
        else:
            extrato += "."

    print(extrato)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("========================================")

def ui_transferir(clientes):
    cliente = ui_obter_cliente(clientes)
    if not cliente:
        return

    print("\n--- Conta de Origem ---")
    conta_origem = ui_selecionar_conta(cliente)
    if not conta_origem:
        return

    print("\n--- Conta de Destino ---")
    conta_destino = ui_selecionar_conta(cliente)
    if not conta_destino:
        return

    if conta_origem == conta_destino:
        print("\n@@@ Conta de origem e destino não podem ser as mesmas! @@@")
        return

    valor = utils._obter_valor_monetario("Informe o valor da transferência: ")
    if valor is None:
        return

    try:
        servicos.realizar_transferencia(cliente, conta_origem, conta_destino, valor)
        print("\n=== Transferência realizada com sucesso! ===")
    except (ValueError, SaldoInsuficienteError, RegraDeNegocioError) as e:
        print(f"\n@@@ {e} @@@")

def ui_criar_cliente(clientes, gerenciador_senhas):
    cpf = utils._obter_cpf_valido()
    if servicos.filtrar_cliente(cpf, clientes):
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    dados_cliente = {
        "nome": utils._obter_nome_completo(),
        "data_nascimento": utils._obter_data_nascimento_valida(),
        "cpf": cpf,
        "endereco": utils._obter_endereco_completo(),
        "telefone": utils.validar_telefone("Informe o telefone"),
        "celular": utils.validar_telefone("Informe o celular")
    }
    
    cliente_criado = servicos.criar_novo_cliente(clientes, **dados_cliente)
    gerenciador_senhas.definir_senha_inicial(cliente_criado)
    print("\n=== Cliente criado com sucesso! ===")

def ui_criar_conta(clientes, contas):
    cliente = ui_obter_cliente(clientes)
    if not cliente:
        return

    while True:
        print("\n--- Selecione o Tipo de Conta ---")
        print("[1] Conta Corrente")
        print("[2] Conta Poupança")
        print("[3] Conta Investimento")
        print("[v] Voltar")
        opcao = input("=> ").lower()

        if opcao == "v":
            break

        try:
            if opcao == "1":
                servicos.criar_nova_conta(cliente, contas, "corrente")
                print("\n=== Conta Corrente criada com sucesso! ===")
                break
            elif opcao == "2":
                if any(isinstance(c, ContaPoupanca) for c in cliente.contas):
                    raise RegraDeNegocioError("Cliente já possui uma Conta Poupança. Não é possível criar outra.")
                servicos.criar_nova_conta(cliente, contas, "poupanca")
                print("\n=== Conta Poupança criada com sucesso! ===")
                break
            elif opcao == "3":
                if not any(isinstance(c, ContaCorrente) for c in cliente.contas):
                    raise RegraDeNegocioError("É necessário ter uma Conta Corrente para criar uma Conta Investimento.")
                
                print("\n--- Selecione o Tipo de Ativo ---")
                for i, ativo in enumerate(config.TIPOS_DE_ATIVOS):
                    print(f"[{i + 1}] {ativo}")
                
                escolha = int(input(f"Digite o número do ativo (1-{len(config.TIPOS_DE_ATIVOS)}): "))
                ativo_selecionado = config.TIPOS_DE_ATIVOS[escolha - 1]

                servicos.criar_nova_conta(cliente, contas, "investimento", ativo=ativo_selecionado)
                print(f"\n=== Conta Investimento ({ativo_selecionado}) criada com sucesso! ===")
                break
            else:
                print("\n@@@ Opção inválida! @@@")
        except (ValueError, IndexError):
            print("\n@@@ Opção de ativo inválida! @@@")
        except RegraDeNegocioError as e:
            print(f"\n@@@ {e} @@@")

def ui_listar_contas(contas):
    if not contas:
        print("\n@@@ Não há contas cadastradas. @@@")
        return

    for conta in ContasIterador(contas):
        print("=" * 100)
        info_conta = f"""
        Agência:\t\t{conta.agencia}
        Número:\t\t{conta.numero}
        Titular:\t\t{conta.cliente.nome}
        Saldo:\t\tR$ {conta.saldo:.2f}
        """
        print(textwrap.dedent(info_conta))

def ui_listar_clientes(clientes):
    if not clientes:
        print("\n@@@ Não há clientes cadastrados. @@@")
        return

    print("\n================ LISTA DE CLIENTES ================")
    for cliente in clientes:
        print(textwrap.dedent(f"""
            Nome:\t\t{cliente.nome}
            CPF:\t\t{utils.formatar_cpf(cliente.cpf)}
            Endereço:\t{cliente.endereco}
            Telefone:\t{cliente.telefone}
            Celular:\t{cliente.celular}
        """))
        print("=" * 50)

def main():
    clientes, contas = persistencia.carregar_dados()
    salvar_ao_sair = [False]

    if clientes:
        print("\n--- Sessão Anterior Encontrada ---")
        while True:
            escolha = input("Deseja [c]arregar os dados ou iniciar uma [n]ova sessão? ").lower()
            if escolha == 'c':
                print("Dados carregados.")
                break
            elif escolha == 'n':
                clientes, contas = [], []
                break
            else:
                print("Opção inválida.")

    gerenciador_senhas = GerenciadorDeSenhas()

    while True:
        opcao = menu()

        if opcao == "d":
            ui_depositar(clientes)
        elif opcao == "s":
            ui_sacar(clientes)
        elif opcao == "e":
            ui_exibir_extrato(clientes)
        elif opcao == "t":
            ui_transferir(clientes)
        elif opcao == "nu":
            ui_criar_cliente(clientes, gerenciador_senhas)
        elif opcao == "nc":
            ui_criar_conta(clientes, contas)
        elif opcao == "lc":
            ui_listar_contas(contas)
        elif opcao == "lu":
            ui_listar_clientes(clientes)
        elif opcao == "cf":
            gerenciar_configuracoes(salvar_ao_sair)
        elif opcao == "q":
            if salvar_ao_sair[0]:
                persistencia.salvar_dados(clientes, contas)
            elif os.path.exists(config.DATA_FILE):
                os.remove(config.DATA_FILE)
            print("\nSaindo do sistema...")
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

if __name__ == "__main__":
    main()