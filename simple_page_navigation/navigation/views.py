from django.shortcuts import render

# Create your views here.
def contact(request):
   return render(request,'navigation/contact.html')


def phone(request):
    return render(request,'navigation/phone.html')
