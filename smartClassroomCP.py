from models.database import db_session
from models.classes import *
from flask import Flask, url_for, render_template, session, escape, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/presence')
def liste_presence():
  classes = getClasseList()
  return render_template('absence.html', classes = classes)


def getClasseList():
  return Classe.query.all()

@app.template_filter('getStudentsList')
def getStudentsList(classe = None):
  if classe == None :
    return Etudiant.query.all()
  return Etudiant.query.filter(Etudiant.classe == classe.id)

if __name__ == '__main__':
  app.run(debug = True, host= '0.0.0.0')

