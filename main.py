from flask import Flask, render_template, request, redirect
from werkzeug.utils import html
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
    
# @app.route('/index')
# def index():
#     return render_template("index.html")

@app.route('/infertility')
def infertility():
    return render_template("infertility.html")

@app.route('/married')
def married():
    return render_template("married.html")

@app.route('/menopause')
def menopause():
    return render_template("menopause.html")

@app.route('/new_moms')
def new_moms():
    return render_template("new-moms.html")

@app.route('/portfolio-details')
def portfolio_details():
    return render_template("portfolio-details.html")

@app.route('/pregnant')
def pregnant():
    return render_template("pregnant.html")

@app.route('/teenage')
def teenage():
    return render_template("teenage.html")

@app.route('/pregtracker')
def pregtracker():
    return render_template("pregtracker.html")

if __name__ == "__main__":
    app.run()