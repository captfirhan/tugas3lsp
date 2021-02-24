from django.db import models

class PollModel(models.Model):
	question=models.TextField()
	option1=models.CharField(max_length=30)
	option2=models.CharField(max_length=30)
	option3=models.CharField(max_length=30)
	vote1=models.IntegerField(default=0)
	vote2=models.IntegerField(default=0)
	vote3=models.IntegerField(default=0)

	def __str__(self):
		return self.question
