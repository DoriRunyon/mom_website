
from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


@app.route('/')
def home():
    """Home page."""

    return render_template("brain_home.html")

@app.route('/about')
def about():
    """Home page."""

    return render_template("about.html")

@app.route('/writers_studio')
def writer_studio():
    """Home page."""

    return render_template("writers_studio.html")

@app.route('/stories')
def stories():
    """Home page."""

    return render_template("stories.html")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    # app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
