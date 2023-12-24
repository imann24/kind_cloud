from django.db import models

class Kind(models.Model):
    text = models.CharField(max_length=400)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.text} - {self.votes}"
