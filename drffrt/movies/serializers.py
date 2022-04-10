from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= ['film', 'year', 'audience_score_percent', 'genre', 'lead_studio', 'profitability', 'rotten_tomatoes_percent', 'worldwide_gross_usd']
