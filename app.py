from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def display_madlibs_form():
    """ Display madlibs form return template """

    prompts = silly_story.prompts

    return render_template("questions.jinja")
