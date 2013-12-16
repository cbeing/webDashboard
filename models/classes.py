from common import *
  
class Etudiant(Base):
  __tablename__ = 'etudiant'
  numInscription = Column('num_insc', String(15), primary_key = True)
  nCin = Column('cin', String(8))
  nom = Column(String(90))
  prenom = Column(String(90))
  adresse = Column(String(90))
  email = Column(String(90), unique = True)
  sexe = Column(String(90))
  date_naissance = Column('dat_nai', Date)
  classe = Column('classe_id', String(15), ForeignKey('classe.id'))

  def __init__(self, numInscription, nCin, nom, prenom, adresse, sexe, date_naissance):
    self.numInscription = numInscription
    self.nCin = nCin
    self.nom = nom
    self.prenom = prenom
    self.adresse = adresse
    self.sexe = sexe
    self.date_naissance = date_naissance




class Enseignant(Base):
  __tablename__ = 'enseignant'
  nCin = Column('cin', String(8))
  nom = Column(String(90))
  prenom = Column(String(90))
  adresse = Column(String(90))
  email = Column(String(90), unique = True)
  sexe = Column(String(90))
  date_naissance = Column('dat_nai', Date)
  matricule = Column(String(10), primary_key = True)

  def __init__(self, matricule, nCin, nom, prenom, adresse, sexe, date_naissance):
    self.matricule = matricule
    self.nCin = nCin
    self.nom = nom
    self.prenom = prenom
    self.adresse = adresse
    self.sexe = sexe
    self.date_naissance = date_naissance

   

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
  matiere = Column('matiere_code', String(20), ForeignKey('matiere.code'))
  classe = Column('classe_id', String(10), ForeignKey('classe.id'))
  presenceList = relationship('Presence', backref='seance', lazy='dynamic')
  date = Column('Date_Se', Date)
  enseignant = Column('enseignant_matricule', String(255), ForeignKey('enseignant.matricule'), nullable = False)

  def __init__(self, matiere, classe):
    self.matiere = matiere
    self.classe = classe

class Presence(Base):
  __tablename__ = 'presence'
  id = Column(Integer, primary_key = True)
  etudiant = Column('etudiant_num_insc', Integer, ForeignKey('etudiant.num_insc'), nullable = False)
  heure_entree = Column('h_entree', Time)
  seance_id = Column(Integer, ForeignKey('seance.id'))
  etat = Column(Boolean)

  def __init__(self, seance, etudiant, heure_entree = None):
    self.seance = seance
    self.etudiant = etudiant
    self.heure_entree = heure_entree
    self.etat = False


