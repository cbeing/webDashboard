from models.database import db_session
from models.classes import *
from flask import Flask, url_for, render_template, session, escape, request

app = Flask(__name__)


@app.route('/')
def index():
  return "Hello Smart Classroom !"



if __name__ == '__main__':
  app.run(debug = True, host= '0.0.0.0')

