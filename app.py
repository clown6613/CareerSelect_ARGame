#coding: utf-8
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET'])
def getpoint():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    name = request.form['name']
    score = request.form['score']
    time = request.form['time']
    #return name,score,time
    return render_template('index_result.html',name=name,score=score,time=time)

if __name__ == '__main__':
    app.run(debug=False)