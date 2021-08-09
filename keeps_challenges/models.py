#Arquivo responsável pela definição dos modelos presentes nesta aplicação.
#Course, Student, Enrollment  
from django.db import models
from datetime import datetime

#Definição do modelo 'Aluno' e seus respectivos atributos.
class Student(models.Model):
	name = models.CharField(max_length=50)
	nickname = models.CharField(max_length=12)
	phone = models.CharField(max_length=30)
	date_created = models.DateTimeField(default= datetime.now, blank=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

#Definição do modelo 'Course' e seus respectivos atributos.
class Course(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=130)
	duration = models.IntegerField(default=1)
	date_created = models.DateTimeField(default= datetime.now, blank=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

#Definição do modelo 'Enrollment' e seus respectivos atributos.
class Enrollment(models.Model):
	student = models.ForeignKey("Student", on_delete=models.SET_NULL, blank=True, null=True)
	course = models.ForeignKey("Course", on_delete=models.SET_NULL, blank=True, null=True)
	date_enroll = models.DateTimeField(default= datetime.now, blank=True)
	#date_close = models.DateTimeField(auto_now=True)
	score = models.IntegerField(default=0)
	status = models.ForeignKey("Status", on_delete=models.SET_NULL, blank=True, null=True) #Testar on_delete=models.PROTECT

#Definição do modelo 'Status' e seus respectivos atributos. Este complementa o modelo 'Enrollment'
class Status(models.Model):
	status = models.CharField(max_length=9)

	def __str__(self):
		return self.status