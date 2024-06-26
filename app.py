from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/stories")
def display_story_options():
    """ Display all optional stories """

    return render_template(
        "stories.jinja",
        madlib_story_names=stories.keys()
    )


@app.get("/stories/form")
def display_madlibs_form():
    """ Display madlibs form """

    story = request.args.get("storylist")
    prompts = stories[story].prompts

    return render_template(
        "questions.jinja",
        story_prompts=prompts,  # NOTE: should this be spaced out? Yes, Keyword arguments in Py
        story_name=story
    )


@app.post("/results")
def display_madlibs_result():
    """ Creates and displays story rendered from the madlibs form inputs """

    story = request.form.get("storyname")

    story_text = stories[story].get_result_text(request.form)

    return render_template(
        "results.jinja",
        madlib_story=story_text,
        story_name=story
    )
