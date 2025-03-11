from django.db import models
from users.models import User


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    # email = models.EmailField()
    location = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    # insert_cv = models.FileField(upload_to='resume/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"
