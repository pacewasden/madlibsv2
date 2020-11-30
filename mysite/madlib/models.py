from django.db import models

class Words(models.Model):
    def __str__(self):
        return self.verb

    verb = models.CharField(max_length=100, blank=True)
    sport = models.CharField(max_length=100, blank=True)
    person= models.CharField(max_length=100, blank=True)
    action = models.CharField(max_length=100, blank=True)
    adjective= models.CharField(max_length=100, blank=True)
    place=models.CharField(max_length=100, blank=True)
    school=models.CharField(max_length=100, blank=True)
    city=models.CharField(max_length=100, blank=True)
    athlete=models.CharField(max_length=100, blank=True)
    expression= models.CharField(max_length=100, blank=True)
