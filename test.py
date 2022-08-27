from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/abc',methods = ['GET', 'POST'])
def test1():
    if(request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/abc1/yash',methods = ['GET', 'POST'])
def test2():
    if(request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify(str(result))

@app.route('/abc1/yash/test3',methods = ['GET', 'POST'])
def test3():
    if(request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a**b
        return jsonify(str(result))

@app.route('/abc1/yash/test4',methods = ['GET', 'POST'])
def test4():
    if(request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a-b
        return jsonify(str(result))

@app.route('/abc1/yash/test5',methods = ['GET', 'POST'])
def test5():
    if(request.method =='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a/b
        return jsonify(str(result))


#the below code is to invoke the main class
if __name__ == '__main__':
    app.run()
    #the app flask method created above is being called
