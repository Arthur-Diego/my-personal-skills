# Catalogo de Anti-patterns

Classifique achados por impacto real no projeto.

## CRITICAL

### Credenciais hardcoded

Sinais:

- `SECRET_KEY = "..."`, tokens, senhas ou strings de conexao diretamente no codigo.
- Chaves com nomes como `password`, `secret`, `api_key`, `jwt`.

Impacto: exposicao de dados sensiveis e configuracao insegura.

### SQL Injection

Sinais:

- SQL montado com f-string, concatenacao, template string ou interpolacao direta de input.
- `cursor.execute("... " + user_input)`.

Impacto: acesso ou manipulacao indevida de dados.

### God File / God Class / God Method

Sinais:

- Arquivo concentrando rotas, banco, regras, validacao e serializacao.
- Classe ou funcao com multiplos dominios e muitas responsabilidades.

Impacto: quebra completa de separacao de responsabilidades.

## HIGH

### Regra de negocio pesada em Controller ou Route

Sinais:

- Handler HTTP contendo calculos, fluxo de dominio, queries e validacoes complexas.
- Controller chamando diretamente muitos detalhes de infraestrutura.

Impacto: dificulta testes e manutencao.

### Acoplamento forte sem injecao ou composicao

Sinais:

- Dependencias globais instanciadas diretamente em varios arquivos.
- Uso disseminado de singletons mutaveis.

Impacto: codigo dificil de testar e substituir.

### Estado global mutavel

Sinais:

- Listas, dicionarios, objetos ou caches globais usados como fonte de verdade.
- Mutacao global em handlers concorrentes.

Impacto: comportamento imprevisivel e risco em producao.

## MEDIUM

### Query N+1

Sinais:

- Query dentro de loop.
- Para cada item, nova consulta para buscar dados relacionados.

Impacto: degradacao de performance conforme volume cresce.

### Validacao ausente ou inconsistente

Sinais:

- Uso direto de `request.json`, `req.body` ou query params sem checagem.
- Falta de validacao de campos obrigatorios, tipos e limites.

Impacto: erros 500, dados invalidos e comportamento inconsistente.

### Tratamento de erro duplicado ou ausente

Sinais:

- Varios `try/catch` ou `try/except` repetidos retornando formatos diferentes.
- Excecoes sem captura em rotas.

Impacto: respostas inconsistentes e baixa observabilidade.

## LOW

### Magic numbers e strings soltas

Sinais:

- Numeros e strings de regra sem nome explicativo.
- Status, limites e mensagens repetidos inline.

Impacto: reduz legibilidade e aumenta chance de erro em mudancas.

### Nomenclatura ruim

Sinais:

- Variaveis como `x`, `data2`, `temp`, `obj` fora de contexto pequeno.
- Funcoes com nomes genericos como `process`, `handle`, `doStuff`.

Impacto: dificulta leitura e onboarding.

### Duplicacao simples

Sinais:

- Blocos equivalentes de validacao, serializacao, query ou resposta.

Impacto: manutencao repetitiva e risco de divergencia.

## APIs deprecated

Sempre procure APIs obsoletas ou depreciadas para a versao detectada.

Sinais gerais:

- Dependencias antigas em manifestos.
- Chamadas marcadas como deprecated em documentacao oficial ou warnings.
- Uso de APIs legadas de framework substituidas por mecanismo novo.

Classificacao:

- `HIGH` se a API deprecated afeta seguranca, boot ou compatibilidade imediata.
- `MEDIUM` se afeta manutencao ou upgrade.
- `LOW` se e apenas limpeza futura sem risco direto.

