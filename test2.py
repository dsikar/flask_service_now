import os

data = "testing concatenation"
osstr = "echo \"" + data + "\" >> data.txt"
          #email = request.args.get('email')
os.system(osstr)
