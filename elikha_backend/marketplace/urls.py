from django.urls import path
from . import views

app_name = 'marketplace' # Optional: for namespacing URLs

urlpatterns = [
    path('', views.home_view, name='home'),
]
