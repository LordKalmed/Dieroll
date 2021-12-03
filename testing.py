import requests
from flask import Flask, request

#comp=requests.get("http://192.168.1.13:5001/comp")
player=request.get_json("http://192.168.96.3:5002/player")

#if int(player.text) > int(comp.text):
    #results="You Win!"
#elif int(player.text) == int(comp.text):
    #results="draw"
#elif int(player.text) < int(comp.text):
    #results="you loose!"
#record = {1: player, 2: comp, 3: results}

#print(comp)
#print(comp.text)
print(player)