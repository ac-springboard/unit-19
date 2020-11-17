from json import dumps
from flask import Flask, render_template, request
import stories

app = Flask(__name__)

default_data = {
    "place": "Andromeda",
    "adjective": "interesting",
    "noun": "singularity",
    "verb": "open and close",
    "plural_noun": "worm holes"
}


@app.route('/')
def root_view():
    # print(dumps(default_params))
    return render_template("root.html", par=default_data)


@app.route('/story')
def story_view():
    story_params = list(request.args.keys())
    story_struct = """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    story_templa = stories.Story(story_params, story_struct)
    story = story_templa.generate(request.args.to_dict())
    return story
