from flask import Flask
import random
from threading import Thread

app = Flask('')
randomPort = random.randint(8080, 50000)

@app.route('/')
def home():
  return "SERVER UP"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
