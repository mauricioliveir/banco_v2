# Banco V2 - Sistema Bancário em Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

Este projeto é um sistema bancário simples desenvolvido em Python, que permite aos usuários realizar operações básicas de um banco, como depósitos, saques, visualização de extrato, cadastro de clientes e criação de contas. O código foi desenvolvido seguindo boas práticas de programação, como modularização, uso de constantes, validação de entradas e documentação clara.

---

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Depósito**:
   - Permite ao usuário depositar valores em sua conta.
   - Valida se o valor é positivo.
   - Atualiza o saldo e o extrato da conta.

2. **Saque**:
   - Permite ao usuário sacar valores de sua conta.
   - Valida se o valor é positivo, se há saldo suficiente, se o valor não excede o limite por saque e se o número máximo de saques diários não foi atingido.
   - Atualiza o saldo, o extrato e o número de saques realizados.

3. **Extrato**:
   - Exibe todas as movimentações (depósitos e saques) realizadas na conta.
   - Mostra o saldo atual.

4. **Cadastro de Cliente**:
   - Permite cadastrar um novo cliente com informações como nome, CPF, data de nascimento e endereço.
   - Valida se o CPF já está cadastrado.

5. **Criação de Conta**:
   - Permite criar uma nova conta para um cliente já cadastrado.
   - Associa a conta a uma agência e a um número de conta único.

---

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **Funções Principais**:
  - `depositar`: Realiza depósitos na conta.
  - `sacar`: Realiza saques na conta.
  - `exibir_extrato`: Exibe o extrato da conta.
  - `criar_cliente`: Cadastra um novo cliente.
  - `criar_conta`: Cria uma nova conta para um cliente.
  - `encontrar_conta_por_cpf`: Encontra uma conta pelo CPF do cliente.

- **Funções Auxiliares**:
  - `processar_deposito`: Gerencia a lógica de depósito.
  - `processar_saque`: Gerencia a lógica de saque.
  - `processar_extrato`: Gerencia a lógica de exibição do extrato.

- **Constantes**:
  - `AGENCIA`: Número da agência bancária.
  - `LIMITE_SAQUES`: Número máximo de saques permitidos por dia.
  - `LIMITE_VALOR_SAQUE`: Valor máximo permitido por saque.
  - `MSG_CONTA_NAO_ENCONTRADA`: Mensagem padrão para conta não encontrada.
  - `MSG_INFORME_CPF`: Mensagem padrão para solicitação de CPF.

- **Função Principal**:
  - `main`: Gerencia o menu interativo e a execução do sistema.

---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.
- Nenhuma dependência externa é necessária.

### Passos para Execução

1. Clone o repositório ou baixe o arquivo `banco_v2.py`.
2. Navegue até o diretório onde o arquivo está localizado.
3. Execute o seguinte comando no terminal:

   ```bash
   python banco_v2.py
   ```
4. Siga as instruções no menu interativo para realizar as operações desejadas.

## Exemplos de Uso
### Cadastro de Cliente
Selecione a opção [c] Cadastrar Cliente no menu.

Insira os dados solicitados (CPF, nome, data de nascimento, endereço).

### Criação de Conta
Selecione a opção [cc] Criar Conta no menu.

Insira o CPF do cliente cadastrado.

### Depósito
Selecione a opção [d] Depositar no menu.

Insira o CPF do cliente e o valor a ser depositado.

### Saque
Selecione a opção [s] Sacar no menu.

Insira o CPF do cliente e o valor a ser sacado.

### Extrato
Selecione a opção [e] Extrato no menu.

Insira o CPF do cliente para visualizar o extrato.

## Boas Práticas Aplicadas
### Modularização:

O código foi dividido em funções pequenas e específicas, cada uma com uma única responsabilidade.

### Uso de Constantes:

Valores fixos, como limites de saque e mensagens, foram definidos como constantes para facilitar a manutenção.

### Validação de Entradas:

As entradas do usuário são validadas para garantir que apenas valores positivos e válidos sejam processados.

### Documentação:

Todas as funções possuem docstrings explicando seu propósito, parâmetros e retornos.

Princípio DRY (Don't Repeat Yourself):

Código repetitivo foi extraído para funções reutilizáveis, como processar_deposito, processar_saque e processar_extrato.

### Legibilidade:

O código foi organizado de forma clara e legível, com nomes descritivos para variáveis e funções.

## Melhorias Futuras
### Persistência de Dados:

Implementar um sistema de armazenamento em arquivo ou banco de dados para salvar clientes e contas entre execuções.

### Interface Gráfica:

Desenvolver uma interface gráfica utilizando bibliotecas como Tkinter ou PyQt.

### Autenticação:

Adicionar um sistema de login com senha para acessar as contas.

### Transações entre Contas:

Permitir transferências entre contas de diferentes clientes.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou novas funcionalidades.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Contato
Se você tiver alguma dúvida ou sugestão, entre em contato:

Nome: Mauricio De Oliveira

[Gmail](manutencaomauricio81@gmail.com)

[GitHub](https://github.com/mauricioliveir)