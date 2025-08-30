from abc import ABC, abstractmethod
from datetime import datetime
import config
from excecoes import SaldoInsuficienteError, LimiteDeSaquesError, LimiteDeValorError, RegraDeNegocioError

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            self._index += 1
            return conta
        except IndexError:
            raise StopIteration


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= config.LIMITE_TRANSACOES_DIARIAS:
            raise RegraDeNegocioError(f"Você excedeu o número de {config.LIMITE_TRANSACOES_DIARIAS} transações permitidas para hoje!")

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco, telefone, celular):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.telefone = telefone
        self.celular = celular
        self._senha = None


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero, **kwargs):
        return cls(numero, cliente, **kwargs)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")

        if valor > self.saldo:
            raise SaldoInsuficienteError("Operação falhou! Você não tem saldo suficiente.")

        self._saldo -= valor

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        
        self._saldo += valor


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=config.LIMITE_VALOR_SAQUE, limite_saques=config.LIMITE_SAQUES):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self.contas_vinculadas = []

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self._limite:
            raise LimiteDeValorError(f"Operação falhou! O valor do saque (R$ {valor:.2f}) excede o limite de R$ {self._limite:.2f}.")

        if numero_saques >= self._limite_saques:
            raise LimiteDeSaquesError(f"Operação falhou! Número máximo de saques ({self._limite_saques}) excedido.")

        super().sacar(valor)

    def __str__(self):
        return f"Conta Corrente | Agência: {self.agencia} | C/C: {self.numero}"


class ContaPoupanca(Conta):
    def __str__(self):
        return f"Conta Poupança | Agência: {self.agencia} | C/P: {self.numero}"


class ContaInvestimento(Conta):
    def __init__(self, numero, cliente, ativo):
        super().__init__(numero, cliente)
        self.ativo = ativo

    def depositar(self, valor):
        raise RegraDeNegocioError("Contas de investimento não aceitam depósito direto. Use a transferência de fundos.")

    def receber_transferencia(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            raise ValueError("O valor da transferência deve ser positivo.")

    def __str__(self):
        return f"Conta Investimento ({self.ativo}) | Agência: {self.agencia} | C/I: {self.numero}"


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao, tipo_override=None):
        self._transacoes.append(
            {
                "tipo": tipo_override or transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        transacoes_hoje = []
        data_hoje = datetime.utcnow().date()
        for transacao in self.transacoes:
            data_transacao = datetime.strptime(transacao['data'], '%d-%m-%Y %H:%M:%S').date()
            if data_hoje == data_transacao:
                transacoes_hoje.append(transacao)
        return transacoes_hoje


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.sacar(self.valor)
        conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.depositar(self.valor)
        conta.historico.adicionar_transacao(self)


class Transferencia(Transacao):
    def __init__(self, valor, conta_destino):
        self._valor = valor
        self.conta_destino = conta_destino

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta_origem):
        conta_origem.sacar(self.valor)
        if isinstance(self.conta_destino, ContaInvestimento):
            self.conta_destino.receber_transferencia(self.valor)
        else:
            self.conta_destino.depositar(self.valor)
        
        conta_origem.historico.adicionar_transacao(self, tipo_override=f"Transf. para C/{self.conta_destino.numero}")
        self.conta_destino.historico.adicionar_transacao(self, tipo_override=f"Transf. de C/{conta_origem.numero}")
