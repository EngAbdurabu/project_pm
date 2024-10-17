from django.db import models
# to add users automatically
from django.conf.global_settings import AUTH_USER_MODEL


# Create your models here.
class ProjectStatus(models.IntegerChoices):
	# IntegerChoices use to make choices
	PENDING = 1, 'Pending'
	COMPLETED = 2, 'Completed'
	POSTPONED = 3, 'Postponed'
	CANCELED = 4, 'Canceled'
	# first value put in database, second value appear to user


class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	# connect between Project status and project
	status = models.IntegerField(
		choices=ProjectStatus.choices,
		default=ProjectStatus.PENDING
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	users = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Task(models.Model):
	description = models.TextField()
	is_completed = models.BooleanField(default=False)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)

	def __str__(self):
		return self.description
