from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>BLOG Home Page!</h1>")

def about(request):
    a = 50+10
    return HttpResponse(f"""
        <h1>BLOG About Page!</h1>
        <p>Calculation result: {a}</p>
        <p>This is a much cleaner way to write HTML in Python.</p>
    """)
    