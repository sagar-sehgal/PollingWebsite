from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	quest=models.CharField(max_length=500)
	date=models.DateTimeField('date asked')
	a_count=models.IntegerField(default=0)
	def __str__(self):
		return self.quest+"__"+str(self.date)
class Choice(models.Model):
	quest=models.ForeignKey(Question,on_delete=models.CASCADE)
	ans=models.CharField(max_length=1000)
	upvotes=models.IntegerField(default=0)
	downvotes=models.IntegerField(default=0)
	date=models.DateTimeField('date answered')
	def __str__(self):
		return self.quest.quest+"__"+self.ans+"__"+str(self.date)