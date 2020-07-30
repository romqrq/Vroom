from django.shortcuts import render
from django.contrib import messages


def index_view(request):
    """View that displays the index page"""
    return render(request, 'index.html')


def about_view(request):
    """View that displays the About page"""
    return render(request, 'about.html')


def faqs_view(request):
    """View that displays the Frequently Asked Questions page"""
    return render(request, 'faqs.html')


def contact_view(request):
    """View that displays the Frequently Asked Questions page"""
    if request.method == 'POST':
        messages.success(
            request,
            "Thanks for contacting us! We'll get back to you soon.")
        return render(request, 'index.html')
    return render(request, 'contact.html')
