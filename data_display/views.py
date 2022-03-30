from distutils.command.build_scripts import first_line_re
import imp
from pkgutil import ImpImporter
import re
from tkinter.messagebox import NO
from django.shortcuts import render

from .models  import DisplayData

# Create your views here.


def main_home (request):

    print(request.GET)



    firstname_data = request.GET.get("name")
    lastname_data = request.GET.get("lastname")
    valu1_data = request.GET.get("valu1")
    valu2_data = request.GET.get("valu2")

    print(firstname_data , lastname_data , valu1_data , valu2_data)        

    new_entery = DisplayData(first_name = firstname_data , last_name = lastname_data , valu1=valu1_data , valu2=valu2_data)
    new_entery.save()
    return render(request,"home.html"   )