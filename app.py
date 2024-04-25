from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def display_madlibs_form():
    """ Display madlibs form """

    prompts = silly_story.prompts

    return render_template(
        "questions.jinja",
        story_prompts=prompts #NOTE: should this be spaced out? Keyword arguments
    )


@app.get("/results")
def display_madlibs_result():
    """ Creates and displays story rendered from the madlibs form inputs """

    story_text = silly_story.get_result_text(request.args)

    return render_template(
        "results.jinja",
        madlib_story=story_text
        )
