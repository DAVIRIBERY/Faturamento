# Faturamento
# Sistema de Cadastro de Convênios — Faturamento

## Sobre o projeto

O projeto Faturamento é um sistema desenvolvido em Python com o objetivo de centralizar e organizar as informações contratuais de diferentes operadoras de planos de saúde.

A aplicação permite cadastrar, consultar, visualizar e alterar informações relacionadas às regras de cobrança acordadas com cada convênio, facilitando a organização dos parâmetros utilizados no processo de faturamento hospitalar.

## Funcionalidades

- **Cadastro de convênios:** registro de novas operadoras e suas respectivas regras de cobrança.
- **Consulta individual:** pesquisa de convênios pelo nome, permitindo visualizar todas as informações cadastradas.
- **Alteração de informações:** atualização dos parâmetros contratuais previamente registrados.
- **Consulta geral:** exibição de todos os convênios cadastrados.
- **Registro de data:** armazenamento da data e horário do cadastro ou da última alteração.
- **Persistência de dados:** armazenamento das informações em arquivo JSON, permitindo recuperar os registros mesmo após o encerramento do programa.

## Informações armazenadas

Para cada convênio, o sistema registra:

| Campo | Descrição |
|---|---|
| Convênio | Nome da operadora |
| Tabela | Tabela de honorários médicos acordada |
| Med | Tabela de medicamentos |
| Mat | Tabela de materiais |
| Fisio_andares | Quantidade de fisioterapias por dia na clínica médica |
| Fisio_uti | Quantidade de fisioterapias por dia nas UTIs |
| Fonoaudiologia | Quantidade de consultas de fonoaudiologia por dia |
| Data | Data e horário do registro ou alteração |

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento da aplicação.
- **JSON:** formato utilizado para armazenamento persistente dos dados.
- **Datetime:** biblioteca utilizada para registrar datas e horários.
- **Listas e dicionários:** estruturas utilizadas para organizar os registros.
- **Funções:** utilizadas para modularizar as operações e organizar o código.

## Estrutura de funcionamento

O sistema possui um menu interativo com cinco opções principais:

1. Cadastrar convênio.
2. Pesquisar convênio.
3. Alterar informações cadastradas.
4. Consultar todos os convênios.
5. Encerrar o programa.

## Objetivo do desenvolvimento

O projeto tem como finalidade aplicar conhecimentos de programação Python na resolução de uma necessidade relacionada ao faturamento hospitalar, transformando informações contratuais em registros organizados e consultáveis.

Também representa uma etapa de aprendizado em desenvolvimento de sistemas, com possibilidade de evolução para integração com bancos de dados SQL e futuras funcionalidades de gerenciamento das regras de cobrança.

---

**Status:** Projeto em desenvolvimento.

**Desenvolvido com Python.**
