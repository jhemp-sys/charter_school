from django.db import models

class First(models.Model):
    first_ratings = models.CharField(max_length=999)
    expected_results = models.CharField(max_length=999)
    points = models.CharField(max_length=999)
    status = models.CharField(max_length=999)
    notes = models.CharField(max_length=999)

    def __str__(self):
        return self.first_ratings
    
class PL(models.Model):
    numbers = models.CharField(max_length=999, default="")
    titles = models.CharField(max_length=999, default="")
    extra = models.CharField(max_length=999, default="")
    ammended_budget = models.CharField(max_length=999, default="")
    ytd_budget = models.CharField(max_length=999, default="" )
    september = models.CharField(max_length=999, default="")
    october = models.CharField(max_length=999, default="")
    november = models.CharField(max_length=999, default="")
    december = models.CharField(max_length=999, default="")
    january = models.CharField(max_length=999, default="")
    february = models.CharField(max_length=999, default="")
    march = models.CharField(max_length=999, default="")
    april = models.CharField(max_length=999, default="")
    may = models.CharField(max_length=999, default="")
    june = models.CharField(max_length=999, default="")
    july = models.CharField(max_length=999, default="")
    august = models.CharField(max_length=999, default="")
    year_to_date = models.CharField(max_length=999, default="" )
    variances = models.CharField(max_length=999, default="" )
    var = models.CharField(max_length=999, default="" )

    def __str__(self):
        return self.numbers
    
class BS(models.Model):
    titles = models.CharField(max_length=999, default="")
    extra = models.CharField(max_length=999, default="")
    fye_year = models.CharField(max_length=999, default="")
    september = models.CharField(max_length=999, default="") 
    october = models.CharField(max_length=999, default="") 
    november = models.CharField(max_length=999, default="") 
    december = models.CharField(max_length=999, default="") 
    january = models.CharField(max_length=999, default="") 
    february = models.CharField(max_length=999, default="") 
    march = models.CharField(max_length=999, default="") 
    april = models.CharField(max_length=999, default="") 
    may = models.CharField(max_length=999, default="") 
    june = models.CharField(max_length=999, default="") 
    july = models.CharField(max_length=999, default="") 
    august = models.CharField(max_length=999, default="") 
    fytd_activity = models.CharField(max_length=999, default="")
    as_of_january = models.CharField(max_length=999, default="")

    def __str__(self):
        return self.fye_year


