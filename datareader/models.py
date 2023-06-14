from django.db import models

class Datas(models.Model):
    first_ratings = models.CharField(max_length=999)
    expected_results = models.CharField(max_length=999)
    points = models.CharField(max_length=999)
    status = models.CharField(max_length=999)
    notes = models.CharField(max_length=999)

    def __str__(self):
        return self.name
