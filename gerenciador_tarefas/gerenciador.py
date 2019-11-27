from fastapi import FastAPI
from flask import request


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
