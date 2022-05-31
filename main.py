import flask
import re
import random

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
    try:
        _, weird_text, original_words = text.split(separator)
    except ValueError:
        raise ValueError('Error: Text is not valid')
    new_text = weird_text
    original_words = original_words.split(' ')
    tokenize_re = re.compile(r'(\w+)', re.U)
    words = tokenize_re.findall(text)
    for original_word in original_words:
        for word in words:
            if sorted(original_word) == sorted(word) and len(original_word) == len(word):
                new_text = new_text.replace(word, original_word, 1)
                break
    return new_text


@app.get("/")
def home():
    return flask.render_template('home_layout.html')


@app.route("/v1/encode", methods=['POST'])
def encode_endpoint():
    text = flask.request.form['text']
    encoded_text = encode(text)
    encoded_text = encoded_text.replace("\n", "\\n")
    return flask.render_template('encode_layout.html', weird_text=encoded_text)


@app.route("/v1/decode", methods=['POST'])
def decode_endpoint():
    text = flask.request.form['weird_text']
    text = text.replace("\\n", "\n")
    decoded_text = decode(text)
    return flask.render_template('decode_layout.html', decoded_text=decoded_text)


if __name__ == "__main__":
    sample_text = 'This is a long looong test sentence,\n with some big (biiiiig) words!'
    encoded_text = encode(sample_text)
    decoded_text = decode(encoded_text)
    print(encoded_text)
    print(decoded_text)
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # app.run(host="localhost", port=8080, debug=True)
