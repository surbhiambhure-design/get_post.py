from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form (can send data via GET or POST)
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Form Example (GET & POST)</title>
</head>
<body style="font-family: Arial; margin: 40px;">
    <h2>User Form (GET & POST Request)</h2>

    <h3>POST Form</h3>
    <form method="POST" action="/submit_post">
        <label for="name">Name:</label>
        <input type="text" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" name="email" required><br><br>

        <button type="submit">Submit (POST)</button>
    </form>

    <hr>

    <h3>GET Form</h3>
    <form method="GET" action="/submit_get">
        <label for="city">City:</label>
        <input type="text" name="city" required><br><br>

        <label for="country">Country:</label>
        <input type="text" name="country" required><br><br>

        <button type="submit">Submit (GET)</button>
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    return html_form


# Handle POST request
@app.route("/submit_post", methods=["POST"])
def submit_post():
    name = request.form.get("name")
    email = request.form.get("email")

    return f"""
    <h2>✔ POST Form Submitted Successfully!</h2>
    <p><b>Name:</b> {name}</p>
    <p><b>Email:</b> {email}</p>
    <br>
    <a href="/">⬅ Back to Form</a>
    """


# Handle GET request
@app.route("/submit_get", methods=["GET"])
def submit_get():
    city = request.args.get("city")
    country = request.args.get("country")

    return f"""
    <h2>✔ GET Form Submitted Successfully!</h2>
    <p><b>City:</b> {city}</p>
    <p><b>Country:</b> {country}</p>
    <br>
    <a href="/">⬅ Back to Form</a>
    """


if __name__ == "__main__":
    app.run(debug=True,port=5002)