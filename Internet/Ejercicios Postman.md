# Consumo de API REST

# 1. Descripción general de la API elegida

La API utilizada fue una API REST pública llamada RESTful API.  
Esta API permite crear, consultar y actualizar objetos dentro de colecciones utilizando peticiones HTTP.

Durante las pruebas se trabajó con una colección llamada `phones`, donde se almacenaron diferentes teléfonos con información como nombre, año y precio.

La API utiliza formato JSON para enviar y recibir información.

---

# 2. Explicación de cada solicitud

---

## 2.1 Obtener objetos de una colección

### Método HTTP usado
GET

### Endpoint

```txt
https://api.restful-api.dev/collections/phones/objects
```

### Parámetros o cuerpo de la solicitud

Headers:

```txt
x-api-key: {api_key}
```

No requiere body.

### Descripción breve de la respuesta

La respuesta retorna todos los objetos almacenados dentro de la colección `phones`.

### Ejemplo de respuesta JSON

```json
[
  {
    "id": "ff8081819d82fab6019e2fd62d1745e4",
    "name": "iphone17",
    "data": {
      "year": 2026,
      "price": 2500.99
    }
  },
  {
    "id": "ff8081819d82fab6019e2fdad3a945ea",
    "name": "iphone16",
    "data": {
      "year": 2025,
      "price": 1849.99
    }
  }
]
```

---

## 2.2 Crear un objeto en una colección

### Método HTTP usado
POST

### Endpoint

```txt
https://api.restful-api.dev/collections/phones/objects
```

### Parámetros o cuerpo de la solicitud

Headers:

```txt
x-api-key: {api_key}
Content-Type: application/json
```

Body:

```json
{
  "name": "iphone16",
  "data": {
    "year": 2025,
    "price": 1849.99
  }
}
```

### Descripción breve de la respuesta

La respuesta retorna el nuevo objeto creado junto con su identificador único (`id`).

### Ejemplo de respuesta JSON

```json
{
  "id": "ff8081819d82fab6019e2fdad3a945ea",
  "name": "iphone16",
  "data": {
    "year": 2025,
    "price": 1849.99
  }
}
```

---

## 2.3 Actualizar un objeto de una colección

### Método HTTP usado
PUT

### Endpoint

```txt
https://api.restful-api.dev/collections/phones/objects/{id}
```

### Parámetros o cuerpo de la solicitud

Headers:

```txt
x-api-key: {api_key}
Content-Type: application/json
```

Body:

```json
{
  "name": "iphone17",
  "data": {
    "year": 2026,
    "price": 2500.99
  }
}
```

### Descripción breve de la respuesta

La respuesta retorna el objeto actualizado con la nueva información enviada.

### Ejemplo de respuesta JSON

```json
{
  "id": "ff8081819d82fab6019e2fd62d1745e4",
  "name": "iphone17",
  "data": {
    "year": 2026,
    "price": 2500.99
  }
}
```

---

# 3. Qué aprendí del proceso

Durante este ejercicio aprendí cómo funcionan las APIs REST y cómo se utilizan diferentes métodos HTTP como GET, POST y PUT.

También aprendí:

- Cómo enviar requests utilizando Postman.
- Cómo trabajar con endpoints.
- Cómo enviar información en formato JSON.
- Cómo interpretar las respuestas de una API.
- Cómo funcionan los headers y la autenticación mediante API Key.

Además, entendí mejor cómo se comunican el FrontEnd y el BackEnd mediante peticiones HTTP.

---

# 4. Reflexión final

Durante este ejercicio aprendí mejor cómo funcionan las APIs y cómo utilizan el protocolo HTTP para comunicarse. También entendí que una API necesita diferentes elementos para funcionar correctamente, como el verbo HTTP que indica la acción que se desea realizar (GET, POST, PUT, etc.), la URL donde se hace el request y distintos parámetros que pueden enviarse en los headers, en la URL o incluso dentro del body de la petición.

Además, aprendí que todos estos componentes trabajan juntos para obtener una respuesta del servidor, la cual luego puede ser procesada por una aplicación o sistema.

Postman fue una herramienta muy importante durante el proceso, ya que me permitió probar diferentes parámetros y configuraciones fácilmente. Gracias a esto pude entender mejor cómo enviar requests, cómo funciona la comunicación entre cliente y servidor y cómo interpretar el formato de las respuestas retornadas por la API.