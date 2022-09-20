from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return HttpResponse("Hello-)")


def about(request):
    author = {
        "name": "Евгений",
        "surname": "Юрченко",
        "email": "eyurchenko@specialist.ru"
    }
    return HttpResponse(str(author))