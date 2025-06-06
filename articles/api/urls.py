from django.urls import path
from .views import index, add_article, agb, legal_notice

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_article, name='add_article'),
    path('agb/', agb, name='agb'),
    path('legal-notice/', legal_notice, name='legal_notice'),
]