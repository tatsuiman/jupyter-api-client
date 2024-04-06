# Jupyter API Client

## Setup
```python
pip install jupyter-api-client
```

## example
* initialize client
```python
from jupyter_api import JupyterClient

TOKEN = os.getenv("JUPYTER_TOKEN")
client = JupyterClient(host="localhost:8888", schema="http", token=TOKEN)
```

* create kernel
```python
kernel_id = client.create_kernel(language="python3")
``` 
* run linux command or code
```python
print(client.execute_code(f"!ls -l", kernel_id, cell=False))
print(client.execute_code(f"print('hello world')", kernel_id))
```

* delete kernel
```python
client.delete_kernel(kernel_id)
```

* upload file
```python
client.upload_file("README.md", "README.md")
```
