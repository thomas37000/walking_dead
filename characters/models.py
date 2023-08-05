from django.db import models
from django.core.exceptions import ValidationError
from private_storage.fields import PrivateFileField


def validate_image_size(value):
    # Taille maximale en octets (1 Mo)
    max_size = 1024 * 1024

    if value.size > max_size:
        raise ValidationError("La taille de l'image ne doit pas dépasser 1 Mo.")
    
# class Membership(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.name
    
# class Friend(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.name
    
# class Enemy(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.name

class Character(models.Model):
    name = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    birth = models.CharField(max_length=255, null=True)
    death = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    is_alive = models.BooleanField()
    country = models.CharField(max_length=50, null=True)
    image = models.FileField(upload_to='public', null=True)
    private_image = PrivateFileField(upload_to='private', null=True)
    # membership = models.ManyToManyField(Membership, blank=True)
    # friends = models.ManyToManyField(Friend, blank=True)
    # enemies = models.ManyToManyField(Enemy, blank=True)
    
    def __str__(self):
        return self.name + " " + self.lastname
    
    charactersList = models.ForeignKey("CharactersList", null=False, on_delete=models.CASCADE)
    
class CharactersList(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Character List'
        verbose_name_plural = 'Characters List'