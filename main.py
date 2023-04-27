from flask import  Flask,jsonify,request
from flask_cors import CORS, cross_origin
import subprocess,sys

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/home',methods=["GET","POST"])
def home():
    data = {"name":"rakesh",
            "backend":"flask"}
    if request.method == "GET":
        print("this is get")
        return jsonify(data)
    elif request.method == "POST":
        # print("post is the method")
        py_code = request.get_json()
        print(py_code['code'])

        with open("./online_code.py", "w") as f:
            f.write((py_code['code']))
        output = open("./output.txt","w+")
        try:
            subprocess.call("python online_code.py",stdout=output,stderr=output)
        except Exception as e:
            print(e)
        output.close()

@app.route('/js', methods=["GET", "POST"])
def js():
    data = {"name": "rakesh",
            "backend": "flask"}
    if request.method == "GET":
        print("this is get")
        return jsonify(data)
    elif request.method == "POST":
        # print("post is the method")
        py_code = request.get_json()
        print(py_code['code'])

        with open("./online_code.py", "w") as f:
            f.write((py_code['code']))
        output = open("./output.txt", "w+")
        try:
            subprocess.call("python online_code.py", stdout=output, stderr=output)
        except Exception as e:
            print(e)
        output.close()

        output = open("./output.txt","r")
        output_data = output.read()
        # print(output_data)
        output.close()
        return output_data



if __name__ == "__main__":
    app.run(debug=True)
