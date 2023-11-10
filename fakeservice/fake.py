from flask import Flask, request
import json
import requests
app = Flask(__name__)

@app.route('/foo', methods = ['GET'])
def hello():
    username = request.headers.get('X-Consumer-Username')
    msg = f"Username: {username} - Bem vindo ao nosso fake service"
    return '{"msg":"' + msg + '"}'

@app.route('/register', methods = ['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Você deveria criar seu próprio database para
    # armazenar seus usuários e senhas (ou hash delas).
    # aqui estamos fazendo um fake. 
    # O parâmetro "custom_id" seria a chave primária do
    # seu database de usuários.
    r = requests.post('http://kong:8001/consumers', data={'username': username, 'custom_id': password})
    return ('',204)

@app.route('/key', methods = ['POST'])
def getKey():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    r = requests.get(f"http://kong:8001/consumers/{username}")
    if not r.status_code == 200:
        return('',403)
    r = requests.post(f"http://kong:8001/consumers/{username}/key-auth", data={'ttl': 120})
    return (json.dumps(r.json()), 201)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')