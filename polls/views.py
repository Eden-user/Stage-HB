from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, bby ! You're at the polls index ;)")
