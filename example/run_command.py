from jupyter_api import JupyterClient
import os

TOKEN = os.getenv("JUPYTER_TOKEN")
JUPYTER_HOST = os.getenv("JUPYTER_HOST", "localhost:8888")
client = JupyterClient(host=JUPYTER_HOST, schema="http", token=TOKEN)

# create kernel
kernel_id = client.create_kernel(language="python3")

# run command
print(client.execute_code(f"!ls -l", kernel_id, cell=False))

# run code
print(client.execute_code(f"print('hello world')", kernel_id, cell=False))

# delete kernel
client.delete_kernel(kernel_id)
