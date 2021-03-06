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

    return { 'building': building, 'value_change': value_change, 'timestamp':  timestamp }

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if 'gold_count' in session:
        gold_count = session['gold_count']
    else: 
        gold_count = 0
        session['gold_count'] = gold_count

    if 'activities' in session:
        activities= session['activities']
    else: 
        activities= []
        session['activities'] = []

    return render_template('index.html', gold_count=gold_count, activities=activities)

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.method == 'POST':
        building = request.form['building']
        earnings = calculate_earnings(building)
        activities = session['activities']

        gold_count = session['gold_count'] + earnings['value_change']
        activities.append(earnings)

        session['activities'] = activities
        session['gold_count'] = gold_count 

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

