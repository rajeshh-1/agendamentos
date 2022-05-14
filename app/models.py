from django.db import models

class ContactGroup(models.Model):
    """A model of a rock band."""
    description = models.CharField(max_length=200,null=False)


class Contact(models.Model):
    """A model of a rock band member."""
    name = models.CharField(max_length=200,null=False)
    phone = models.CharField(max_length=20,null=False)
    email = models.EmailField(max_length=200,null=False)
    address = models.CharField(max_length=200,null=False)
    number = models.IntegerField(null=False)
    district = models.CharField(max_length=200,null=False)
    cep = models.CharField(max_length=20,null=False)
    city = models.CharField(max_length=200,null=False)
    state = models.CharField(max_length=100,null=False)
    contactGroup = models.ForeignKey("ContactGroup", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)