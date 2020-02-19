from django.db import models

# Create your models here.


class Document(models.Model):
    document_title = models.CharField(max_length=200)
    pub_date       = models.DateTimeField('Data publikacji')
    text           = models.TextField(max_length=2000)
    image_name     = models.CharField(max_length=100)


class Comments(models.Model):
    document    = models.ForeignKey(Document, on_delete=models.CASCADE)
    text        = models.CharField(max_length=200)
