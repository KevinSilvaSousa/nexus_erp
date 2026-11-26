from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    nexus_erp = "Nexus ERP"

    test = {
        "company_name": nexus_erp,
        "version": " 1.0"
    }
    
    return render(request, "core/home.html", test)