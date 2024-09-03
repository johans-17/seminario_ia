
import requests

url = 'http://localhost:11434/api/generate'
myobj = {
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": False
}

x = requests.post(url, json = myobj)

print(x.text)

