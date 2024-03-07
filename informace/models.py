from django.db import models

# Create your models here.

class Pavilon(models.Model):
    jmeno = models.CharField(max_length=30)
    umisteni = models.CharField(max_length=40)

    def __str__(self):
        return self.jmeno


class Zvire(models.Model):
    jmeno = models.CharField(max_length=30)
    druh = models.CharField(max_length=30)
    vek = models.IntegerField()
    popis = models.CharField(max_length=200)
    barva = models.CharField(max_length=30, null=True)
    pavilon = models.ForeignKey(Pavilon, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return f"{self.druh} {self.jmeno} má {self.vek} let."
    
    class Meta:
        verbose_name_plural = "Zvirata"
        ordering = ("jmeno", "-id")
    


