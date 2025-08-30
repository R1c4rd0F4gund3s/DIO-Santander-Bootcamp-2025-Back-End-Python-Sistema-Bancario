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

O projeto foi organizado nas seguintes pastas:

-   **/src**: Contém todo o código-fonte da aplicação.
    -   `main.py`: Ponto de entrada da aplicação (UI).
    -   `modelos.py`: Classes de dados (Cliente, Conta, etc.).
    -   `servicos.py`: Lógica de negócio.
    -   `decorators.py`: Decoradores customizados.
    -   `excecoes.py`: Exceções customizadas.
    -   `persistencia.py`: Lógica de persistência de dados.
    -   `utils.py`: Funções utilitárias.
    -   `config.py`: Constantes e configurações.
-   **/doc**: Armazena a documentação do projeto.
-   **/images**: Para armazenar imagens (se aplicável).
-   **/scripts**: Para scripts auxiliares (se aplicável).

## Como Executar

1.  Certifique-se de ter o Python 3 instalado.
2.  Clone este repositório.
3.  Navegue até o diretório `banco_modular/` pelo seu terminal.
4.  Execute o seguinte comando:

    ```bash
    python src/main.py
    ```

5.  Siga as instruções apresentadas no menu interativo.

## Documentação do Projeto

Para uma compreensão mais aprofundada da arquitetura e do funcionamento do sistema, consulte os seguintes documentos na pasta `/doc`:

-   **[📄 Manual de Utilização](doc/MANUAL.md)**: Um guia para o usuário final sobre como operar o sistema.
-   **[📐 Diagrama de Classes (UML)](doc/diagrama_uml.md)**: Uma representação visual das classes e seus relacionamentos.
-   **[🌊 Fluxograma do Sistema](doc/fluxograma.md)**: Um diagrama que ilustra o fluxo principal de execução da aplicação.

## Contato

#### Ricardo Fagundes
[e-mail](fagundz@gmail.com)
[Linkedin](https://www.linkedin.com/in/ricardofagundes)
