#!/usr/bin/python3
"""
A Flask web application with several routes to handle different requests.
"""

from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" at the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" at the /hbnb route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays "C " followed by the value of the text variable.
    Replaces underscores with spaces.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Displays "Python " followed by the value of the text variable.
    Replaces underscores with spaces. Default value is "is cool".
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays "n is a number" only if n is an integer.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with "Number: n" inside an H1 tag.
    Only if n is an integer.
    """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page with "Number: n is odd|even" inside an H1 tag.
    Only if n is an integer.
    """
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=f"{n} is {parity}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
