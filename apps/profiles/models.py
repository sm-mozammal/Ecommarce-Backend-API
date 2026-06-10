from django.db import models

# Create your models here.
class UserProfile(models.Model):

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
