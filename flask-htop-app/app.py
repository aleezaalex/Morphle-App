from flask import Flask
import os
import time
import subprocess
from pytz import timezone
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your Full Name
    name = "Aleeza Alex"

    # System Username
    username = os.getlogin()

    # Get Server Time in IST
    ist_time = datetime.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    # Run the `top` command and get its output
    top_output = subprocess.check_output(['top', '-bn1']).decode('utf-8')

    # Construct HTML page
    response = f"""
    <html>
    <head>
        <title>HTOP Output</title>
    </head>
    <body>
        <h1>HTOP Output</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
