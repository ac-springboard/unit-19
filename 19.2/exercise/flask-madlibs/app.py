from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import stories

"""
This App implements a simplified version of the Madlibs game.
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'
debug = DebugToolbarExtension(app)

default_data = {
    "place": "Andromeda Galaxy",
    "adjective": "interesting",
    "noun": "Singularity",
    "verb": "open and close",
    "plural_noun": "Worm Holes"
}


@app.route('/')
def root_view():
    """Landpage view - shows the form with the default story"""
    # print(dumps(default_params))
    return render_template("root.html", par=default_data)


@app.route('/story', methods=["POST"])
def story_view():
    """
    Shows the rendered story using the parameters from the form in the landing page

    This function was developed in a way that makes it easier to implement the feature that allows the user to create hers or his own stories.
    """
    story_params = list(request.form.keys())
    story_struct = """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    story_templa = stories.Story(story_params, story_struct)
    story = story_templa.generate(request.form.to_dict())
    return render_template('story.html', story=story)
