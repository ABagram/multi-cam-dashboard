# app.py - Python Flask Server

from flask import Flask, render_template
import os
template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

CAMERA_FEEDS = {
    "ALPHA": "http://192.168.0.197:81/stream", 
    "BETA": "http://192.168.0.152:81/stream",
    "GAMMA": "http://192.168.0.124:81/stream"
}

@app.route('/')
def dashboard():
    # Passes the list of cameras (name and URL) to the HTML template
    return render_template('dashboard.html', feeds=CAMERA_FEEDS)

if __name__ == '__main__':
    # Runs the web server on your computer at port 8000
    app.run(host='0.0.0.0', port=8000, debug=True)