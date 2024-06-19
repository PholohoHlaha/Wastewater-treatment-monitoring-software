from django.shortcuts import render

def operator(request):
    return render(request, "operator/operator.html")