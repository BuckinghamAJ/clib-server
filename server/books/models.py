from django.db import models
from django.contrib.auth.models import User # change when custom User is complete
from users.models import ClibUser

# Setting Media Type Variable for multiple choice
MEDIA_TYPE = [
    ('audio', 'Audio'),
    ('text', 'Text'),
]

# Create your models here.
class Collection(models.Model):
    title: models.CharField(max_length=200)
    type: models.CharField(max_length=5, choices=MEDIA_TYPE)
    count: models.IntegerField()
    next_avaliable: models.DateTimeField()

class Book(models.Model):
    media: models.FileField()
    avaliable: models.BooleanField()
    #rented_by: models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    rented_by: models.OneToOneField(ClibUser, on_delete=models.CASCADE, null=True)
    rented_when: models.DateTimeField()
    time_left: models.DateTimeField()
    collection: models.ForeignKey(Collection, on_delete=models.CASCADE)
