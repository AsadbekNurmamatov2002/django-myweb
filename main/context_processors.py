from .models import ManiCatigorey, Boglanish, Reclama, Navbar

def manicatigorey(request):
    catigorey_context=ManiCatigorey.objects.all().order_by('-id')
    return {'mcatigorey_context':catigorey_context }

def reclama(request):
    reclama_context=Reclama.objects.all().order_by('-id')
    return {'reclama_context':reclama_context }

def boglanish(request):
    boglanish_context=Boglanish.objects.all().order_by('-id')
    return {'boglanish_context':boglanish_context}

def navbar(request):
    navbar=Navbar.objects.all().order_by('-id')
    return {'navbar':navbar}