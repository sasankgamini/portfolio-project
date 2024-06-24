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
        {'lat': 40, 'lon': -100, 'popup': 'USA'},
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
        'job_title': "Site Reliability Engineer Fellow",
        'company': "Meta x MLH",
        'location': "Remote",
        'start_date': "June 2024",
        'end_date': "September 2024",
        },
        {
        'job_title': "AI/ML Intern",
        'company': "Enterprise Minds",
        'location': "San Ramon, CA",
        'start_date': "June 2023",
        'end_date': "September 2023",
        'description': "• Designed experiments using open-source LLMs to solve complex business problems, achieving a 30% increase in solution efficiency • Integrated open-source LLMs with Langchain, Pinecone, and Chainlit to create a Conversational AI-powered travel agent • Developed a personalized AI-powered Q&A application extracting information from PDF documents using Langchain, Streamlit, and ChromaDB/FAISS, supporting 500+ user queries per day."
        },
        {
        'job_title': "Software Engineer Intern",
        'company': "Mempage Technologies",
        'location': "Pleasanton, CA",
        'start_date': "May 2022",
        'end_date': "October 2022",
        'description': "• Supported the development of AI and machine learning solutions for ICE and VIA by managing data collection and preprocessing to model development and deployment, resulting in streamlined project workflows and improved team collaboration • Created an AI tool, analyzing face-to-face conversations via Haar cascades using the OpenCV module in Python  • Developed Keras-based machine learning models, integrated with OpenCV, to create a live prediction AI system for classifying car colors/makes"
        },
        {
        'job_title': "Web Developer",
        'company': "BayAreaRedwood",
        'location': "San Ramon, CA",
        'start_date': "January 2022",
        'end_date': "September 2022",
        'description': "• Developed web pages as a full-stack developer, with a heavy focus on front-end development using HTML, CSS, and JavaScript. • Built the company’s new e-commerce website, integrating it with their existing point of sales system to manage inventory and purchases, increasing website traffic by 200%  • Monitored website traffic, user behavior, and campaign performance using tools like Google Analytics, providing actionable insights to enhance marketing efforts."
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