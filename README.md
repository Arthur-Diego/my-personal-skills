# Repositorio Local de Skills

Este repositorio guarda suas skills para uso futuro e inclui um terminal interativo para escolher, visualizar e instalar skills em projetos.

## Como usar o terminal

Execute:

```bash
python3 bin/skills-terminal.py
```

Opcoes disponiveis:

1. Listar skills salvas.
2. Ver detalhes de uma skill.
3. Instalar uma skill em um projeto.
4. Criar esqueleto de nova skill.
5. Sair.

Para listar sem abrir o menu:

```bash
python3 bin/skills-terminal.py list
```

Para instalar direto em um projeto:

```bash
python3 bin/skills-terminal.py install refactor-arch /caminho/do/projeto
```

Isso copia a skill para:

```text
/caminho/do/projeto/.claude/skills/refactor-arch/
```

Se quiser sobrescrever uma instalacao existente:

```bash
python3 bin/skills-terminal.py install refactor-arch /caminho/do/projeto --force
```

## Estrutura do repositorio

```text
.
├── bin/
│   └── skills-terminal.py
├── skills/
│   └── refactor-arch/
│       ├── SKILL.md
│       └── references/
├── .claude/
│   └── skills/
│       └── refactor-arch/
└── reports/
```

A pasta `skills/` e a biblioteca principal. Guarde nela todas as suas skills reutilizaveis.

A pasta `.claude/skills/` fica como copia local pronta para uso no proprio repositorio.

## Como adicionar uma nova skill

Pelo terminal interativo:

```bash
python3 bin/skills-terminal.py
```

Escolha a opcao `4. Criar esqueleto de nova skill`.

Ou crie manualmente:

```text
skills/minha-skill/
├── SKILL.md
└── references/
```

O `SKILL.md` precisa ter frontmatter com `name` e `description`:

```markdown
---
name: minha-skill
description: Descricao curta dizendo quando esta skill deve ser usada.
---

# Minha Skill

Instrucoes da skill.
```

## Skill inicial: refactor-arch

A primeira skill salva neste repositorio e `refactor-arch`, criada para o desafio de auditoria e refatoracao arquitetural.

Ela e capaz de orientar um agente em tres fases:

1. Analisar uma codebase e detectar linguagem, framework, dominio e arquitetura.
2. Auditar anti-patterns e code smells com severidade, arquivo e linha.
3. Refatorar para MVC e validar que a aplicacao continua funcionando.

## Overview do desafio refactor-arch

Voce precisa entregar uma skill chamada `refactor-arch` capaz de auditar e refatorar tres projetos legados para uma arquitetura MVC, mantendo a aplicacao funcionando depois das mudancas.

Os projetos-alvo sao:

- `code-smells-project/`: Python + Flask, API de e-commerce.
- `ecommerce-api-legacy/`: Node.js + Express, API de LMS com checkout.
- `task-manager-api/`: Python + Flask, API de gerenciamento de tarefas.

O desafio tem quatro blocos principais:

1. **Analise manual**
   - Ler os tres projetos antes de automatizar.
   - Documentar no README pelo menos 5 problemas por projeto.
   - Cada projeto deve ter pelo menos 1 problema `CRITICAL` ou `HIGH`, 2 `MEDIUM` e 2 `LOW`.

2. **Construcao da skill**
   - Criar `.claude/skills/refactor-arch/SKILL.md`.
   - Criar referencias em Markdown para analise de projeto, catalogo de anti-patterns, template de relatorio, guidelines MVC e playbook de refatoracao.
   - Garantir que a skill seja agnostica de tecnologia, funcionando em Flask e Express.

3. **Execucao nos tres projetos**
   - Rodar `/refactor-arch` em cada projeto.
   - Verificar Fase 1, Fase 2 e Fase 3.
   - Salvar relatorios em `reports/audit-project-1.md`, `reports/audit-project-2.md` e `reports/audit-project-3.md`.
   - Commitar o codigo refatorado de cada projeto.

4. **Validacao final**
   - Confirmar que os endpoints originais continuam respondendo.
   - Confirmar que a estrutura MVC foi criada.
   - Confirmar que configuracoes sensiveis foram extraidas.
   - Preencher README com resultados, comparativo antes/depois e logs ou screenshots.

## Prototipo criado para o desafio

Este repositorio contem um prototipo inicial da skill em:

```text
skills/refactor-arch/
├── SKILL.md
└── references/
    ├── anti-pattern-catalog.md
    ├── mvc-guidelines.md
    ├── project-analysis.md
    ├── refactoring-playbook.md
    └── report-template.md
```

Use este prototipo como base copiavel para dentro de cada projeto:

```bash
python3 bin/skills-terminal.py install refactor-arch code-smells-project
python3 bin/skills-terminal.py install refactor-arch ecommerce-api-legacy
python3 bin/skills-terminal.py install refactor-arch task-manager-api
```

Depois, execute dentro de cada projeto:

```bash
claude "/refactor-arch"
```

## Como testar incrementalmente

1. Coloque os tres projetos-base na raiz deste repositorio.
2. Copie a pasta `.claude/` para o projeto que deseja testar primeiro.
3. Execute a skill no projeto.
4. Na Fase 2, revise o relatorio antes de aprovar a refatoracao.
5. Apos a Fase 3, rode os testes ou comandos de boot da aplicacao.
6. Ajuste os arquivos de referencia se a skill nao detectar problemas suficientes.

## Estrutura esperada na entrega

```text
desafio-skills/
├── README.md
├── code-smells-project/
│   └── .claude/skills/refactor-arch/
├── ecommerce-api-legacy/
│   └── .claude/skills/refactor-arch/
├── task-manager-api/
│   └── .claude/skills/refactor-arch/
└── reports/
    ├── audit-project-1.md
    ├── audit-project-2.md
    └── audit-project-3.md
```

## Checklist de aceite

- [ ] Fase 1 detecta linguagem, framework, dominio, arquitetura e quantidade de arquivos.
- [ ] Fase 2 gera no minimo 5 findings por projeto.
- [ ] Fase 2 inclui pelo menos 1 finding `CRITICAL` ou `HIGH` por projeto.
- [ ] Fase 2 lista arquivo e linha exatos para cada finding.
- [ ] Fase 2 pausa e pede confirmacao antes de editar arquivos.
- [ ] Fase 3 cria estrutura MVC.
- [ ] Fase 3 remove configuracoes sensiveis hardcoded.
- [ ] Fase 3 centraliza tratamento de erro.
- [ ] Fase 3 valida boot da aplicacao.
- [ ] Fase 3 valida endpoints originais.
