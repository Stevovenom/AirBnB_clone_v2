#!/usr/bin/python3
# web_flask/7-states_list.py

"""
7-states_list.py

This module sets up a Flask web application that provides an endpoint to
display a list of states. The states are retrieved from a storage system
and presented on a web page.

Modules:
- Flask: Web framework used to create the application.
- render_template: Function to render HTML templates.
- storage: Custom storage object for database interactions.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close the SQLAlchemy session after each request.

    Args:
        exception (Exception): one that occurred during request processing.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display a list of states sorted by name.

    Returns:
        str: Rendered HTML template displaying the list of states.
    """
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
