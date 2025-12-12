# TODO: Hide dropdown menu until Add criteria is clicked
from flask import Flask, render_template, redirect, url_for
from src.screener_params import screener_dictionary
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('screener'))
@app.route('/screener')
def screener():
    screener_fields = screener_dictionary
    return render_template('screener.html', screener_field=screener_fields)

if __name__ == '__main__':
    app.run(debug=True)