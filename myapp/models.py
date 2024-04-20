from django.db import models
from django.db.models.fields import CharField, TextField, URLField
from django.db.models.fields.files import ImageField


# Create your models here.
class Tren(models.Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to="myapp/images/")
    url = URLField()

    def __str__(self):
        return self.title
