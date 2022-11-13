import os

HOST = "127.0.0.1"
PORT = 8000
URL = f"http://{HOST}:{PORT}"

TOKEN = os.environ["TOKEN"]
WEBHOOK = "https://58d4-178-66-157-187.eu.ngrok.io"
WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = WEBHOOK + WEBHOOK_PATH
