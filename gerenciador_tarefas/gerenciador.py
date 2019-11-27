from fastapi import FastAPI
from flask import request
from operator import itemgetter

app = FastAPI()


TAREFAS = []


@app.get('/tarefas')
def listar():
    return TAREFAS

@app.route('/task', methods=['POST'])
def criar():
    return jsonify()

@app.route('/task', methods=['POST'])
def criar():
    titulo = request.json.get('titulo')
    descricao = request.json.get('descricao')
    tarefa = {
        'id': len(tarefas) + 1,
        'titulo': titulo,
        'descricao': descricao,
        'estado': False
    }
    return jsonify(tarefa)

@app.route('/task')
def listar():
    return jsonify(sorted(tarefas, key=itemgetter('estado')))

@app.route('/task/<int:id_tarefa>', methods=['DELETE'])
def remover(id_tarefa):
    return ''

@app.route('/task/<int:id_tarefa>', methods=['DELETE'])
def remover(id_tarefa):
    return '', 204

@app.route('/task/<int:id_tarefa>', methods=['DELETE'])
def remover(id_tarefa):
    tarefa = [tarefa for tarefa in tarefas if tarefa['id'] == id_tarefa]
    tarefas.remove(tarefa[0])
    return '', 204

@app.route('/task/<int:id_tarefa>', methods=['DELETE'])
def remover(id_tarefa):
    tarefa = [tarefa for tarefa in tarefas if tarefa['id'] == id_tarefa]
    if not tarefa:
        abort(404)
    tarefas.remove(tarefa[0])
    return '', 204

@app.route('/task/<int:id_tarefa>', methods=['GET'])
def detalhar(id_tarefa):
    tarefa = [tarefa for tarefa in tarefas if tarefa['id'] == id_tarefa]
    return jsonify(tarefa[0])

@app.route('/task/<int:id_tarefa>', methods=['GET'])
def detalhar(id_tarefa):
    tarefa = [tarefa for tarefa in tarefas if tarefa['id'] == id_tarefa]
    if not tarefa:
        abort(404)
    return jsonify(tarefa[0])

@app.route('/tarefa/<int:id_tarefa>', methods=['PUT'])
def atualizar(id_tarefa):
    tarefa = [tarefa for tarefa in tarefas if tarefa['id'] == id_tarefa]
    titulo = request.json.get('titulo')
    descricao = request.json.get('descricao')
    estado = request.json.get('estado')
    tarefa_escolhida = tarefa[0]
    tarefa_escolhida['titulo'] = titulo or tarefa_escolhida['titulo']
    tarefa_escolhida['descricao'] = descricao or tarefa_escolhida['descricao']
    tarefa_escolhida['estado'] = estado or tarefa_escolhida['estado']
    return jsonify(tarefa_escolhida)

@app.route('/tarefa/<int:id_tarefa>', methods=['PUT'])
def atualizar(id_tarefa):
    tarefa = [tarefa for tarefa in tarefas if tarefa['id'] == id_tarefa]
    titulo = request.json.get('titulo')
    descricao = request.json.get('descricao')
    entregue = request.json.get('entregue')
    if not tarefa:
        abort(404)
    tarefa_escolhida = tarefa[0]
    tarefa_escolhida['titulo'] = titulo or tarefa_escolhida['titulo']
    tarefa_escolhida['descricao'] = descricao or tarefa_escolhida['descricao']
    tarefa_escolhida['entregue'] = entregue or tarefa_escolhida['entregue']
    return jsonify(tarefa_escolhida)

@app.route('/tarefa/<int:id_tarefa>', methods=['PUT'])
def atualizar(id_tarefa):
    tarefa = [tarefa for tarefa in tarefas if tarefa['id'] == id_tarefa]
    titulo = request.json.get('titulo')
    descricao = request.json.get('descricao')
    estado = request.json.get('estado')
    if not tarefa:
        abort(404)
    if not descricao or not titulo or estado is None:
        abort(400)
    tarefa_escolhida = tarefa[0]
    tarefa_escolhida['titulo'] = titulo or tarefa_escolhida['titulo']
    tarefa_escolhida['descricao'] = descricao or tarefa_escolhida['descricao']
    tarefa_escolhida['estado'] = estado or tarefa_escolhida['estado']
    return jsonify(tarefa_escolhida)