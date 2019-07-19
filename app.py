from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/mobile")
def mobile():
    return "Due to the dynamic nature of its website, Analytec does not currently support mobile viewing. Please use a Mac, PC, or laptop to view our site. Any suggestions and/or questions can be e-mailed to analytecofficial@gmail.com."
