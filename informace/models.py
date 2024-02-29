from django.db import models

# Create your models here.

class Zvire(models.Model):
    jmeno = models.CharField(max_length=30)
    druh = models.CharField(max_length=30)
    vek = models.IntegerField()
    popis = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.druh} {self.jmeno} má {self.vek} let."
    
# LAZY EVALUATION

