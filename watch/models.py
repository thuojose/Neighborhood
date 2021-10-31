from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from django.db.models import Q

Priority=(
    ('Informational', 'Informational'),
    ('High Priority', 'High Priority'),
)

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length = 60)

    def __str__(self):
        return self.neighbourhood_name

    def create_neighbourhood(self):
        self.save()
        
    @classmethod
    def delete_neighbourhood(cls, neighbourhood_name):
        cls.objects.filter(neighbourhood_name=neighbourhood_name).delete()

    @classmethod
    def find_neighbourhood(cls, search_term):
        search_results = cls.objects.filter(neighbourhood_name__icontains = search_term)
        return search_results

    def update_neighbourhood(self, neighbourhood_name):
        self.neighbourhood_name = neighbourhood_name
        self.save()

