from django.db import models

# Create your models here.


class Prize(models.Model):
    prize_id = models.CharField(max_length=20)
    prize_cname = models.CharField(max_length=20)
    prize_amount = models.IntegerField()

    def __str__(self):
        return self.prize_cname


class Winner(models.Model):
    last_ssn = models.CharField(max_length=3)
    prize_id = models.ForeignKey(
        "Prize", on_delete=models.CASCADE)

    def __str__(self):
        return self.prize_id.prize_cname + ", " + self.last_ssn
