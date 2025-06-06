from django import forms
from django.core import validators  
class contact_form(forms.Form):
    name=forms.CharField(label="UserName", required=False, widget= forms.Textarea(attrs={'placeholder':'Enter your name'}))
    # file=forms.FileField()


    # email=forms.EmailField(label="UserEmail")
    # age=forms.IntegerField(label="User Age")
    # weight=forms.FloatField()
    # Balance=forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput)
    check=forms.BooleanField()


    birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))

    appoinment=forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))



    CHOICE= [('S',"Small"),('M','Medium'), ('L','Large')]
    size= forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)

    MEAL= [('S','Spicy'),('M','Mashroom'),('C','Cheese')]
    pizza= forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    

# class student_data(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)


#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
        
#         if len(valname) < 10 :
#             raise forms.ValidationError("Enter a name at least 10 char")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your Email Must contain .com ")


def len_text(value):
    if len(value) <10:
        raise forms.ValidationError("text at least 10 char")



class student_data(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(10,message='Enter a Name at least 10 char')])

    text= forms.CharField(widget=forms.TextInput, validators=[len_text])


    email=forms.CharField(widget=forms.EmailInput , validators=[validators.EmailValidator(message="Enter a valid Email")])
    age=forms.IntegerField(validators=[validators.MinValueValidator(18,message="Age at least 18"), validators.MaxValueValidator(35,message="Age Must be 35")])

    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="File Must be in pdf format")])


class password_validation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pass = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
     cleaned_data= super().clean()

     val_pass = self.cleaned_data['password']
     con_pass = self.cleaned_data['confirm_pass']
     val_name = self.cleaned_data['name']

     if val_pass != con_pass:
        raise forms.ValidationError("Enter a Valid Password")
     if len(val_name) < 10 :
        raise forms.ValidationError("Name at least 10 char")





