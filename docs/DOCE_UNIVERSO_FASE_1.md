# RELATÓRIO DE DESENVOLVIMENTO – FASE 1: PLANEJAMENTO

**Projeto:** Doce Universo – E-commerce de Confeitaria Personalizada  
**Disciplina:** Desenvolvimento Rápido de Aplicações em Python (RAD)  
**Professor:** Elton Silva  
**Semestre:** 2026_01  

---

## 1. INFORMAÇÕES GERAIS DO PROJETO
O projeto "Doce Universo" consiste em uma plataforma de e-commerce focada no setor de confeitaria artesanal. O sistema permite a gestão de produtos doces, controle de estoque e personalização de pedidos através de variantes (SKUs), visando facilitar a operação de pequenos produtores e a experiência de compra do cliente final.

---

## 2. FASE 1 – PLANEJAMENTO DE REQUISITOS

### 2.1 Definição do Problema
Pequenas confeitarias enfrentam dificuldades na gestão manual de pedidos personalizados (sabores, coberturas e tamanhos variados), resultando em erros de estoque e falta de histórico de clientes. A ausência de uma interface digital centralizada limita o alcance de novos clientes e a eficiência na geração de relatórios de vendas.

### 2.2 Objetivo do Sistema
Desenvolver uma aplicação funcional utilizando a metodologia RAD que permita o gerenciamento completo (CRUD) de produtos e pedidos, com suporte a variantes customizáveis, garantindo persistência de dados e uma interface de usuário intuitiva.

### 2.3 Requisitos Funcionais (RF)
*   **RF01 – Gestão de Produtos:** O sistema deve permitir criar, ler, atualizar e excluir (CRUD) doces e categorias.
*   **RF02 – Gestão de Variantes (SKU):** O sistema deve permitir a criação de variantes para cada doce (ex: sabores, tamanhos).
*   **RF03 – Autenticação:** O sistema deve permitir o cadastro e login de clientes e administradores.
*   **RF04 – Carrinho de Compras:** O sistema deve permitir a seleção de itens e armazenamento temporário via sessão.
*   **RF05 – Gestão de Pedidos:** O sistema deve registrar pedidos vinculados a usuários, com histórico completo.
*   **RF06 – Exportação de Dados:** O sistema deve permitir a geração de planilhas (CSV/Excel) de estoque e vendas.

### 2.4 Requisitos Não Funcionais (RNF)
*   **RNF01 – Persistência:** Utilização de banco de dados relacional PostgreSQL.
*   **RNF02 – Validação:** Validação obrigatória de campos como CPF, e-mail e quantidade de estoque.
*   **RNF03 – Desempenho:** Interface responsiva focada em carregamento rápido (metodologia RAD).
*   **RNF04 – Qualidade:** Uso de linting (Ruff) e testes automatizados (CI via GitHub Actions).

### 2.5 Tecnologias Escolhidas
*   **Linguagem:** Python 3.12
*   **Framework Web:** Django 6.0.3 (RAD focus)
*   **Banco de Dados:** PostgreSQL 14 (Dockerized)
*   **Gerenciador de Dependências:** uv (astral-sh)
*   **Armazenamento de Mídia:** Minio (S3 Compatible)
*   **Qualidade e CI:** Ruff e GitHub Actions

### 2.6 Modelo Inicial do Banco de Dados
O sistema baseia-se em um modelo relacional com as seguintes entidades principais:
1.  **Categoria:** Identificação e agrupamento dos doces.
2.  **Produto:** Entidade pai contendo nome, descrição e imagens.
3.  **ProdutoVariant (SKU):** Entidade relacionada que define preço e estoque por combinação de atributos (ex: Brigadeiro + Pistache + 30g).
4.  **Usuario/Cliente:** Dados de autenticação e perfis de entrega.
5.  **Pedido/ItemPedido:** Registro das transações e itens vendidos.

---

## 3. DIVISÃO DE TAREFAS (Grupo)
*   **[Seu Nome]:** Liderança técnica, Arquitetura de Software, Modelagem de Dados e Integração Backend.
*   **[Membro 2]:** Desenvolvimento de Interface (Design do Usuário) e Front-end (Templates Django).
*   **[Membro 3]:** Qualidade de Software, Escrita de Testes Unitários e Validação de Requisitos.
*   **[Membro 4]:** Desenvolvimento do Sistema de Geração de Planilhas e Relatórios.
*   **[Membro 5]:** Documentação Técnica, Regras de Negócio e Manual do Usuário.

---
**OBS:** Este documento reflete o planejamento inicial iterativo conforme os princípios do Rapid Application Development (RAD).
