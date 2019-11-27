from starlette.testclient import TestClient
from gerenciador_tarefas.gerenciador import app, TAREFAS


def test_quando_listar_tarefas_devo_ter_como_retorno_codigo_de_status_200():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200

def test_quando_listar_tarefas_formato_de_retorno_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.headers["Content-Type"] == "application/json"

def test_quando_listar_tarefas_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert isinstance(resposta.json(), list)

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_id():
    TAREFAS.append({"id": 1})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "id" in resposta.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_titulo():
    TAREFAS.append({"titulo": "titulo 1"})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "titulo" in resposta.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_descricao():
    TAREFAS.append({"descricao": "descricao 1"})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "descricao" in resposta.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_um_estado():
    TAREFAS.append({"estado": "finalizado"})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "estado" in resposta.json().pop()
    TAREFAS.clear()

def test_criar_tarefa_aceita_post():
    with app.test_client() as cliente:
        resposta = cliente.post('/task')
        assert resposta.status_code != 405

def test_criar_tarefa_retorna_tarefa_inserida():
    tarefas.clear()
    cliente = app.test_client()
    # realiza a requisição utilizando o verbo POST
    resposta = cliente.post('/task', data=json.dumps({
        'titulo': 'titulo',
        'descricao': 'descricao'}),
        content_type='application/json')
    # é realizada a análise e transformação para objeto python da resposta
    data = json.loads(resposta.data.decode('utf-8'))
    assert data['id'] == 1
    assert data['titulo'] == 'titulo'
    assert data['descricao'] == 'descricao'
    # qaundo a comparação é com True, False ou None, utiliza-se o "is"
    assert data['estado'] is False

def test_criar_tarefa_codigo_de_status_retornado_deve_ser_201():
    with app.test_client() as cliente:
        resposta = cliente.post('/task', data=json.dumps({
            'titulo': 'titulo',
            'descricao': 'descricao'}),
            content_type='application/json')
        assert resposta.status_code == 201

def test_criar_tarefa_insere_elemento_no_banco():
    tarefas.clear()
    cliente = app.test_client()
    # realiza a requisição utilizando o verbo POST
    cliente.post('/task', data=json.dumps({
        'titulo': 'titulo',
        'descricao': 'descricao'}),
        content_type='application/json')
    assert len(tarefas) > 0

def test_criar_tarefa_sem_descricao():
    cliente = app.test_client()
    # o código de status deve ser 400 indicando um erro do cliente
    resposta = cliente.post('/task', data=json.dumps({'titulo': 'titulo'}),
                            content_type='application/json')
    assert resposta.status_code == 400