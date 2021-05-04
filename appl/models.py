from django.db import models
from django.conf import settings
from django.utils import timezone

class Course(models.Model):
    title = models.CharField(max_length=200)
    lessons = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

#    def __str__(self):
#        return self.title
