from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello world"


@app.route("/about")
def adish_info():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
