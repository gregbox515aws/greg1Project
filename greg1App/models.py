from django.db import models

# Create your models here.

genderList = (('M', 'Male'), ('F', 'Female'))

class Person(models.Model):
	firstName = models.CharField('First Name', max_length=20)
	lastName = models.CharField('Last Name', max_length=20)
	age = models.IntegerField('Age', null=True, blank=True)
	gender = models.CharField('Gender', max_length=1, choices=genderList, null=True, blank=True)
	
	def __unicode__(self):
		return '%s %s' % (self.firstName, self.lastName)

	class Admin:
		pass
		
class PersonEvent(models.Model):
	person = models.ForeignKey(Person)
	created = models.DateTimeField('Created', auto_now_add=True)
	event = models.CharField('Event', max_length=40)
	eventDate = models.DateField('Event Date')
	comments = models.TextField('Comments', max_length=200, blank=True, null=True)

	def __unicode__(self):
		return '%s %s-%s' % (self.person.firstName, self.person.lastName, self.event)
		
	class Admin:
		pass
		
