from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

PAGE = """<html><body>
<p><a href="/">home</a> | <a href="/search">search</a></p>
{{ body|safe }}
</body></html>"""

@app.route("/")
def home():
    body = """
    <form method="POST" action="/login">
    name: <input name="name"><br>
    password: <input name="password" type="password"><br>
    <button type="submit">login</button>
    </form>
    """
    return render_template_string(PAGE, body=body)

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("name", "")
    password = request.form.get("password", "")

    conn = sqlite3.connect("students.db")
    rows = conn.execute(
        "SELECT id, name, email FROM students WHERE name = ? AND password = ?",
        (name, password),
    ).fetchall()
    conn.close()

    template = """
    {% if rows %}
    <p>login ok</p>
    <ul>
    {% for r in rows %}
    <li>{{ r[0] }} {{ r[1] }} {{ r[2] }}</li>
    {% endfor %}
    </ul>
    {% else %}
    <p>login failed</p>
    {% endif %}
    """
    body = render_template_string(template, rows=rows)
    return render_template_string(PAGE, body=body)

@app.route("/search")
def search():
    q = request.args.get("q", "")
    template = """
    <form method="GET" action="/search">
    <input name="q" value="{{ q }}">
    <button type="submit">search</button>
    </form>
    <p>you searched for: {{ q }}</p>
    """
    body = render_template_string(template, q=q)
    return render_template_string(PAGE, body=body)

if __name__ == "__main__":
    app.run(port=5001)
