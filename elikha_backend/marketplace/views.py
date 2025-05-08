from django.shortcuts import render

def home_view(request):
    return render(request, 'marketplace/home.html', {'message': 'Welcome to Elikha!'})
