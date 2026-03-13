# Doce Universo - Projeto RAD

Este é o projeto **Doce Universo**, um sistema de e-commerce especializado em confeitaria artesanal e doces personalizados. O projeto é desenvolvido para a disciplina de Desenvolvimento Rápido de Aplicações (RAD) em Python, utilizando o framework Django e banco de dados PostgreSQL.

## Tecnologias
- **Linguagem:** Python 3.12
- **Framework:** Django 6.0.3
- **Banco de Dados:** PostgreSQL 14 (Dockerized)
- **Interface Administrativa:** Django Unfold (Material Design)
- **Mídia/Storage:** Minio (S3 Compatible) para persistência de imagens
- **Qualidade:** Linting com Ruff e CI via GitHub Actions

## Arquitetura de Domínios (Apps)
- **produtos**: Gestão de catálogo com suporte a **SKUs** (sabores, tamanhos e preços dinâmicos).
- **usuarios**: Autenticação, perfis de clientes e gestão de endereços de entrega.
- **carrinho**: Lógica de compras temporária gerenciada via sessões (sem persistência no DB).
- **pedidos**: Processamento de checkout, registro histórico de vendas e baixa automática de estoque.

---

## Planejamento e Governança

### 1. Distribuição de Tarefas
*   **Gabriel S. | 202403903172:** Liderança Técnica, Arquitetura, Backend Core e Infraestrutura (Docker/CI).
*   **[Nome]:** Desenvolvimento do Frontend (HTML/CSS) e UX da vitrine de doces.
*   **[Nome]:** Escrita de testes unitários e garantia de integridade das funcionalidades.
*   **[Nome]:** Desenvolvimento do sistema de geração e exportação de relatórios (CSV/Excel).
*   **[Nome]:** Redação do Relatório Final do Grupo e Elaboração dos Slides de Apresentação.

### 2. Status do Cronograma (Metodologia RAD)
*   **Fase 1 (Concluída):** Planejamento de Requisitos e Modelagem Inicial do Banco.
*   **Fase 2 (Em andamento):** Design do Usuário, Protótipos e ajustes de interface.
*   **Fase 3 (Atual):** Construção do Backend, Integração com Banco de Dados e CRUD Funcional.
*   **Fase 4 (Futura):** Transição, Testes de Aceitação e Validação Final.

### 3. Regras de Desenvolvimento (Obrigatórias)
1.  **Simplicidade RAD:** Priorizar a funcionalidade básica e testável antes de incrementos visuais.
2.  **Estabilidade de Código:** Proibido modificar estruturas estáveis sem justificativa técnica.
3.  **Independência de Camadas:** Atrasos em templates ou documentação não devem travar o desenvolvimento do núcleo (Backend).
4.  **Verificação Mandatória:** Todo código deve passar pelo Ruff e pelos Testes Unitários antes de qualquer merge na branch principal.

---

## REFERÊNCIAS
- **Vídeo:** [The Ideal Shape of Web Projects | The 12 Factors](https://youtu.be/gpJgtED36U4) - Fabio Akita.
- **Vídeo:** [Usando Git Direito | Limpando seus Commits!](https://youtu.be/6OokP-NE49k) - Fabio Akita.
- **Artigo:** [The Twelve-Factor App](https://12factor.net/) - Metodologia original.

**OBS:** O planejamento e a documentação técnica deste projeto foram gerados com auxílio de agentes de IA, visando agilidade e conformidade acadêmica.
