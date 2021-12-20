from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola, mundo! Te encuentras en el índice de POLLS.")

