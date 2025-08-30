"""Módulo para exceções customizadas da aplicação."""

class SaldoInsuficienteError(Exception):
    """Exceção levantada quando não há saldo suficiente para uma operação."""
    pass

class LimiteDeSaquesError(Exception):
    """Exceção levantada quando o limite de saques diários é atingido."""
    pass

class LimiteDeValorError(Exception):
    """Exceção levantada quando o valor de um saque excede o limite da conta."""
    pass

class RegraDeNegocioError(Exception):
    """Exceção genérica para violações de regras de negócio."""
    pass
