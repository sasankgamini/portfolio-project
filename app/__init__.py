import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

name = "Sasank Gamini"

@app.route('/')
def index():
    about_section = "Hi, my name is Sasank and this is my portfolio web app"
    markers = [
        {'lat': 34, 'lon': -118, 'popup': 'Los Angeles'},
         {'lat': 40, 'lon': -74, 'popup': 'New York'},
        {'lat': 17, 'lon': 78, 'popup': 'India'},
        {'lat': 25, 'lon': -78, 'popup': 'Bahamas'},
        {'lat': 19, 'lon': -155, 'popup': 'Hawaii'},
        {'lat': 22, 'lon': -109, 'popup': 'Cabo San Lucas'},
        {'lat': 21, 'lon': -86, 'popup': 'Cancun'},
        {'lat': 9, 'lon': -83, 'popup': 'Costa Rica'},
    ]
    return render_template('index.html', name=name, title="About", about=about_section, markers=markers, url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    hobby_list = ["Basketball", "Dancing", "Working Out", "Skiing", "Camping"]
    return render_template('hobbies.html', name=name, title="Hobbies", hobbies=hobby_list, url=os.getenv("URL"))

@app.route('/work_experiences')
def work_experiences():
    experiences = [
        {
        'job_title': "something",
        'company': "something",
        'location': "something",
        'start_date': "something",
        'end_date': "something",
        'description': "something"
        },
        {
        'job_title': "something",
        'company': "something",
        'location': "something",
        'start_date': "something",
        'end_date': "something",
        'description': "something"
        }
    ]
    return render_template('work_experiences.html', name=name, title="Work Experiences", work_experiences=experiences, url=os.getenv("URL"))

@app.route('/education')
def education():
    educations = [
        {
            'school': "UC Berkeley",
            'degree': "Bachelor's in Computer Science, Statistics",
            'start_date': "August 2024",
            'end_date': "May 2026",
            'description': "Pursuing Computer Science and Statistics at UC Berkeley"
        }
    ]
    return render_template('education.html', name=name, title="Education", educations = educations, url=os.getenv("URL"))