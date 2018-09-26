from flask import Flask, render_template, request, session
import random
import os

def calculate_earnings(building):
    options = {
            'farm' : {'min': 10, 'max': 21},
            'cave' : {'min': 5, 'max': 11},
            'house' : {'min': 2, 'max': 6},
            'casino' : {'min': -50, 'max': 51},
            }

    value_change = random.randint(options[building]['min'], options[building]['max']);
    print('value_change')
    return value_change

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    gold_count = 0
    session['gold_count'] = gold_count
    return render_template('index.html', gold_count=gold_count)

@app.route('/process_money', methods=['GET', 'POST'])
def process_money():
    if request.method == 'POST':
        building = request.form['building']
        value_change = calculate_earnings(building)
        print(value_change)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

