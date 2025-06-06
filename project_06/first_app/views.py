from django.shortcuts import render
from .forms import contact_form,student_data,password_validation

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    if request.method == 'POST':
        

        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
    return render(request, 'about.html', {'name': name, 'email': email, 'select':select})


def submit_form(request):
    return render(request,'form.html')

def Django_form(request):
    if request.method == 'POST':
        form = contact_form(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
        return render(request,'django_form.html', {'form': form})
    else:
        form = contact_form()
    return render(request, 'django_form.html', {'form': form})



def student_form(request):

    if request.method == 'POST':
        form = student_data(request.POST , request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request,'django_form.html', {'form': form})
    else:
        form = student_data()
    return render(request, 'django_form.html', {'form': form})



def password_check(request):

    if request.method == 'POST':
        form = password_validation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request,'django_form.html', {'form': form})
    else:
        form = password_validation()
    return render(request, 'django_form.html', {'form': form})
