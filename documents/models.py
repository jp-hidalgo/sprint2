from django.db import models

from users.models import User

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    length = models.FloatField(null=True, blank=True, default=None)
    fileType = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)