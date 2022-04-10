from django.db import models


class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    film = fields.Str(max_length=100) # the title of the film
    year = fields.Str(min_length=4, max_length=4)
    audience_score_percent = fields.Str(max_length=2,allow_blank=True)
    genre = fields.Str(max_length=100,allow_blank=True)
    lead_studio = fields.Str(max_length=100,allow_blank=True)
    profitability = fields.Str(max_length=100,allow_blank=True)
    rotten_tomatoes_percent = fields.Str(max_length=2,allow_blank=True)
    worldwide_gross_usd = fields.Str(max_length=20,allow_blank=True)

    class Meta:
        ordering = ['created']
