#coding: utf-8
from flask import Flask,request,render_template
from assets.database import db_session
from assets.models import Player,Point
app = Flask(__name__)

@app.route('/',methods=['GET'])
def getpoint():
    # data = db_session.query(Point.id,Point.point).all()
    data = db_session.query(Player.name, Player.time, Player.score).all()
    return render_template('index.html',data=data)
    # return data

@app.route('/result',methods=['POST'])
def result():
    name = request.form['name']
    score = request.form['score']
    score = int(score)
    time = request.form['time']
    time = int(time)
    #return name,score,time
    row = Player(score=score,time=time,name=name)
    db_session.add(row)
    # row = Point(point=1)
    # db_session.add(row)
    db_session.commit()
    return render_template('index_result.html',name=name,score=score,time=time)

if __name__ == '__main__':
    app.run(debug=False)