from django.db import models

class Movie(models.Model):

    film = models.CharField(max_length=100) # the title of the film
    year = models.SmallIntegerField()
    audience_score_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    genre = models.CharField(max_length=100,blank=True)
    lead_studio = models.CharField(max_length=100,blank=True)
    profitability = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    rotten_tomatoes_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    worldwide_gross_usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    class Meta:
        ordering = ['film', 'year']
