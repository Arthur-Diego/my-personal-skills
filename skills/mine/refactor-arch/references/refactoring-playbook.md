# Playbook de Refatoracao

Use estes padroes como transformacoes concretas.

## 1. Extrair configuracao hardcoded

Antes:

```python
app.config["SECRET_KEY"] = "minha-chave-super-secreta-123"
```

Depois:

```python
import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
```

## 2. Parametrizar SQL

Antes:

```python
cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
```

Depois:

```python
cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
```

## 3. Mover SQL da rota para repository/model

Antes:

```python
@app.route("/products")
def products():
    rows = db.execute("SELECT * FROM products").fetchall()
    return jsonify(rows)
```

Depois:

```python
@products_bp.get("/products")
def list_products():
    return jsonify(product_controller.list_products())
```

```python
def list_products():
    return product_repository.find_all()
```

## 4. Extrair regra de negocio do handler

Antes:

```javascript
app.post('/checkout', (req, res) => {
  const total = req.body.items.reduce((sum, item) => sum + item.price, 0);
  if (total > 100) discount = total * 0.1;
  res.json({ total: total - discount });
});
```

Depois:

```javascript
router.post('/checkout', checkoutController.createCheckout);
```

```javascript
function createCheckout(req, res, next) {
  const result = checkoutService.calculate(req.body.items);
  res.json(result);
}
```

## 5. Criar Blueprint ou Router por dominio

Antes:

```python
app.route("/users")(create_user)
app.route("/products")(list_products)
```

Depois:

```python
app.register_blueprint(user_routes.bp)
app.register_blueprint(product_routes.bp)
```

## 6. Centralizar tratamento de erro

Antes:

```javascript
try {
  // ...
} catch (err) {
  res.status(500).json({ error: err.message });
}
```

Depois:

```javascript
app.use(errorHandler);
```

```javascript
function errorHandler(err, req, res, next) {
  res.status(err.status || 500).json({ error: err.message || 'Internal error' });
}
```

## 7. Remover estado global mutavel

Antes:

```python
CURRENT_USER = None
```

Depois:

```python
def get_current_user(request_context):
    return request_context.user
```

## 8. Substituir magic numbers por constantes

Antes:

```javascript
if (items.length > 50) throw new Error('too many items');
```

Depois:

```javascript
const MAX_CHECKOUT_ITEMS = 50;
if (items.length > MAX_CHECKOUT_ITEMS) throw new Error('too many items');
```

## 9. Criar camada de validacao de entrada

Antes:

```python
name = request.json["name"]
```

Depois:

```python
payload = request.get_json() or {}
if not payload.get("name"):
    raise ValidationError("name is required")
```

## 10. Preservar contrato de endpoint

Antes de mover codigo, registre:

- Metodo HTTP.
- Path.
- Payload esperado.
- Status codes.
- Formato da resposta.

Depois da refatoracao, valide os mesmos contratos com teste, `curl`, arquivo `.http` ou cliente Flask/Express.

