# RELATÓRIO DE PLANEJAMENTO – FASE 1 (RAD)

**PROJETO:** DOCE UNIVERSO – SISTEMA DE E-COMMERCE DE CONFEITARIA  
**DISCIPLINA:** DESENVOLVIMENTO RÁPIDO DE APLICAÇÕES EM PYTHON  
**PROFESSOR:** ELTON SILVA  
**EQUIPE:**  
- Gabriel S. | Matrícula: 202403903172  
- [Nome do Aluno 2]  
- [Nome do Aluno 3]  
- [Nome do Aluno 4]  
- [Nome do Aluno 5]  

---

## 1. INFORMAÇÕES GERAIS
O projeto "Doce Universo" é uma aplicação web desenvolvida sob a metodologia Rapid Application Development (RAD). O sistema foca na comercialização e gestão de produtos de confeitaria artesanal, permitindo a personalização de pedidos através de um modelo de variantes (SKU) e o gerenciamento completo do fluxo de vendas.

---

## 2. INTRODUÇÃO
**Objetivo do Projeto:** Desenvolver uma plataforma funcional de vendas que resolva o problema da gestão manual de pedidos e estoques em pequenas confeitarias. A aplicação permite que clientes realizem pedidos personalizados e que administradores gerenciem o catálogo, usuários e vendas de forma centralizada e automatizada.

---

## 3. PLANEJAMENTO DE REQUISITOS (FASE 1 DO RAD)

### 3.1 Definição do Problema
A falta de um sistema integrado para gerenciar pedidos de doces com múltiplas variações (sabores, tamanhos e coberturas) gera erros de produção e dificuldades no controle de estoque. Além disso, a ausência de um histórico digital de clientes limita o crescimento e a análise de desempenho do negócio.

### 3.2 Requisitos Funcionais (RF)
*   **RF01 – Gestão de Catálogo:** O sistema deve permitir o CRUD completo de produtos, categorias e variações (SKU).
*   **RF02 – Autenticação de Usuários:** O sistema deve permitir cadastro, login e gerenciamento de perfil para clientes e administradores.
*   **RF03 – Carrinho de Compras:** O sistema deve permitir a seleção de itens e armazenamento temporário via sessão.
*   **RF04 – Processamento de Pedidos:** O sistema deve converter o carrinho em um pedido permanente vinculado ao usuário.
*   **RF05 – Gestão de Estoque:** O sistema deve atualizar automaticamente a quantidade de produtos após cada venda.
*   **RF06 – Exportação de Relatórios:** O sistema deve permitir a geração de planilhas (CSV/Excel) de vendas e estoque.

### 3.3 Requisitos Não Funcionais (RNF)
*   **RNF01 – Persistência de Dados:** Utilização de banco de dados relacional PostgreSQL.
*   **RNF02 – Segurança:** Proteção de rotas e validação de formulários via Django Forms.
*   **RNF03 – Qualidade de Código:** Uso mandatório de linting (Ruff) e testes unitários automatizados.
*   **RNF04 – Infraestrutura:** Execução via contêineres Docker para garantir paridade de ambientes.

### 3.4 Ferramentas e Tecnologias
*   **Linguagem:** Python 3.12
*   **Framework Web:** Django 6.0.3
*   **Banco de Dados:** PostgreSQL 14
*   **Interface Administrativa:** Django Unfold (Material Design)
*   **CI/CD:** GitHub Actions para testes e qualidade.

---

## 4. MODELO INICIAL DO BANCO DE DADOS
O esquema relacional contempla os seguintes domínios principais:
1.  **Usuários e Clientes:** Extensão do modelo nativo do Django para incluir dados de entrega e CPF.
2.  **Produtos e Variações:** Estrutura pai-filho para suportar SKUs customizados (ex: Sabor, Tamanho).
3.  **Pedidos e Itens:** Relacionamento para registro histórico de transações e quantidades vendidas.

---

## 5. DISTRIBUIÇÃO DAS TAREFAS (EQUIPE)
A divisão de responsabilidades foi estabelecida conforme as competências individuais, garantindo a autonomia das camadas:

*   **Gabriel S. | 202403903172:** Liderança técnica, Arquitetura do Sistema, Modelagem de Banco de Dados e Desenvolvimento de Backend Core.
*   **[Membro 2]:** Desenvolvimento de Interface (Fase de Design) e Implementação de Front-end (Templates Django).
*   **[Membro 3]:** Qualidade de Software, Garantia de Requisitos e Escrita de Testes Automatizados.
*   **[Membro 4]:** Desenvolvimento do Sistema de Geração e Exportação de Planilhas/Relatórios.
*   **YURI DOS SANTOS | 202408176783::** Redação do Relatório Final do Grupo e Elaboração dos Slides para Apresentação.

---
**OBS:** Este documento segue as normas da ABNT para trabalhos acadêmicos (Arial 12, Espaçamento 1.5, Texto Justificado na versão final em DOCX/PDF).
