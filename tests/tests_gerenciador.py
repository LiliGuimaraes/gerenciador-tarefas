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

def test_criar_tarefa_sem_titulo():
    cliente = app.test_client()
    # o código de status deve ser 400 indicando um erro do cliente
    resposta = cliente.post('/task', data=json.dumps(
        {'descricao': 'descricao'}),
        content_type='application/json')
    assert resposta.status_code == 400

def test_listar_tarefas_deve_apresentar_tarefas_nao_finalizadas_primeiro():
    tarefas.clear()
    tarefas.append({'id': 1, 'titulo': 'tarefa 1', 'descricao': 'tarefa de numero 1',
                    'estado': True})
    tarefas.append({'id': 2, 'titulo': 'tarefa 2', 'descricao': 'tarefa de numero 2',
                    'estado': False})
    with app.test_client() as cliente:
        resposta = cliente.get('/task')
        data = json.loads(resposta.data.decode('utf-8'))
        primeira_task, segunda_task = data
        assert primeira_task['titulo'] == 'tarefa 2'
        assert segunda_task['titulo'] == 'tarefa 1'

def test_deletar_tarefa_utiliza_verbo_delete():
    tarefas.clear()
    with app.test_client() as cliente:
        resposta = cliente.delete('/task/1')
        assert resposta.status_code != 405

def test_remover_tarefa_existente_retorna_204():
    tarefas.clear()
    tarefas.append({'id': 1, 'titulo': 'titulo',
                    'descricao': 'descricao', 'estado': False})
    cliente = app.test_client()
    resposta = cliente.delete('/task/1', content_type='application/json')
    assert resposta.status_code == 204
    assert resposta.data == b''

def test_remover_tarefa_existente_remove_tarefa_da_lista():
    tarefas.clear()
    tarefas.append({'id': 1, 'titulo': 'titulo',
                    'descricao': 'descricao', 'estado': False})
    cliente = app.test_client()
    cliente.delete('/task/1', content_type='application/json')
    assert len(tarefas) == 0

def test_remover_tarefa_nao_existente():
    tarefas.clear()
    cliente = app.test_client()
    resposta = cliente.delete('/task/1', content_type='application/json')
    assert resposta.status_code == 404

def test_detalhar_tarefa_existente():
    tarefas.clear()
    tarefas.append({'id': 1, 'titulo': 'titulo',
                    'descricao': 'descricao', 'entregue': False})
    cliente = app.test_client()
    resposta = cliente.get('/task/1', content_type='application/json')
    data = json.loads(resposta.data.decode('utf-8'))
    assert resposta.status_code == 200
    assert data['id'] == 1
    assert data['titulo'] == 'titulo'
    assert data['descricao'] == 'descricao'
    assert data['entregue'] is False

def test_detalhar_tarefa_nao_existente():
    tarefas.clear()
    cliente = app.test_client()
    resposta = cliente.get('/task/1', content_type='application/json')
    assert resposta.status_code == 404

def test_atualizando_uma_tarefa_nao_existente():
    tarefas.clear()
    cliente = app.test_client()
    resposta = cliente.put('/tarefa/1', data=json.dumps(
        {'titulo': 'titulo atualizado',
         'decricao': 'descricao atualizada', 'estado': True}
    ),
        content_type='application/json')
    assert resposta.status_code == 404

def test_atualizando_uma_tarefa_com_campos_invalidos():
    tarefas.clear()
    tarefas.append({'id': 1, 'titulo': 'titulo',
                    'descricao': 'descricao', 'estado': False})
    cliente = app.test_client()
    # sem estado
    resposta = cliente.put('/tarefa/1', data=json.dumps(
        {'titulo': 'titulo atualizado',
         'decricao': 'descricao atualizada'}
    ),
        content_type='application/json')
    assert resposta.status_code == 400
    # sem descrição
    resposta = cliente.put('/tarefa/1', data=json.dumps(
        {'titulo': 'titulo atualizado',
         'estado': False}
    ),
        content_type='application/json')
    assert resposta.status_code == 400
    # sem titulo
    resposta = cliente.put('/tarefa/1', data=json.dumps(
        {'descricao': 'descricao atualizado',
         'estado': False}
    ),
        content_type='application/json')
    assert resposta.status_code == 400