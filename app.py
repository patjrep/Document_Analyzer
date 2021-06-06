import Modules
import config
import processor
from flask import Flask, render_template

app = Flask(__name__)
p = processor
ret = p.mainProcessor()


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', output=ret)


if __name__ == "__main__":
    app.run()
