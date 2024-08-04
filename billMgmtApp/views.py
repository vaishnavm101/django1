from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloFunction(request):
    print("Hello world")
    return HttpResponse('<h1>Hello World</h1> <a href="contact">Goto Contact page</a>')


def contactFunction(request):
    names = ["Vaishnav", "Priya", "Shubham", "Gurbux"]
    data = {
        "names": names,
        "city":"Mumbai"
    }
    return render(request, "contact.html", data)


def getUser(request, username):
    print(username)
    return HttpResponse("Hello " + username)

