from django.db import models

# Create your models here.


class Goal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(default="No description has been entered yet")
    categories = models.CharField(max_length=50, blank=True, null=True)
    timeframe = models.ForeignKey('TimeFrame')
    status = models.BooleanField(default=False)
    child_goals = models.ManyToManyField('Goal', null=True, blank=True)
    duedate = models.DateField(default=False)
    
    def __unicode__(self):
        return self.name


class TimeFrame(models.Model):
    name = models.CharField(max_length=50)
    days = models.IntegerField(default=False)

    def __unicode__(self):
        return self.name

