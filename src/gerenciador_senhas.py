class GerenciadorDeSenhas:
    """Classe simulada para gerenciamento de senhas."""

    def definir_senha_inicial(self, cliente):
        print(f"\n[SIMULAÇÃO] Senha inicial definida para {cliente.nome}.")
        # Em um cenário real, isso solicitaria e armazenaria uma senha com hash.
        cliente._senha = "senha_padrao_simulada"
        return True

    def validar_senha(self, cliente):
        print(f"\n[SIMULAÇÃO] Validando senha para {cliente.nome}.")
        # Em um cenário real, isso solicitaria uma senha e compararia os hashes.
        return True

    def gerenciar_alteracao_senha(self, cliente):
        print(f"\n[SIMULAÇÃO] Gerenciando alteração de senha para {cliente.nome}.")
        # Em um cenário real, haveria um fluxo completo de validação e atualização.
        cliente._senha = "nova_senha_simulada"
        print("Senha alterada com sucesso.")
        return True

