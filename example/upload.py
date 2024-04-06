from jupyter_api import JupyterClient
import os

TOKEN = os.getenv("JUPYTER_TOKEN")
JUPYTER_HOST = os.getenv("JUPYTER_HOST", "localhost:8888")
client = JupyterClient(host=JUPYTER_HOST, schema="http", token=TOKEN)
print(client.upload_file("../README.md", "README1.md"))
