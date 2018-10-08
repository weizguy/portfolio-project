from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    post = models.TextField()
    image = models.ImageField(upload_to='images/')
