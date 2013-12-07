from models.database import db_session
from models.classes import *
from flask import Flask, url_for, render_template, session, escape, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/c')
def listClass(class_id = None):
  classes = getClasseList()
  return render_template('classes.html', classes = classes)

@app.route('/c/<class_id>')
def listOfStudentsPerClass(class_id):
  classe = Classe.query.filter(Classe.id == class_id)
  if(classe.count() == 0):
    return render_template('students.html', classe = None)

  return render_template('students.html', classe = classe[0])

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

