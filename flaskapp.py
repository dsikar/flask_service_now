from flask import Flask
from flask import request
# import parse_json as pf
import os

app = Flask(__name__)
@app.route('/')
def hello_world():
  #user = request.args.get('email')
  return 'Hello from Flask How are you?' #+ user

@app.route('/data')
def data():
  email = request.args.get('email')
  return email

@app.route('/data_post', methods = ['GET', 'POST', 'DELETE'])
def data_post():
  if request.method == 'POST':  
    data = request.data # form
    osstr = "echo \"" + data + "\" >> /home/ubuntu/flaskapp/data.txt"
    # another approach, import code - note source needs modifying, i.e. do not parse
    # input parameter, define process() function, comment out __main__, define __init__.py
    # pf.process(data)
    result = os.system(osstr)
    osstr = "/usr/bin/python3 /home/ubuntu/flaskapp/parse_json.py \"" + data + "\"" 
    result = os.system(osstr)
  return data

@app.route('/google_forms', methods = ['GET', 'POST', 'DELETE'])
def google_forms():
  if request.method == 'POST':  
    # data = request.get_json() # form
    data = str(request.is_json)
    data = 'stuff'
    # payload = request.args.get('payload')
    osstr = "echo \"" + data + "\" >> /home/ubuntu/flaskapp/google_forms.txt"
    # another approach, import code - note source needs modifying, i.e. do not parse
    # input parameter, define process() function, comment out __main__, define __init__.py
    # pf.process(data)
    #result = os.system(osstr)
    #osstr = "/usr/bin/python3 /home/ubuntu/flaskapp/parse_json.py \"" + data + "\"" 
    #result = os.system(osstr)
  return 'OK' #data

methods = ['GET', 'POST', 'DELETE']
if __name__ == '__main__':
  app.run()
