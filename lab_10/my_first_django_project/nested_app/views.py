from django.http import HttpResponse

# создание своих представлений
def home(request):
    return HttpResponse("<p>Home</p>")

def catalog(request):
    return HttpResponse("<p>Catalog</p>")

def textarea(request):
    return HttpResponse("<textarea></textarea>")
