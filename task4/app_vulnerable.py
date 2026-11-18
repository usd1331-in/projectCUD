from flask import Flask, request
import sqlite3

app = Flask(__name__)

PAGE = """<html><body>
<p><a href="/">home</a> | <a href="/search">search</a></p>
{body}
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
    return PAGE.format(body=body)

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("name", "")
    password = request.form.get("password", "")

    query = "SELECT id, name, email FROM students WHERE name = '" + name + "' AND password = '" + password + "'"

    conn = sqlite3.connect("students.db")
    rows = conn.execute(query).fetchall()
    conn.close()

    body = "<p>query: " + query + "</p>"
    if rows:
        body += "<p>login ok</p><ul>"
        for r in rows:
            body += "<li>" + str(r) + "</li>"
        body += "</ul>"
    else:
        body += "<p>login failed</p>"

    return PAGE.format(body=body)

@app.route("/search")
def search():
    q = request.args.get("q", "")
    body = """
    <form method="GET" action="/search">
    <input name="q" value="{q}">
    <button type="submit">search</button>
    </form>
    <p>you searched for: {q}</p>
    """.format(q=q)
    return PAGE.format(body=body)

if __name__ == "__main__":
    app.run(port=5000)
