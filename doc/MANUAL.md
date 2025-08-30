# Manual de Utilização - Sistema Bancário

Este manual descreve como utilizar o Sistema Bancário via linha de comando.

## 1. Iniciando a Aplicação

Para iniciar o sistema, navegue até o diretório `banco_modular` e execute o seguinte comando:

```bash
python src/main.py
```

### Carregando Dados Anteriores

Ao iniciar, se houver dados de uma sessão anterior, o sistema perguntará:

`Deseja [c]arregar os dados ou iniciar uma [n]ova sessão?`

-   Digite `c` para continuar de onde parou.
-   Digite `n` para começar uma sessão nova e limpa (os dados antigos serão apagados).

## 2. Menu Principal

Após a inicialização, o menu principal será exibido com as seguintes opções:

-   `[d] Depositar`: Inicia o fluxo para depositar um valor em uma conta.
-   `[s] Sacar`: Inicia o fluxo para sacar um valor de uma conta.
-   `[e] Extrato`: Exibe o extrato de transações de uma conta específica.
-   `[t] Transferir`: Inicia o fluxo para transferir valores entre duas contas.
-   `[nu] Novo Usuário`: Inicia o fluxo para cadastrar um novo cliente no sistema.
-   `[nc] Nova Conta`: Inicia o fluxo para criar uma nova conta bancária para um cliente existente.
-   `[lc] Listar Contas`: Exibe um resumo de todas as contas bancárias cadastradas.
-   `[lu] Listar Usuários`: Exibe os dados de todos os clientes cadastrados.
-   `[cf] Configurações`: Acessa o menu de configurações do sistema.
-   `[q] Sair`: Encerra a aplicação.

## 3. Detalhes das Operações

### Depósito, Saque e Transferência

Para as operações de `Depositar`, `Sacar` e `Transferir`, o sistema solicitará:

1.  O **CPF** do cliente.
2.  A **seleção da conta** (se o cliente tiver mais de uma).
3.  O **valor** da operação.

### Extrato

Ao selecionar a opção de extrato, o sistema perguntará se você deseja filtrar os resultados:

`Deseja filtrar por tipo de transação? (s/d/t para saque/depósito/transferência ou deixe em branco para todas):`

-   Pressione `s` para ver apenas saques.
-   Pressione `d` para ver apenas depósitos.
-   Pressione `t` para ver apenas transferências.
-   Pressione `Enter` (deixar em branco) para ver todas as transações.

### Novo Usuário

O sistema solicitará os seguintes dados para o cadastro:
-   Nome completo
-   Data de nascimento (no formato `dd-mm-aaaa`)
-   CPF (apenas números)
-   Endereço completo
-   Telefone e Celular (com DDD, apenas números)

### Nova Conta

1.  Primeiro, o sistema pedirá o **CPF** do cliente para quem a conta será criada.
2.  Em seguida, você poderá escolher entre **Conta Corrente**, **Conta Poupança** ou **Conta Investimento**.
3.  Se for uma Conta Investimento, você deverá selecionar um dos **tipos de ativo** disponíveis.

## 4. Configurações

No menu de configurações (`[cf]`), você pode alterar o seguinte parâmetro:

-   **Salvar dados ao sair:** Pressione `1` para alternar entre `Ativado` e `Desativado`.
    -   Se **Ativado**, todos os dados da sessão atual serão salvos em um arquivo (`bank_data.pkl`) quando você sair do programa.
    -   Se **Desativado**, nenhum dado será salvo.

## 5. Para Desenvolvedores

### Log de Transações

Todas as operações de criação (cliente, conta) e transações financeiras (depósito, saque, transferência) são registradas no console. O log inclui a data, hora, nome da função, argumentos e o valor de retorno, facilitando o rastreamento e a depuração.
