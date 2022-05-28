#coding: utf-8


from sqlalchemy import Column,Integer,String,Boolean,DateTime,Date,Text
from assets.database import Base
from datetime import datetime as dt

#データベースのテーブル情報
class Player(Base):
    __tablename__ = "player"
    
    id = Column(Integer,primary_key=True)
    name = Column(Text,unique=False)
    time = Column(Integer,unique=False)
    score = Column(Integer,unique=False)

    #初期化する
    def __init__(self,name=None,time=None,score=None):
        self.name = name
        self.time = time
        self.score = score

class Point(Base):
    __tablename__ = "point"
    
    id = Column(Integer,primary_key=True)
    LAT = Column(Integer,unique=False)
    LNG = Column(Integer,unique=False)
    ALT = Column(Integer,unique=False)

    #初期化する
    #LAT=緯度、LNG=経度、ALT＝高度
    def __init__(self,LAT=None,LNG=None,ALT=None):
        self.LAT = LAT
        self.LNG = LNG
        self.ALT = ALT
