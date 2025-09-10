from django.shortcuts import render
from .forms import ApplicationForm

def index(request):
    #get the data from the widgets
    if request.method == "POST":
        #ContactForm Class
        form = ApplicationForm(request.POST)
        if form.is_valid():
            #dictionary is created in cleaned_data like {"first_name":"John","last_name":"Smith"}
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            print(first_name,last_name, email,date,occupation)
    return render(request,"index.html")



