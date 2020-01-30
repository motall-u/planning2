from django.db import models

# Create your models here.
class Secretaire(models.Model):
	nom=models.CharField(max_length=50)
	prenom=models.CharField(max_length=50)
	mail=models.CharField(max_length=100)
	telephone=models.CharField(max_length=20)
	login=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	fk_id_class=models.ForeignKey('Classe',on_delete=models.CASCADE)

	def __str__(self):
		return self.nom


class Classe(models.Model):
	nom_class=models.CharField(max_length=50)
	login_class=models.CharField(max_length=50)
	password_class=models.CharField(max_length=50)
	fk_id_elev=models.ForeignKey('Eleve',on_delete=models.CASCADE)

	def __str__(self):
		return self.nom_class


class Eleve(models.Model):
	nom_eleve=models.CharField(max_length=50)
	prenom_eleve=models.CharField(max_length=50)
	grade_eleve=models.CharField(max_length=30)

	def __str__(self):
		return self.nom_eleve

class CahierTexte(models.Model):
	heure_cours=models.CharField(max_length=50)
	date=models.DateTimeField()
	contenu=models.TextField()

class Prof(models.Model):
	nom=models.CharField(max_length=50)
	prenom=models.CharField(max_length=50)
	mail=models.CharField(max_length=50)
	login=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	grade=models.CharField(max_length=30)
	fk_id_cours=models.ForeignKey('Cours',on_delete=models.CASCADE)
	fk_id_notification=models.ForeignKey('Notification',on_delete=models.CASCADE)


	def __str__(self):
		return self.nom


class Cours(models.Model):
	nom_cours=models.CharField(max_length=50)
	duree=models.CharField(max_length=50)
	date=models.DateTimeField()

	def __str__(self):
		return self.nom_cours

class Notification(models.Model):
	date=models.DateTimeField()
	contenu=models.TextField()


class Enseigner(models.Model):
	fk_id_class=models.ForeignKey('Classe', on_delete=models.CASCADE)
	fk_id_prof=models.ForeignKey('Prof', on_delete=models.CASCADE)


class PresAbs(models.Model):
	fk_id_eleve=models.ForeignKey('Eleve', on_delete=models.CASCADE)
	fk_id_cours=models.ForeignKey('Cours', on_delete=models.CASCADE)


