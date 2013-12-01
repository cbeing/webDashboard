from database import db_session
from classes import *

def addStudent(numInscription, nCin, nom, prenom, addresse, email, sexe, date_naissance, classe):
  etudiant = Etudiant(numInscription)
  etudiant.nCin = nCin
  etudiant.nom = nom
  etudiant.prenom = prenom
  etudiant.addresse = addresse
  etudiant.email = email
  etudiant.sexe = sexe
  etudiant.date_naissance = date_naissance
  etudiant.classe = classe.id
  db_session.add(etudiant)
  db_session.commit()

def addClasse(classeId):
  classe = Classe(classeId)
  db_session.add(classe)
  db_session.commit()

