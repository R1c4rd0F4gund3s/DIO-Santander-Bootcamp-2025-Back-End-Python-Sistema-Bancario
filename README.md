# Sistema Bancário em Python (POO)

![Python](https://img.shields.io/badge/python-3.11-blue.svg)

Este projeto é uma simulação de um sistema bancário desenvolvido em Python, utilizando os princípios da Programação Orientada a Objetos (POO). O sistema é executado via linha de comando (CLI) e foi estruturado de forma modular para facilitar a manutenção, testabilidade e futuras expansões.

## Funcionalidades

-   **Gerenciamento de Clientes e Contas**: Crie múltiplos clientes e associe a eles diferentes tipos de contas.
-   **Tipos de Contas**: Suporte para Conta Corrente, Conta Poupança e Conta Investimento, cada uma com suas próprias regras de negócio.
-   **Operações Bancárias**: Realize depósitos, saques e transferências entre contas.
-   **Histórico de Transações**: Todas as operações são registradas e podem ser consultadas no extrato da conta.
-   **Persistência de Dados**: O estado da aplicação (clientes e contas) pode ser salvo ao sair e recarregado ao iniciar, permitindo a continuidade entre sessões.
-   **Configuração de Sessão**: O usuário pode escolher se deseja ou não salvar os dados ao final de cada sessão.

## Arquitetura do Projeto

O código foi refatorado para uma arquitetura modular, separando as responsabilidades em diferentes arquivos para garantir um baixo acoplamento e alta coesão.

-   `main.py`: Ponto de entrada da aplicação. Responsável pela interface com o usuário (menus, inputs, prints) e pela orquestração das chamadas aos outros módulos.
-   `modelos.py`: Contém as classes que representam os dados do sistema (Cliente, Conta, Transacao, etc.).
-   `servicos.py`: Contém a lógica de negócio pura, como as regras para realizar uma transferência ou um saque.
-   `excecoes.py`: Define as exceções customizadas para um tratamento de erros mais claro e robusto.
-   `persistencia.py`: Encapsula a lógica de salvar e carregar os dados da aplicação em um arquivo.
-   `utils.py`: Funções auxiliares para validação e formatação de entradas do usuário.
-   `config.py`: Arquivo central para constantes e configurações da aplicação, como limites de saque, quantidade de transações e tipos de ativos de investimento.

## Como Executar

1.  Certifique-se de ter o Python 3 instalado.
2.  Clone este repositório.
3.  Navegue até o diretório `banco_modular/` pelo seu terminal.
4.  Execute o seguinte comando:

    ```bash
    python main.py
    ```

5.  Siga as instruções apresentadas no menu interativo.

## Documentação do Projeto

Para uma compreensão mais aprofundada da arquitetura e do funcionamento do sistema, consulte os seguintes documentos:

-   **[📄 Manual de Utilização](MANUAL.md)**: Um guia para o usuário final sobre como operar o sistema.
-   **[📐 Diagrama de Classes (UML)](diagrama_uml.md)**: Uma representação visual das classes e seus relacionamentos.
-   **[🌊 Fluxograma do Sistema](fluxograma.md)**: Um diagrama que ilustra o fluxo principal de execução da aplicação.