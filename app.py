from flask import Flask, json

# app setup
app = Flask(__name__)
@app.route("/odds",methods=["GET"])
def get_odds():
    odd_numbers = [1,3,5,7,9]
    return json.dumps(odd_numbers)