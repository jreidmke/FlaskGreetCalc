from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <a href='/welcome'>Welcome</a>
        </body>
    </html>
    """
    return html

@app.route('/welcome')
def welcome():
    return "WELCOME"

@app.route('/welcome/<location>')
def add_local(location):
    return f"WELCOME {location}"