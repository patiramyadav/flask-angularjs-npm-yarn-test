from flask.ext.api import FlaskAPI
from flask import request,jsonify

from flask.ext.cors import CORS
app = FlaskAPI(__name__)
CORS(app)

@app.route('/getData/')
def getData():
    return {'name':'roy'}

@app.route('/Authenticate',methods=['POST'])
def Authenticate():
    content = request.json
    return jsonify({'username':content['username'],'password':content['password']})


if __name__=="__main__":
    app.run(debug=True)