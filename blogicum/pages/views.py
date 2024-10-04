from django.shortcuts import render

# Create your views here.
def about(request):
    return render('about.html')

def rules(request):
    return render('rules.html')