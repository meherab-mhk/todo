from django.urls import path
from . views import polls_views

urlpatterns = [
    path('list/',  polls_views, name='polls_views'),
]
