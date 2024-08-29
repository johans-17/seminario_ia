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

# Comandos

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