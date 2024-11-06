from Django.http import HttpResponse

# Create your views here.
def home(requests) :
    return HttpResponse('<h1>Welcome to Django Workings</h1>')