from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>decode apocalypse</h1>'
 
# main driver function
if __name__ == '__main__':
    app.run(host="127.0.0.1", port= os.getenv("PORT"), debug=True)
