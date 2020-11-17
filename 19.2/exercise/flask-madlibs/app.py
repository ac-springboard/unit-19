from json import dumps
from flask import Flask, render_template
import stories

app = Flask(__name__)

default_params = {
    "place": "Andromeda",
    "adjective": "interesting",
    "noun": "singularity",
    "verb": "open and close",
    "plural_noun": "worm holes"
}


# default_story = stories.story_structure.generate(default_params)

@app.route('/')
def r_root():
    print(dumps(default_params))
    return render_template("root.html", par=default_params)
