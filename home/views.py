from django.shortcuts import render


def index_view(request):
    """View that displays the index page"""
    return render(request, 'index.html')


def about_view(request):
    """View that displays the About page"""
    return render(request, 'about.html')
