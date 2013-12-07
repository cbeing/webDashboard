from models.database import db_session
from models.classes import *
from flask import Flask, url_for, render_template, session, escape, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/c')
def listClass():
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

@app.route('/m')
def listMaterials():
  materials = getMaterialsList()
  return render_template('materials.html', materials = materials)

@app.route('/m/add', methods=['GET', 'POST'])
def addMaterial():
  if 'label' in request.form and 'code' in request.form:
    m = Matiere(request.form['code'], request.form['label'])
    db_session.add(m)
    db_session.commit()

  materials = getMaterialsList()
  return render_template('materials.html', materials = materials)

@app.route('/m/update', methods=['GET', 'POST'])
def updateMaterial():
  material_id = request.form['code']
  m = Matiere.query.get(material_id)
  m.label = request.form['label']
  db_session.add(m)
  db_session.commit()

  materials = getMaterialsList()

  return render_template('materials.html', materials = materials)

def getClasseList():
  return Classe.query.all()

@app.template_filter('getStudentsList')
def getStudentsList(classe = None):
  if classe == None :
    return Etudiant.query.all()
  return Etudiant.query.filter(Etudiant.classe == classe.id)

def getMaterialsList():
  return Matiere.query.all()

if __name__ == '__main__':
  app.run(debug = True, host= '0.0.0.0')

