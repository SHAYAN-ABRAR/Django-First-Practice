from calendar import month
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

def post_detail(request, post_id):
    return HttpResponse(f"<h1>BLOG Post Detail Page for Post ID: {post_id}!</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>BLOG User Profile Page for User: {username}!</h1>")

def article_by_year(request, year):
    return HttpResponse(f"<h1>BLOG Articles from the Year: {year}!</h1>")

def article_detail(request, **kwargs):
    return HttpResponse(f"<h1>BLOG Article Detail Page from {kwargs}!</h1>")
    