from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/header-footer")
def header_footer_page():
    return render_template("header_footer.html")
