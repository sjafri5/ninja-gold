from flask import Flask, render_template, request, session, redirect, url_for
import random
import datetime
import os

def calculate_earnings(building):
    options = {
            'farm' : {'min': 10, 'max': 20},
            'cave' : {'min': 5, 'max': 10},
            'house' : {'min': 2, 'max': 5},
            'casino' : {'min': -50, 'max': 50},
            }

    value_change = random.randint(options[building]['min'], options[building]['max']);
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")

    return { 'value_change': value_change, 'timestamp':  timestamp }

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    gold_count = 0
    session['gold_count'] = gold_count
    session['activities'] = []
    return render_template('index.html', gold_count=gold_count)

@app.route('/process_money', methods=['GET', 'POST'])
def process_money():
    if request.method == 'POST':
        building = request.form['building']
        activities = session['activities']
        earnings = calculate_earnings(building)

        gold_count = session['gold_count'] + earnings['value_change']
        activities.append(earnings)

        session['activities'] = activities
        session['gold_count'] = gold_count 


        return render_template('index.html', gold_count=gold_count, activities=activities)


if __name__ == '__main__':
    app.run(debug=True)

