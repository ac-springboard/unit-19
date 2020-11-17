from flask import Flask
import stories

app = Flask(__name__)

ans = {
    'place': 'Andromeda',
    'adjective': 'interesting',
    'noun': 'singularity',
    'verb': 'open and close',
    'plural_noun': 'worm holes'
}
story = stories.story_structure.generate(ans)
print(story)
