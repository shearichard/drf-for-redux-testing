from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import generics, filters
import django_filters.rest_framework
#from django_filters import DjangoFilterBackend


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'film', 'year', 'lead_studio']


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
