from flask import Flask, request, redirect, Response, jsonify
import requests
import random

colour=requests.get("http://192.168.1.13:5001/colour")
p2=colour.text
result = colour.text
print(result)
print(colour)
print(p2)