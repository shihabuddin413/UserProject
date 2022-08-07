from django.db import models
from django.utils.timezone import now

# Create your models here.
class Advertisments(models.Model):
    name = models.CharField(max_length=200, help_text="Type Advertisment Title Here")
    content = models.TextField(help_text="Type Or Paste Your Content Here")
    publish_date = models.DateField(default=now, help_text="The day you want to scheduled this advertisment")
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name







 
    