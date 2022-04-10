from django.db import models

class Movie(models.Model):

    film = fields.Str(max_length=100) # the title of the film
    year = fields.SmallIntegerField()
    audience_score_percent = fields.Decimal(max_digits=4, decimal_places=2, blank=True)
    genre = fields.Str(max_length=100,allow_blank=True)
    lead_studio = fields.Str(max_length=100,allow_blank=True)
    profitability = fields.Decimal(max_digits=10, decimal_places=2, blank=True)
    rotten_tomatoes_percent = fields.Decimal(max_digits=4, decimal_places=2, blank=True)
    worldwide_gross_usd = fields.Decimal(max_digits=10, decimal_places=2, blank=True)

    class Meta:
        ordering = ['created']
