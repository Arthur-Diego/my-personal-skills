# Analise de Projeto

Use estas heuristicas para detectar stack e arquitetura.

## Linguagem e framework

- Python:
  - `requirements.txt`, `pyproject.toml`, `Pipfile`, arquivos `.py`.
  - Flask: imports de `flask`, `Flask(__name__)`, decorators `@app.route` ou `Blueprint`.
  - Django: `manage.py`, `settings.py`, `urls.py`.
  - FastAPI: imports de `fastapi`, `FastAPI()`, decorators `@app.get`.
- Node.js:
  - `package.json`, arquivos `.js`, `.ts`, `.mjs`, `.cjs`.
  - Express: dependencia `express`, uso de `express()`, `app.get`, `router.post`.
  - NestJS: `@nestjs/*`, `Controller`, `Injectable`, `Module`.

## Banco de dados

- SQLite: `sqlite3`, arquivos `.db`, `sqlite://`.
- SQLAlchemy: `sqlalchemy`, `db.Model`, `create_engine`.
- PostgreSQL: `pg`, `psycopg2`, `postgres://`.
- MySQL: `mysql`, `pymysql`, `mysql2`.
- MongoDB: `mongoose`, `pymongo`, `mongodb://`.

## Arquitetura atual

Classifique a arquitetura pelo acoplamento observado:

- Monolito sem camadas: rotas, SQL, validacao e regra de negocio no mesmo arquivo.
- Parcialmente organizado: possui pastas, mas responsabilidades misturadas.
- MVC incompleto: models/routes/controllers existem, mas ha vazamento de regra ou dados.
- MVC aceitavel: camadas separadas, entry point claro e config externa.

## Mapeamento de rotas

Procure:

- Flask: `@app.route`, `@blueprint.route`, `add_url_rule`.
- Express: `app.get`, `app.post`, `router.put`, `router.delete`, `app.use('/prefix', router)`.

Registre metodo, path, arquivo, linha e funcao handler.

## Dominio da aplicacao

Inferir a partir de:

- Rotas: `/products`, `/orders`, `/users`, `/tasks`, `/courses`, `/checkout`.
- Tabelas ou colecoes.
- Classes e funcoes.
- Arquivos `.http`, seeds, fixtures e exemplos de payload.

