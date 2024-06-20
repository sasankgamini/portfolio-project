import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('index.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/work_experiences')
def work_experiences():
    return render_template('index.html', title="Work Experiences", url=os.getenv("URL"))

@app.route('/education')
def education():
    return render_template('index.html', title="Education", url=os.getenv("URL"))