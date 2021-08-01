from flask import Flask
from threading import Thread
from bot import *

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run()

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == '__main__':
    keep_alive()
    main()