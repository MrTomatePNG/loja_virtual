# Doce Universo - Projeto RAD

Este é o projeto **Doce Universo**, um sistema de e-commerce especializado em confeitaria e doces personalizados, desenvolvido para a disciplina de Desenvolvimento Rápido de Aplicações (RAD) em Python.

## Tecnologias
- **Linguagem:** Python
- **Framework:** Django
- **Banco de Dados:** PostgreSQL
- **Ambiente:** Docker
- **Storage:** Minio (S3) para fotos dos doces

## Domínios (Apps)
- **produtos**: Catálogo de doces, categorias e gestão de variantes (SKUs para sabores, coberturas e tamanhos).
- **usuarios**: Autenticação de clientes e perfis com histórico de pedidos.
- **pedidos**: Fluxo de compra, cálculo de frete simulado e status de entrega.
- **carrinho**: Gestão temporária de doces selecionados via sessão.

---

## Planejamento de Desenvolvimento

### 1. Distribuição de Tarefas
*   **Gabriel S. | 202403903172:** Arquitetura, Banco de Dados, Backend Core e Infraestrutura (Docker/CI).
*   **[Nome]:** Desenvolvimento do Frontend (HTML/CSS) com foco em uma vitrine de doces atrativa.
*   **[Nome]:** Escrita de testes automatizados para garantir a estabilidade das compras.
*   **[Nome]:** Desenvolvimento do sistema de geração e exportação de planilhas (Relatórios de Estoque/Vendas).
*   **[Nome]:** Documentação das regras de negócio e manual de personalização de pedidos.

### 2. Objetivos por Etapas
*   **Fase 1 (Atual):** Login de clientes e sistema de perfil com endereços de entrega.
*   **Fase 2:** Carrinho de compras e fluxo completo de pedido de doces.
*   **Fase 3:** Refatoração para SKUs (sabores/tamanhos customizados) e exportação de dados para Excel/CSV.

### 3. Regras do Projeto (Obrigatórias)
1.  **Simplicidade e Entrega:** Funcionalidades devem ser legíveis, organizadas e testáveis. Evitar complexidade desnecessária; focar no funcionamento básico primeiro.
2.  **Estabilidade:** Não modificar partes prontas sem necessidade extrema. O que já funciona não deve ser quebrado.
3.  **Independência:** O núcleo do sistema não pode parar por atrasos em partes visuais ou documentais.
4.  **Obrigatoriedade de Testes:** Novos códigos só entram na branch principal com testes unitários e aprovação do CI (GitHub Actions).

---

## REFERÊNCIAS
- **Vídeo:** [The Ideal Shape of Web Projects | The 12 Factors](https://youtu.be/gpJgtED36U4) - Fabio Akita.
- **Vídeo:** [Usando Git Direito | Limpando seus Commits!](https://youtu.be/6OokP-NE49k) - Fabio Akita.
- **Artigo:** [The Twelve-Factor App](https://12factor.net/) - Manifesto original.

**OBS:** Este documento de planejamento foi gerado com auxílio de agentes de IA com base em textos e discussões prévias sobre o nicho de doceria personalizada.
