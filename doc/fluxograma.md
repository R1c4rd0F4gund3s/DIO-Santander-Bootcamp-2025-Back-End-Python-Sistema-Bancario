```mermaid
flowchart TD
    A[Início] --> B{Arquivo de dados existe?};
    B -- Sim --> C{Carregar dados?};
    B -- Não --> D[Inicia com listas vazias];
    C -- Sim --> E[Carrega clientes e contas do arquivo];
    C -- Não --> F[Apaga arquivo de dados e inicia com listas vazias];
    D --> G[Loop Principal: Exibe Menu];
    E --> G;
    F --> G;
    
    G --> H{Opção escolhida?};
    H -- [d] Depositar --> I[Fluxo de Depósito];
    H -- [s] Sacar --> J[Fluxo de Saque];
    H -- [e] Extrato --> K_SUB;
    H -- [t] Transferir --> L[Fluxo de Transferência];
    H -- [nu] Novo Usuário --> M[Fluxo de Criação de Cliente];
    H -- [nc] Nova Conta --> N[Fluxo de Criação de Conta];
    H -- [lc/lu] Listar --> O[Fluxo de Listagem];
    H -- [cf] Config. --> P[Menu de Configurações];
    
    subgraph K_SUB [Fluxo de Extrato]
        direction LR
        K1[Obtém cliente e conta]
        K2{Deseja filtrar?}
        K3[Define tipo de filtro]
        K4[Gera relatório com filtro]
        K5[Gera relatório completo]
        K6[Exibe extrato e saldo]
        
        K1 --> K2
        K2 -- Sim --> K3 --> K4
        K2 -- Não --> K5
        K4 --> K6
        K5 --> K6
    end

    I --> G;
    J --> G;
    K_SUB --> G;
    L --> G;
    M --> G;
    N --> G;
    O --> G;
    P --> G;

    H -- [q] Sair --> Q{Salvar ao sair ativado?};
    Q -- Sim --> R[Salva dados no arquivo];
    Q -- Não --> S[Apaga arquivo de dados se existir];
    R --> T[Fim];
    S --> T;

```
