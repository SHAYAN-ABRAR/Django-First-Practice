from calendar import month
from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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

def post_list(request):
    return render(request, 'blog/post_list.html')

# DICTIONARY EXAMPLE
# class user:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# def profile(request):
#     context = {
#         "name": "Alice",
#         "age": 30,
#         "skills": ["Django", "Python", "JavaScript"],
#         "user": user("Alice", 30),
#         "blog":{
#             "title": "Django Development",
#             "content": "A blog about Django development.",
#             "created_at": datetime.now()
#         },
#         "empty_value": None
#     }
#     return render(request, 'blog/home.html', context)

def post_list(request):
    blogs = [
        {"title": "First Blog Post", "is_featured": True, "author": "Shayan Abrar"},
        {"title": "Second Blog Post", "is_featured": False, "author": ""},
        {"title": "Third Blog Post", "is_featured": False, "author": "Ratul"},
    ]
    context = {
        "blogs": blogs,
        "title": "My First Blog Post",
        "author": "John Doe",
        "content": "This is the content of my first blog post.",
        "today": datetime.now(),
        "html_code": "<h1>This is a paragraph of HTML code.</h1>",
        "tags": ["Django", "Python", "Web Development"],
        "comments": [
            {"user": "Alice", "comment": "Great post!", "date": datetime.now()},
            {"user": "Bob", "comment": "Very informative.", "date": datetime.now()}
        ],
        "price": 10,
        "number": 7,
    }
    return render(request, 'blog/post_list.html', {"post": context})