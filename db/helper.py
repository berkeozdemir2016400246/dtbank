from django.db import models

class DBManager(models.Model):
    username = models.CharField(max_length=45)
    password = models.TextField()

    def __str__(self):
        return self.name


