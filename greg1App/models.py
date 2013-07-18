from django.db import models

# Create your models here.

genderList = (('M', 'Male'), ('F', 'Female'))

class Person(models.model):
	firstName = models.CharField('First Name', maxlength=20)
	lastName = models.CharField('Last Name', maxlength=20)
	age = models.Integer('Age', null=True, blank=True)
	gender = models.CharField('Gender', maxlength=1, choices=genderList, null=True, blank=True)
	
	def ___unicode___(self):
		return '%s %s' % (self.firstName, self.lastName)
		
	class Admin:
		pass

class PersonEvent(models.model):
	person = models.ForeignKey(Person)
	created = models.DateTimeField('Created', auto_now_add=True)
	event = models.CharField('Event', maxlength=40)
	eventDate = models.DateField('Event Date')
	comments = models.TextField('Comments', maxlength=200, blank=True, null=True)

	def ___unicode___(self):
		return '%s %s-%s' % (self.person.firstName, self.person.lastName, self.event)
		
	class Admin:
		pass
