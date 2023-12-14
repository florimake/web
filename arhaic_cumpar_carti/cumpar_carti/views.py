from django.shortcuts import render
from .models import *

# Create your views here.

############################################################### index ##################################################################
def view_index(request):
    context = {"headerparagrafe": HeaderParagraf.objects.all(), "paragrafe": Paragraf.objects.all(), "contacte": Contact.objects.all()}
    # print(context)
    return render(request, "index.html", context)
############################################################### index ##################################################################