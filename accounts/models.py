from typing import ClassVar
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Staff Models.
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name="staff")
    otherNames = models.CharField(max_length=50)
    hometown = models.CharField(max_length=50)
    phoneNumber= models.CharField(max_length=10)
    emergencyContactPerson = models.CharField(max_length=50)
    emergencyContactNumber = models.CharField(max_length=10)
    picture = models.ImageField(upload_to = "profile/")
    dateCreated = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ("-user",)


    def __str__(self) -> str:
        return self.user.username + " " + self.otherNames
