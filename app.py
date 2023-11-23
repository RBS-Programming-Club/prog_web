from flask import Flask, render_template
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def hello_world():
    return render_template("index.html")
 
# main driver function
if __name__ == '__main__':
    app.run(host="127.0.0.1", port= os.getenv("PORT"), debug=True)
