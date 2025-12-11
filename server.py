# TODO: Hide dropdown menu until Add criteria is clicked
from flask import Flask, render_template, redirect, url_for
from scraping import equity_field_params
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('screener'))
@app.route('/screener')
def screener():
    regions = equity_field_params.get_regions()
    print(regions)
    exchanges = equity_field_params.get_exchanges()
    sectors, industries = equity_field_params.get_industries()
    peer_groups = equity_field_params.get_peer_groups()

    return render_template('screener.html')

if __name__ == '__main__':
    app.run(debug=True)