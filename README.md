# Loja Virtual - Projeto RAD

Este é um projeto de CRUD simples de uma lojinha virtual, desenvolvido para a disciplina de Desenvolvimento Rápido de Aplicações (RAD) em Python.

## Tecnologias
- **Linguagem:** Python
- **Framework:** Django
- **Banco de Dados:** PostgreSQL
- **Ambiente:** Docker

## Domínios (Apps)
- **produtos**: Gerencia o catálogo de produtos, categorias e estoque.
- **usuarios**: Cuida do gerenciamento de clientes e autenticação.
- **pedidos**: Lida com o processo de compra e histórico de pedidos.
- **carrinho**: Responsável pelo carrinho de compras temporário (gerenciado por lógica de sessão).

---

## Planejamento de Desenvolvimento

Este documento define a divisão de trabalho e as regras de execução do projeto, priorizando a entrega funcional e a estabilidade do código.

### 1. Distribuição de Tarefas
*   **[Seu Nome]:** Arquitetura, Banco de Dados, lógica de Backend e Servidor (Docker/CI).
*   **[Nome]:** Desenvolvimento das telas (HTML) e estilização visual (CSS).
*   **[Nome]:** Escrita de testes automatizados para novas funcionalidades.
*   **[Nome]:** Preparação de dados de produtos e organização de planilhas para importação.
*   **[Nome]:** Redação de manuais e documentação das regras de negócio.

### 2. Objetivos por Etapas
*   **Fase 1 (Atual):** Finalizar cadastro, login e perfil do cliente com endereço.
*   **Fase 2:** Implementar o carrinho de compras e o fluxo de fechamento de pedido.
*   **Fase 3:** Evoluir o modelo de produtos para SKUs (variantes) e importar dados via CSV.

### 3. Regras do Projeto
1.  **Simplicidade e Entrega:** Implementar funcionalidades de forma legível, organizada e testável. Deve-se evitar estruturas complexas e não criar nada além do mínimo necessário para o funcionamento básico de cada tarefa.
2.  **Estabilidade do Código:** Evitar modificações em partes do sistema que já estão funcionando, a menos que seja estritamente necessário para a nova tarefa. Não se deve quebrar o que já foi entregue.
3.  **Independência de Tarefas:** Se uma tarefa travar, o membro deve reportar imediatamente e auxiliar em outra área. O núcleo do sistema não pode parar por pendências visuais ou de documentação.
4.  **Obrigatoriedade de Testes:** Nenhuma funcionalidade nova será aceita sem o seu respectivo teste unitário. O código só será integrado à branch principal se passar em todas as verificações automáticas.

---

## REFERÊNCIAS
- **Vídeo:** [The Ideal Shape of Web Projects | The 12 Factors](https://youtu.be/gpJgtED36U4) - Fabio Akita.
- **Vídeo:** [Usando Git Direito | Limpando seus Commits!](https://youtu.be/6OokP-NE49k) - Fabio Akita.
- **Artigo:** [The Twelve-Factor App](https://12factor.net/) - Manifesto original.

**OBS:** Este documento de planejamento foi gerado com auxílio de agentes de IA com base em textos e discussões prévias.
