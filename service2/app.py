from flask import Flask
import random
from requests import put, get

app=Flask(__name__)

class Game:

    def roll():
        value=random.randint(1,6)
        return value
 
    d1=roll
    d2=roll
    d3=roll
    d4=roll
    d5=roll
    d6=roll

#get message name
#Create name.game object with players dice results in a list. e.g Angus.game[2,4,3,6,1]


#after request from service 4 for oject infor drop object