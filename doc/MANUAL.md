# 🏦 Manual de Utilização — Sistema Bancário

Este manual orienta o uso do Sistema Bancário via linha de comando.

---

## 1️⃣ Iniciando a Aplicação

Para iniciar o sistema, navegue até o diretório `banco_modular` e execute:
```bash
python src/main.py
```

### ♻️ Carregando Dados Anteriores

Ao iniciar:
> **Deseja [c]arregar os dados ou iniciar uma [n]ova sessão?**
- 🔄 Digite `c` para continuar de onde parou
- 🆕 Digite `n` para iniciar uma sessão nova (os dados antigos serão apagados)

---

## 🏠 Menu Principal

Após a inicialização, o menu principal exibe:

- 💰 `[d] Depositar`: Iniciar depósito em uma conta
- 🏧 `[s] Sacar`: Sacar um valor de uma conta
- 📄 `[e] Extrato`: Exibir extrato de uma conta
- 🔁 `[t] Transferir`: Transferir valores entre contas
- 👤 `[nu] Novo Usuário`: Cadastrar novo cliente
- 🏦 `[nc] Nova Conta`: Criar conta para cliente existente
- 📋 `[lc] Listar Contas`: Resumo das contas cadastradas
- 🗂️ `[lu] Listar Usuários`: Dados de todos os clientes
- ⚙️ `[cf] Configurações`: Menu de configurações
- ❌ `[q] Sair`: Encerra a aplicação

---

## 🧩 Detalhes das Operações

### 💸 Depósito, Saque e Transferência

Para estas operações, serão solicitados:
1. 🆔 **CPF** do cliente
2. 💳 Seleção da conta (se houver mais de uma)
3. 💲 Valor da operação

### 📄 Extrato

Ao selecionar extrato, você pode filtrar:
> **Deseja filtrar por tipo de transação? (s/d/t para saque/depósito/transferência ou deixe em branco para todas):**
- 🏧 `s`: Saques
- 💰 `d`: Depósitos
- 🔁 `t`: Transferências
- ⏸️ _Enter_: Todas as transações

### 👤 Novo Usuário

Dados necessários:
- 📝 Nome completo
- 🎂 Data de nascimento (dd-mm-aaaa)
- 🆔 CPF (apenas números)
- 🏠 Endereço completo
- ☎️ Telefone/Celular (com DDD)

### 🏦 Nova Conta

1. Informe o **CPF** do cliente
2. Escolha o tipo: Conta Corrente, Poupança ou Investimento
3. Para Conta Investimento, selecione o tipo de ativo

---

## ⚙️ Configurações

No menu `[cf]` é possível alterar:

- 💾 **Salvar dados ao sair**: 
  - Pressione `1` para alternar entre Ativado/Desativado
  - Se **Ativado**: dados salvos em `bank_data.pkl` ao sair
  - Se **Desativado**: dados não serão salvos

---

## 👩‍💻 Para Desenvolvedores

### 🪵 Log de Transações

Todas as operações (criação de cliente, conta, transações) são registradas no console, com data, hora, função e argumentos.

---

Se desejar ajustes nos ícones, estrutura ou tradução, posso adaptar o manual conforme sua preferência!