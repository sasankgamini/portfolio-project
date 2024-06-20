import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

name = "Sasank Gamini"

@app.route('/')
def index():
    return render_template('index.html', name=name, title="About", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', name=name, title="Hobbies", url=os.getenv("URL"))

@app.route('/work_experiences')
def work_experiences():
    return render_template('work_experiences.html', name=name, title="Work Experiences", url=os.getenv("URL"))

@app.route('/education')
def education():
    return render_template('education.html', name=name, title="Education", url=os.getenv("URL"))