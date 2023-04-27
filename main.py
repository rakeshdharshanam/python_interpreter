from flask import  Flask,jsonify,request
from flask_cors import CORS, cross_origin
import subprocess,sys

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# file = open("./output.txt","w")
# sys.stdout = file



@app.route('/home',methods=["GET","POST"])
def home():
    if request.method == "GET":
        print("this is get")
        return jsonify(data)
    elif request.method == "POST":
        py_code = request.get_json()

        with open("./online_code.py", "w") as f:
            f.write((py_code['code']))
            
        output = open("./output.txt","w+")
        try:
            subprocess.call("python online_code.py",stdout=output,stderr=output)
        except Exception as e:
            print(e)
        output.close()
        
        output = open("./output.txt","r")
        output_data = output.read()
        output.close()
        return output_data



if __name__ == "__main__":
    app.run(debug=True)
