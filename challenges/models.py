from django.db import models


# Create your models here.
class Challenge(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Month(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class ChallengeMonth(models.Model):
    id = models.AutoField(primary_key=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.month.name}: {self.challenge.name}"
