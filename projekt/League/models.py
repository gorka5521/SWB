from django.db import models
import cassiopeia as cass

# Create your models here.

class Rola(models.Model):
    nazwa = models.TextField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Rola"
        verbose_name_plural = "Role"


class Pozycja(models.Model):
    nazwa = models.TextField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Pozycja"
        verbose_name_plural = "Pozycje"


class Postac(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=2000)
    rola = models.ForeignKey(Rola, on_delete=models.CASCADE, null=True)
    pozycja = models.ForeignKey(Pozycja, on_delete=models.CASCADE, null=True)
    kod = models.CharField(max_length=10)

    nazwaP = models.CharField(max_length=100)
    opisP = models.CharField(max_length=500)

    nazwaQ = models.CharField(max_length=100)
    opisQ = models.CharField(max_length=500)

    nazwaW = models.CharField(max_length=100)
    opisW = models.CharField(max_length=500)

    nazwaE = models.CharField(max_length=100)
    opisE = models.CharField(max_length=500)

    nazwaR = models.CharField(max_length=100)
    opisR = models.CharField(max_length=500)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Postać"
        verbose_name_plural = "Postacie"