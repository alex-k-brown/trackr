from django.db import models

# Create your models here.


class Goal(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(default="No description has been entered yet")
    categories = models.CharField(max_length=50, blank=True, null=True)
    timeframe = models.DateField(auto_now_add=False)
    status = models.BooleanField(default=False)
    child_goals = models.ManyToManyField('Goal', null=True, blank=True)
    
    def __unicode__(self):
        return self.name


