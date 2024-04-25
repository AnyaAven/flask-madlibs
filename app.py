from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def display_madlibs_form():
    """ Display madlibs form, return template """

    prompts = silly_story.prompts

    return render_template(
        "questions.jinja",
        story_prompts=prompts
    )


@app.get("/results")
def display_madlibs_result():
    """ Displays the form results of madlibs into our story text"""

    answers = {}
    for prompt_key in silly_story.prompts:
        text = request.args.get(prompt_key)

        answers[prompt_key] = text

    print("ANSWERS", answers)
    story_text = silly_story.get_result_text(answers=answers)

    return render_template(
        "results.jinja",
        madlib_story=story_text
        )
