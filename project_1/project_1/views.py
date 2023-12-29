from django.http import HttpResponse



def contact(request):
    return HttpResponse("Main-This is Contact")

def home(request):
    return HttpResponse("Main-Home page")


