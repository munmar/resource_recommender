from django.shortcuts import render
from django.http import HttpResponse

def recommend_courses(request):
    return render(request, 'index.html')