from koffie.nespresso.models import cups
from django.http import HttpResponse

def cupsView(request):
    q = cups.objects.all()
    return HttpResponse(format(q))

