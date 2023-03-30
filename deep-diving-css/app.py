from pathlib import Path

from flask import Flask, abort, render_template
from pygments import highlight as pygments_highlight
from pygments.lexers import CssLexer, HtmlLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/examples/<title>")
def example_page(title):
    title = _url_pattern_to_filename(title)

    css_path = Path(f"static/{title}.css")
    template_path = Path(f"templates/examples/{title}.html")
    if not css_path.exists() or not template_path.exists():
        abort(404)

    css_text = css_path.read_text()
    highlighted_css = pygments_highlight(css_text, CssLexer(), HtmlFormatter())

    html_text = template_path.read_text()
    highlighted_html = pygments_highlight(html_text, HtmlLexer(), HtmlFormatter())

    return render_template(
        f"examples/{title}.html",
        highlighted_css=highlighted_css,
        highlighted_html=highlighted_html,
    )


def _url_pattern_to_filename(s):
    return s.replace("-", "_")
