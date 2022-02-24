from flask import Flask
from datetime import datetime as dt

app = Flask(__name__)


@app.get("/")
def home():
    return {"data": "Hello Flask!"}, 200


@app.get("/current_datetime")
def current_datetime():

    message = "Bom dia!"
    current_time = dt.now()

    if current_time.hour > 12:
        message = "Boa tarde!"

    elif current_time.hour > 18:
        message = "Boa noite!"

    show_date = current_time.strftime("%d/%m/%Y %I:%M:%S %p")

    return {'current_datetime': show_date, 'message': message}, 200
