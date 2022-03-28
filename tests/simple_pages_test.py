"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/aaaTesting">AAA Testing</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/oops">OOPS</a>' in response.data
    assert b'<a class="nav-link" href="/pylintAndOthers">Pylint and Others</a>' in response.data
    assert b'<a class="nav-link" href="/pythonFlask">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/solid">SOLID</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data


def test_request_aaa(client):
    """This makes the index page"""
    response = client.get("/aaaTesting")
    assert response.status_code == 200
    assert b"AAA Testing" in response.data


def test_request_cicd(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data


def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_request_git(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data


def test_request_oop(client):
    """This makes the index page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"OOPS" in response.data


def test_request_pylint(client):
    """This makes the index page"""
    response = client.get("/pylintAndOthers")
    assert response.status_code == 200
    assert b"Pylint and Others" in response.data


def test_request_pythonFlask(client):
    """This makes the index page"""
    response = client.get("/pythonFlask")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data


def test_request_solid(client):
    """This makes the index page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data



