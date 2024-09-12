# SEMINARIO IA

Repositorio de trabajo con modelos de leguaje largo usando ollama

# 1. Instalación
Primero descargamos [ollama](https://ollama.com/download) de la pagina web para el S.O correspondiente.

#### En el caso de linux ejecutamos el siguiente comando

```bash
curl -fsSL https://ollama.com/install.sh | sh
```
# 2. Inicializar ollama

Para iniciar la ejecucion de ollama ejecutaremos el siguiente comando

```bash
ollama serve
```
#### Para ver todos los comnados de ollama ejecutamos el siguiente comando

```bash
ollama
```

# 3. Instalar modelos
Ingresamos a la pagina de ollama pero entramos a la secion de [modelos](https://ollama.com/library) selecionamos el modelo de preferencia y para realizar la instalacion del modelo podemos ejecutar los siguiente comandos

#### Para descargar el modelo sin correrlo 

```bash
ollama pull nombre_del_modelo:version
```
### Ejemplo
```bash
ollama pull gemma2:2b
```
#### Para descargar el modelo y correrlo 

```bash
ollama run nombre_del_modelo:version
```
### Ejemplo
```bash
ollama run gemma2:2b
```

### Nota
Si el modelo no tiene versiones no es nesesario poner :version por ejemplo

```bash
ollama run gemma2
```

# Comandos de Ollama

algunos comandos utiles de ollama son los siguientes
```bash
  #Usando
  ollama [command]

  #command
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command
```

# Algunos API'S REQUEST 

para unar espuesta generativa

```bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}'
```
para una respuesta completa

```bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```
# API Request desde Python

```bash
import requests

url = 'http://localhost:11434/api/generate'
myobj = {
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}

x = requests.post(url, json = myobj)

print(x.text)
```


```bash
import requests
import json

url = 'http://localhost:11434/api/generate'
myobj = {
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": False
}

x = requests.post(url, json = myobj)

print(x.text)


# parse x:
y = json.loads(x.text)

# the result is a Python dictionary:
print(y["response"])
```


### Comandos GIT

```bash
git add .
git commit -m "apis request"
git push -u origin main
```

## GroqCloud
### Creacion de API Key
Se ingresa a la pagina de [GroqCloud](https://console.groq.com/) se inicia sesion con Github y se da click en Api Keys luego en Create API Key se crea la API Key y se copia la KEY

### Conectarse a la API Key
con la API Key usamos el siguiente comando para definir la variable de entorno que la contendra para su uso

```bash
export GROQ_API_KEY=<your-api-key-here>
```

### Realizar un Request

Para realizar un request se ejecuta el siguiente comando
```bash
curl -X POST "https://api.groq.com/openai/v1/chat/completions" \
     -H "Authorization: Bearer $GROQ_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"messages": [{"role": "user", "content": "why is the sky blue"}], "model": "llama3-8b-8192"}'
```

### 9. Programa Web
#### JS

Se hace uso de una función de JavaScript llamada send_request() que se utiliza para enviar una solicitud HTTP POST a un servidor local que ejecuta un modelo de lenguaje de Ollama. El formulario toma una entrada de usuario, genera un "prompt", lo envía al servidor y luego muestra la respuesta en el HTML.

```bash
function send_request() {
    // Leer valores del formulario "datos"
    // Obtiene el valor ingresado por el usuario en el campo de formulario con nombre "prompt"
    var prompt = document.forms.datos.prompt.value;

    // Define el payload que será enviado al servidor
    const PAYLOAD = {
        model: "gemma:2b",  // Define el modelo que se va a utilizar
        prompt: prompt,     // Prompt ingresado por el usuario
        seed: 1234,         // Semilla para controlar la generación (opcional)
        temperature: 0.5,   // Controla la aleatoriedad de la respuesta (0.5 es moderado)
        stream: false       // Define si la respuesta será transmitida por partes o completa
    };

    // URL del servidor local de Ollama, que está escuchando en el puerto 11434
    const URL = "http://localhost:11434/api/generate";

    // Crea un objeto XMLHttpRequest para realizar la solicitud HTTP
    var request = new XMLHttpRequest();

    // Abre una conexión asíncrona al servidor, usando el método POST
    request.open('POST', URL, true);

    // Configura los headers de la solicitud para enviar JSON
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Content-Type", "application/json");

    // Envía la solicitud con el cuerpo (payload) en formato JSON
    request.send(JSON.stringify(PAYLOAD));

    // Se ejecuta cuando la respuesta del servidor esté lista
    request.onload = () => {
        // Verifica si la solicitud fue exitosa (estado 200 significa "OK")
        if (request.status === 200) {
            // Almacena la respuesta del servidor en formato texto
            const response = request.responseText;

            // Convierte la respuesta de texto a un objeto JSON para manipularlo
            const json = JSON.parse(response);

            // Muestra la respuesta en la consola del navegador para depuración
            console.log("response: " + response);
            console.log("json: " + json);

            // Selecciona el elemento <div> con id "responses" donde se mostrará la respuesta
            const responses = document.getElementById("responses");

            // Crea dos elementos <p> para mostrar el prompt y la respuesta
            var p_ask = document.createElement("p");
            var p_response = document.createElement("p");

            // Estilos CSS para el prompt y la respuesta
            p_ask.setAttribute("style", "color:blue;text-align:right");
            p_response.setAttribute("style", "color:green;text-align:left");

            // Inserta el prompt ingresado por el usuario en el párrafo
            p_ask.innerHTML = prompt;

            // Inserta la respuesta del modelo en el párrafo (toma solo el campo "response" del JSON)
            p_response.innerHTML = json.response;

            // Agrega los párrafos al <div> responses para que se muestren en el DOM
            responses.appendChild(p_ask);
            responses.appendChild(p_response);
        } else {
            // Si la solicitud falla, muestra una alerta al usuario
            alert("Fallo en la conexión con el servidor");
        }
    };
};

```

#### HTML

#### Cabecera (head):

Incluye los metadatos y referencias a la CDN de Bootstrap para agregar estilos.
Define el archivo ollama_request.js para manejar la lógica de envío de la solicitud HTTP.

#### Cuerpo (body):

Contiene un formulario simple con un campo de entrada de texto para ingresar el "prompt" y un botón para enviar la consulta.
El resultado de la consulta se muestra en un div con el id responses.

```bash
<!DOCTYPE html>
<html lang="en">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <meta charset="UTF-8">
    <script type="text/javascript" src="../static/js/ollama_request.js"></script>
    <title>IA Generativa</title>
</head>

<body>
    <div class="container">
        <h1>Ollama UI</h1>

        <form name="datos">
            <div class="mb-3">
                <label for="prompt" class="form-label">Escribe tu consulta (prompt)</label>
                <input type="text" class="form-control" id="prompt" name="prompt" required placeholder="Prompt">
            </div>
            <input type="button" class='btn btn-primary' onclick="send_request()" value="Consultar">
        </form>
        <div id="responses">
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/gh/MarketingPipeline/Markdown-Tag/markdown-tag.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

</body>

</html>
```