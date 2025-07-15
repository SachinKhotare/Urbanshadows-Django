from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128, default='temp1234')
    confirmPassword = models.CharField(max_length=128, default='temp1234')

    def __str__(self):
        return self.name
