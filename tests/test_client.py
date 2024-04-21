import pytest
from jupyter_api import JupyterClient
import os


@pytest.fixture
def client():
    TOKEN = os.getenv("JUPYTER_TOKEN")
    JUPYTER_HOST = os.getenv("JUPYTER_HOST", "localhost:8888")
    return JupyterClient(host=JUPYTER_HOST, schema="http", token=TOKEN)


def test_jupyter_python1(client):
    # create kernel
    kernel_id = client.create_kernel(language="python3")
    assert kernel_id is not None, "kernel_idがNoneです。"

    # run code
    code = """
    a = "hello world"
    a
    """
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert result == "'hello world'", "コードの実行結果が期待通りではありません。"


def test_jupyter_python2(client):
    # create kernel
    kernel_id = client.create_kernel(language="python3")
    assert kernel_id is not None, "kernel_idがNoneです。"

    # run code
    code = """
    import time
    time.sleep(3)
    """
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert result == "", "コードの実行結果が期待通りではありません。"


def test_jupyter_python3(client):
    # create kernel
    kernel_id = client.create_kernel(language="python3")
    assert kernel_id is not None, "kernel_idがNoneです。"

    code = "print('hello world')"
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert result == "hello world\n", "コードの実行結果が期待通りではありません。"


def test_jupyter_python4(client):
    # create kernel
    kernel_id = client.create_kernel(language="python3")
    assert kernel_id is not None, "kernel_idがNoneです。"

    code = """
    import time
    for i in range(3):
        print('hello world')
        time.sleep(1)
    """
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert (
        result == "hello world\nhello world\nhello world\n"
    ), "コードの実行結果が期待通りではありません。"


def test_jupyter_python5(client):
    # create kernel
    kernel_id = client.create_kernel(language="python3")
    assert kernel_id is not None, "kernel_idがNoneです。"

    code = """
    error
    """
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert (
        "name 'error' is not defined" in result
    ), "コードの実行結果が期待通りではありません。"


def test_jupyter_bash1(client):
    # create kernel
    kernel_id = client.create_kernel(language="python3")
    assert kernel_id is not None, "kernel_idがNoneです。"

    code = "!echo hello world"
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert result == "hello world\r\n", "コードの実行結果が期待通りではありません。"


def test_jupyter_bash2(client):
    # create kernel
    kernel_id = client.create_kernel(language="python3")
    assert kernel_id is not None, "kernel_idがNoneです。"

    code = "!sleep 3"
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert result == "", "コードの実行結果が期待通りではありません。"


def test_jupyter_bash3(client):
    # create kernel
    kernel_id = client.create_kernel(language="python3")
    assert kernel_id is not None, "kernel_idがNoneです。"

    code = "!a"
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert (
        "a: command not found" in result
    ), "コードの実行結果が期待通りではありません。"


def test_jupyter_typescript1(client):
    # create kernel
    kernel_id = client.create_kernel(language="tslab")
    assert kernel_id is not None, "kernel_idがNoneです。"

    code = """
    console.log("hello world");
    """
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert result == "hello world\n", "コードの実行結果が期待通りではありません。"


def test_jupyter_typescript2(client):
    # create kernel
    kernel_id = client.create_kernel(language="tslab")
    assert kernel_id is not None, "kernel_idがNoneです。"
    # typescript code
    code = """
    var a = 1;
    var b = 2;
    var c = a + b;
    c;
    """
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert result == "\x1b[33m3\x1b[39m\n", "コードの実行結果が期待通りではありません。"


def test_jupyter_javascript1(client):
    # create kernel
    kernel_id = client.create_kernel(language="jslab")
    assert kernel_id is not None, "kernel_idがNoneです。"

    code = """
    console.log("hello world");
    """
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert result == "hello world\n", "コードの実行結果が期待通りではありません。"


def test_jupyter_javascript2(client):
    # create kernel
    kernel_id = client.create_kernel(language="jslab")
    assert kernel_id is not None, "kernel_idがNoneです。"
    # typescript code
    code = """
    var a = 1;
    var b = 2;
    var c = a + b;
    c;
    """
    result = client.execute_code(code, kernel_id, cell=False)
    client.delete_kernel(kernel_id)
    assert result == "\x1b[33m3\x1b[39m\n", "コードの実行結果が期待通りではありません。"
