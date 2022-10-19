from flask import Flask, redirect, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'Your api key'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
        response = requests.get(request_url)
        data = response.json()
        info = data
        return render_template('display.html', info = info)
    return render_template('home.html')

@app.route('/back')
def back():
    return redirect('/')

if __name__ == "__main__": 
    app.run(debug=True)
