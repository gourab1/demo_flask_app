from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    name = 'Bani'
    return render_template('home.html', name=name)
    
@app.route('/form_donation')
def form_donation():
    name = 'Bani'
    return render_template('form_donation.html', name=name)
    
@app.route('/thankyou')
def thankyou():
    name = 'Bani'
    donation_item = request.args.get('donation_item')
    return render_template('thankyou.html', name=name, donation_item=donation_item)
    
@app.route('/give')
def give():
    name = 'Bani'
    donations = ['sofa', 'table lamp']
    return render_template('give.html', name=name, donations=donations)
    
@app.route('/get')
def get():
    testapi = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=kraft%20mac%20cheese'
    return request.get(testapi).content
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

