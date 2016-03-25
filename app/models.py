from django.db import models
from datetime import datetime
import random

# Create your models here.
class Building(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200, default="")
	picture_url = models.CharField(max_length=200, default="")

	def __str__(self):
		return self.name

	def get_url(self):
		url_with_spaces = str(self.name)
		url_without_spaces = url_with_spaces.replace (" ", "_")
		url_without_periods = url_without_spaces.replace (".", "_")
		return url_without_periods.lower()

	def save(self, *args, **kwargs):

		if not self.url:
			self.url = self.get_url()

		#for testing
			self.picture_url = "/static/app/img/i-form-password-ios.svg"

		super(Building, self).save(*args, **kwargs)

	#for testing purposes
	def fake_bathrooms(self):
		i = 0
		while i < 5:
			bath_name = str(self.name) + " " + str(i)
			rating_random = random.uniform(0,5)
			print bath_name, " and rating_random: ", rating_random
			temp = ''
			temp = Bathroom(in_building = self, floor = i + 1, rating = rating_random, name = bath_name)
			temp.save()
			i +=1

class Bathroom(models.Model):
	in_building = models.ForeignKey(Building, on_delete=models.CASCADE)
	floor = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200, default="")
	picture_url = models.CharField(max_length=200, default="")
	rating = models.FloatField(default=0)

	def __str__(self):
		return str(self.in_building) + " " + str(self.floor)

	def get_url(self):
		url_with_spaces = str(self.name)
		url_without_spaces = url_with_spaces.replace (" ", "_")
		url_without_periods = url_without_spaces.replace (".", "_")
		return url_without_periods.lower()

	def fake_comments(self):
		i = 0
		while i < 15:
			comment = "This is simple card with plain text. But card could contain its own header, footer, list view, image, and any elements inside."
			votes_random = random.randint(-20, 20)
			temp = ''
			temp = Comment(for_bathroom = self, comment_text = comment, votes = votes_random)
			temp.save()
			i +=1

	def save(self, *args, **kwargs):
		if not self.url:
			self.url = self.get_url()
			#for testing
			self.picture_url = "/static/app/img/i-form-settings-ios.svg"
		super(Bathroom, self).save(*args, **kwargs)

class Comment(models.Model):
	for_bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return str(self.for_bathroom) + " " + str(self.comment_text)
