from flask import Flask, render_template, request
import requests

app = Flask(__name__)

import os
API_KEY = "08a241a5f6ea741e3dbe4e0ad7ea8e8c"

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error = None   # ✅ added

    if request.method == 'POST':
        city = request.form['city']

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            weather_data = {
                "city": city,
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "condition": data["weather"][0]["main"]
            }
        else:
            error = "City not found!"   # ✅ added

    return render_template('index.html', weather=weather_data, error=error)  # ✅ updated

if __name__ == '__main__':
    app.run(debug=True)