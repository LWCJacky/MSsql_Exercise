import os
from flask import Flask,send_from_directory,render_template,request
from flask_socketio import SocketIO
from instance.config import Config,DevelopmentConfig
from sqldome1 import sad
from ReInt import INint
app = Flask(__name__, template_folder="./",instance_relative_config=True)
socketio = SocketIO(app)

6

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['POST', 'GET'])
def query():
    return render_template('app.html')

@app.route('/sql.json')
def sqlJson():
    id=request.values.get('id')
    print(id)
    if INint().Isint(id):
        sql=sad()
        data=sql.go(id)
        return data

@socketio.on("login")
def logingo(msg):
    ...
if __name__=="__main__":
    socketio.run(app)