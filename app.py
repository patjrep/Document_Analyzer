import Modules
import config
import processor
from flask import Flask, render_template, Markup, request

app = Flask(__name__)
p = processor
ret = p.mainProcessor()
keyword_var = p.keywordWeightGrabber()


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    print(keyword_var)
    # if request.method == 'POST':
    #     keyword_var = request.form.get('msg')
    return render_template("index.html", output=ret, keyword=keyword_var)
    # return msg


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', output=ret)


if __name__ == "__main__":
    app.run()
