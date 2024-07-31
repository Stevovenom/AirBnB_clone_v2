#!/usr/bin/python3
"""
7. Start Flask service to display a list of states.

This script sets up a Flask web application with a single route, `/states_list`
that displays a list of states retrieved from the `storage` module. The states
are sorted by name before being passed to the template for rendering.

Modules:
- flask: Used for creating the web application and rendering templates.
- logging: Provides logging functionality for debugging.
- models.storage: Used for interacting with the data storage.

Functions:
- teardown_db: Closes the SQLAlchemy session after each request.
- states_list: Fetches, sorts, and displays a list of states.
"""

import logging
from flask import Flask, render_template
from models import storage

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Create a Flask application instance
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close the SQLAlchemy session after each request.

    This function is called after each request to ensure that the database
    session is properly closed, freeing up resources and avoiding potential
    leaks.

    Args:
        exception (Exception): The exception raised during the request, if any.
    """
    storage.close()


@app.route('/states_list')
def states_list():
    """
    Display a list of states.

    Fetches all states from the storage, sorts them by name, and passes
    them to the template for rendering. The template displays the list
    of states in an HTML format.

    Returns:
        str: The rendered HTML template showing the list of states.
    """
    states = storage.all("State")  # Use storage to fetch data
    print(states)  # Debug print to verify the data
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
