from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"Home.html")
#create a view for about 
def about(request):
    return render(request,"about.html")
#create a view for contact
def contact(request):
    return render(request,"contact.html")