from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('basic.html')
    
@app.route('/get')
def get():
    testapi = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=kraft%20mac%20cheese'
    return requests.get(testapi).content
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

