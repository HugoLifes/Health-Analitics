from django.db import models

# Create your models here.

class Activity(models.Model):
    ActivityId= models.AutoField(primary_key=True)
    ActivityDate = models.DateField()
    Steps = models.IntegerField()
    Distance= models.IntegerField()
    Run= models.IntegerField()
    Calories = models.IntegerField()

class Heartrate(models.Model):
    HeartId= models.AutoField(primary_key=True)
    HeartDate = models.DateField()
    Time = models.CharField(max_length=500)
    HeartRate = models.IntegerField()

class Sleep(models.Model):
    SleepId = models.AutoField(primary_key=True)
    SleepDate = models.DateField()
    DeepSleepTime = models.IntegerField()
    ShallowSleepTime = models.IntegerField()
    WakeTime = models.IntegerField()
    Start = models.DateField()
    End = models.DateField()
