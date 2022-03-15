from flask import Flask
from flask import request
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
    # email = request.form.getlist('email_id[]')
    #email = "myemail"
    #mydict = data.to_dict()
    #dictstr = ''
    #for key in mydict:
    #    dictstr = dictstr + ',  ' + key
    osstr = "echo \"" + data + "\" >> /home/ubuntu//flaskapp/data.txt"
  #email = request.args.get('email')
    os.system(osstr)
  return data



methods = ['GET', 'POST', 'DELETE']
if __name__ == '__main__':
  app.run()
