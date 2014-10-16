from django.db import models

# Create your models here.


class Goal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(default="No description has been entered yet")
    timeFrame = models.ForeignKey('TimeFrame')
    status = models.BooleanField(default=False)
    dueDate = models.DateField(default=False)
    
    def __unicode__(self):
        return self.name


class TimeFrame(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    days = models.IntegerField(default=False)

    def __unicode__(self):
        return "[{}] {}".format(self.id, self.name)


class ChildGoal(models.Model):
    step = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    goal = models.ForeignKey('Goal', related_name="children")
    timeFrame = models.ForeignKey('TimeFrame')

    def __unicode__(self):
        return self.step


class JournalEntry(models.Model):
    topic = models.CharField(max_length=100, blank=True, null=True)
    entry = models.TextField()

    def __unicode__(self):
        return self.topic



