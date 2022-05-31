import flask
from wtforms import StringField
import re
import random
from copy import copy

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)
separator = '\n-weird-\n'

def encode(text):
    tokenize_re = re.compile(r'(\w+)', re.U)
    weird_text = text
    words = tokenize_re.findall(text)
    original_words = []
    new_words = []
    for word in words:
        if len(word) > 3:
            if word[1:-1] != word[1] * len(word[1:-1]):
                tmp = word[1:-1]
                while tmp == word[1:-1]:
                    list_tmp = list(tmp)
                    random.shuffle(list_tmp)
                    tmp = ''.join(list_tmp)
                new_word = word[0] + tmp + word[-1]
                new_words.append(new_word)
                weird_text = weird_text.replace(word, new_word, 1)
                original_words.append(word)
    weird_text = separator + weird_text + separator + ' '.join(sorted(original_words, key=str.lower))
    return weird_text


def decode(text):

    return text


@app.get("/")
def home():
    # text = StringField('text')
    return flask.render_template('home_layout.html')


@app.route("/v1/encode", methods=['POST'])
def encode_endpoint():
    text = flask.request.form['text']
    return encode(text)


@app.route("/v1/decode", methods=['POST'])
def decode_endpoint():
    text = flask.request.form['text']
    return decode(text)


if __name__ == "__main__":
    sample_text = 'This is a long looong test sentence,\nwith some big (biiiiig) words!'
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # app.run(host="localhost", port=8080, debug=True)
