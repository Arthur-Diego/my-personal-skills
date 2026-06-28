# Guidelines MVC

Objetivo: separar responsabilidade sem mudar contratos publicos.

## Estrutura Python/Flask sugerida

```text
src/
├── app.py
├── config/
│   └── settings.py
├── controllers/
├── models/
├── views/
│   └── routes.py
├── middlewares/
│   └── error_handler.py
└── repositories/
```

Mapeamento:

- `views/routes`: registra rotas e traduz HTTP para chamada de controller.
- `controllers`: orquestra casos de uso e validacao de entrada.
- `models`: entidades, acesso a dados e queries.
- `repositories`: persistencia quando separar queries dos models for mais claro.
- `config`: variaveis de ambiente e defaults seguros.
- `middlewares`: erros, CORS, auth, logging.

## Estrutura Node.js/Express sugerida

```text
src/
├── app.js
├── server.js
├── config/
│   └── settings.js
├── controllers/
├── models/
├── routes/
├── middlewares/
│   └── errorHandler.js
└── repositories/
```

Mapeamento:

- `routes`: define path/metodo e chama controller.
- `controllers`: fluxo de aplicacao.
- `models`: entidades e acesso a dados.
- `repositories`: queries e adaptadores de storage.
- `config`: ambiente e constantes.
- `middlewares`: tratamento transversal.

## Regras

- Route nao deve conter SQL nem regra de negocio pesada.
- Controller nao deve montar SQL manualmente.
- Model/repository nao deve depender de request/response HTTP.
- Configuracao sensivel deve vir de variavel de ambiente.
- Entry point deve ser pequeno e claro.
- Erros devem retornar formato consistente.

