from django.db import models


class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
