from django.shortcuts import render


def index_view(request):
    """View that displays the index page"""
    return render(request, 'index.html')
