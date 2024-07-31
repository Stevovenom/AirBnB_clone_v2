#!/usr/bin/python3
""" 7. Start Flask service that does something. """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """Close the SQLAlchemy session."""
    storage.close()


@app.route('/states_list')
def states_list():
    """Display a list of states."""
    states = storage.all("State")  # Use storage to fetch data
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
