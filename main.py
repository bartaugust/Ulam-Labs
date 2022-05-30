import flask
from wtforms import StringField

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)

def encode(text):
    weird_text = text
    return weird_text

@app.get("/")
def home():
    # text = StringField('text')
    return flask.render_template('home_layout.html')


@app.route("/encode", methods=['POST'])
def encode_endpoint():
    text = flask.request.form['text']
    return encode(text)


if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
