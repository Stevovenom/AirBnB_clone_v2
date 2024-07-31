#!/usr/bin/python3
"""
Starts a Flask web application that displays a list of states.

The script sets a Flask web application with a single route, `/states_list`,
that displays a list of states retrieved from the `storage` module. The states
are sorted by name before being passed to the template for rendering.

Modules:
- flask: Provides necessities for creating application and rendering templates
- models: Imports the necessary modules from the `models` package.
- models.storage: Handles data storage and retrieval operations.

Functions:
- states_list: Handles the `/states_list` route to fetch and  display states
- teardown_db: Closes SQLAlchemy session after request for resouce mngt

Routes:
- `/states_list`: Displays an HTML page listing all State in alphabetical order

Application Configuration:
- Host: `0.0.0.0`
- Port: `5000`
- `strict_slashes=False`: Ensures the route does not require a trailing slash.

How to Run:
- Run the script using Python 3 with the command: `python3 script_name.py`
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays a list of states.

    Fetches all states from the storage, sorts them by name, and passes them
    to the `7-states_list.html` for rendering. The states are displayed
    in an HTML format within an unordered list.

    Returns:
        str: The rendered HTML template showing the list of states.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the SQLAlchemy session after each request.

    This function is called after each request to ensure that the database
    session is properly closed, freeing up resources and avoiding potential
    leaks.

    Args:
        exception (Exception): The exception raised during the request, if any.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
