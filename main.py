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
    data = {"name":"rakesh",
            "backend":"flask"}
    if request.method == "GET":
        print("this is get")
        return jsonify(data)
    elif request.method == "POST":
        # print("post is the method")
        py_code = request.get_json()
        print(py_code['code'])

        # print(py_code.split(":")[1].strip('"}'))
        # py_code = py_code.split(":")[1].strip('"}')
        # for data in py_code:
        #     print(py_code[data])
        # print(type(py_code))
        # code = ''
        # for char in py_code:
        #     if char == '\\':
        #         print("got him")
        #     else:
        #         code = code + char
        # py_code = code
        # print(py_code)
        with open("./online_code.py", "w") as f:
            f.write((py_code['code']))
        output = open("./output.txt","w+")
        try:
            subprocess.call("python online_code.py",stdout=output,stderr=output)
        except Exception as e:
            print(e)
        output.close()
        # # return request.data
        # with open("./output.txt","r")as f:
        #     output_data = f.read()
        output = open("./output.txt","r")
        output_data = output.read()
        # print(output_data)
        output.close()
        return output_data



if __name__ == "__main__":
    app.run(debug=True)
