"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/index">Index</a>' in response.data
    assert b'<a class="nav-link" href="/aaaTesting">AAA</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CICD</a>' in response.data
    assert b'<a class="nav-link" href="/docker">DOCKER</a>' in response.data
    assert b'<a class="nav-link" href="/git">GIT</a>' in response.data
    assert b'<a class="nav-link" href="/oops">OOP</a>' in response.data
    assert b'<a class="nav-link" href="/pylintAndOthers">Pylint</a>' in response.data
    assert b'<a class="nav-link" href="/pythonFlask">PythonFlask</a>' in response.data
    assert b'<a class="nav-link" href="/solid">SOLID</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/index")
    assert response.status_code == 200
    assert b"Index" in response.data


def test_request_aaa(client):
    """This makes the index page"""
    response = client.get("/aaaTesting")
    assert response.status_code == 200
    assert b"AAA" in response.data


def test_request_cicd(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CICD" in response.data


def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"DOCKER" in response.data


def test_request_git(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"GIT" in response.data


def test_request_oop(client):
    """This makes the index page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"OOP" in response.data


def test_request_pylint(client):
    """This makes the index page"""
    response = client.get("/pylintAndOthers")
    assert response.status_code == 200
    assert b"Pylint" in response.data


def test_request_pythonFlask(client):
    """This makes the index page"""
    response = client.get("/pythonFlask")
    assert response.status_code == 200
    assert b"PythonFlask" in response.data


def test_request_solid(client):
    """This makes the index page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404

