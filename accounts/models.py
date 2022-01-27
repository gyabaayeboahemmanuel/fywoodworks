from typing import ClassVar
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Staff Models.
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name="staff")
    hometown = models.CharField(max_length=50)
    phone_number= models.CharField(max_length=10)
    emergency_contact_person = models.CharField(max_length=50)
    emergency_contact_number = models.CharField(max_length=10)
    picture = models.ImageField(upload_to = "profile/")
    dateCreated = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ("-user",)


    def __str__(self) -> str:
        return self.user.first_name  + self.user.last_name
