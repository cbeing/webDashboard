from common import *

class Personne(Base):
  __tablename__ = 'personne'
  nCin = Column(Integer, primary_key = True)
  nom = Column(String(90))
  prenom = Column(String(90))
  adresse = Column(String(90))
  email = Column(String(90), unique = True)
  sexe = Column(String(90))
  date_naissance = Column(Date)
  type = Column(String(20))

  __mapper_args__ = { 'polymorphic_identity':'personne',
                      'polymorphic_on':type}

  def __init__(self, nCin, nom, prenom, adresse, email, sexe, date):
    self.nCin = nCin
    self.nom = nom
    self.prenom = prenom
    self.adresse = adresse
    self.sexe = sexe
    self.date_naissance = date_naissance

  def __repr__(self):
    return '<Personne %r %r>' %(self.nom, self.prenom)


class Etudiant(Personne):
  __tablename__ = 'etudiant'
  id = Column(Integer, ForeignKey('personne.nCin'), unique = True)
  numInscription = Column(String(15), primary_key = True)
  classe = Column(String(15), ForeignKey('classe.id'))

  __mapper_args__ = {'polymorphic_identity':'etudiant'}

  def __init__(self, numInscription):
    self.numInscription = numInscription



class Enseignant(Personne):
  __tablename__ = 'enseignant'
  id = Column(Integer, ForeignKey('personne.nCin'))
  matricule = Column(String(10), primary_key = True)
  grade = Column(Integer, ForeignKey('grade.id'), nullable = False)

  __mapper_args__ = {'polymorphic_identity':'enseignant'}

  def __init__(self, grade):
    self.grade = grade
    

class Grade(Base):
  __tablename__ = 'grade'
  id = Column(Integer, primary_key = True)
  nom = Column(String(20), nullable = False, unique = True)

  def __init__(self, nom):
    self.nom = nom

class Classe(Base):
  __tablename__ = 'classe'
  id = Column(String(10), primary_key = True)

  def __init__(self, id, nombreEtudiant = None):
    self.id = id
    self.nombreEtudiant = nombreEtudiant

class Matiere(Base):
  __tablename__ = 'matiere'
  code = Column(String(20), primary_key = True)
  label = Column(String(20), nullable = False)

  def __init__(self, code, label):
    self.code = code
    self.label = label


class Seance(Base):
  __tablename__ = 'seance'
  id = Column(Integer, primary_key = True)
  matiere = Column(String(20), ForeignKey('matiere.code'))
  classe = Column(String(10), ForeignKey('classe.id'))

  def __init__(self, matiere, classe):
    self.matiere = matiere
    self.classe = classe

class Presence(Base):
  __tablename__ = 'presence'
  id = Column(Integer, primary_key = True)
  seance = Column(Integer, ForeignKey('seance.id'), nullable = False)
  etudiant = Column(Integer, ForeignKey('etudiant.id'), nullable = False)
  enseignant = Column(Integer, ForeignKey('enseignant.id'), nullable = False)
  heure_entree = Column(Date)

  def __init__(self, seance, etudiant, enseignant, heure_entree):
    self.seance = seance
    self.etudiant = etudiant
    self.enseignant = enseignant
    self.heure_entree = heure_entree


