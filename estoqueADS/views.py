from django.shortcuts import render, HttpResponse

def index(request):
    frutas = ['Maçã', 'Uva', 'Jambo']
    return render(request, 'pages/index.html', {"frutas": frutas})
