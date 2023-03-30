from pathlib import Path

from flask import Flask, render_template
from pygments import highlight as pygments_highlight
from pygments.lexers import CssLexer, HtmlLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/header-footer")
def header_footer_page():
    css_text = Path("static/header_footer.css").read_text()
    highlighted_css = pygments_highlight(css_text, CssLexer(), HtmlFormatter())

    html_text = Path("templates/header_footer.html").read_text()
    highlighted_html = pygments_highlight(html_text, HtmlLexer(), HtmlFormatter())

    return render_template(
        "header_footer.html",
        highlighted_css=highlighted_css,
        highlighted_html=highlighted_html,
    )
