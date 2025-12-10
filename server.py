# TODO: Hide dropdown menu until Add criteria is clicked
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('screener'))

@app.route('/screener')
def screener():
    sectors = {'Equity Fields': {'exchange':['BUE', 'VIE', 'ASX', 'BRU',
                                             'SAO', 'CNQ', 'NEO', 'TOR',
                                             'VAN', 'EBS', 'SGO'] }}
    return render_template('screener.html')

if __name__ == '__main__':
    app.run(debug=True)