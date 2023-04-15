from django.db import models

class Plan(models.Model):
    sarlavha = models.CharField(max_length=20)
    batafsil = models.CharField(max_length=300, null=True, blank=True)
    oxirgi_muddat = models.DateField()
    zarurlik = models.CharField(max_length=12)
    bajarildi = models.BooleanField(default=False)
    sana = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.sarlavha}"
