from django.db import models

# Create your models here.
class landscape(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=20)
    descrizione = models.CharField(max_length=40)

    def __str__(self):
        return self.nome 
