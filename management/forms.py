from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
        
class ProfileUdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(ProfileUdateForm, self).__init__(*args, **kwargs)
        self.fields['State'].empty_label = '--Select State--'
        
    # def __init__(self, *args, **kwargs):
    #     super(ProfileUdateForm, self).__init__(*args, **kwargs)
    #     self.fields['position'].empty_label = 'select'
        
        
        
class Userprofileform(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['profile_pic']
        

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='Your Username')
    email = forms.EmailField(required=True, label='Your Email')
    last_name = forms.CharField(max_length=30, label='Your Surname')
    first_name = forms.CharField(max_length=30, label='Your Full name')
    password1 = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, label='Repeat your password', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields[field_name].widget.attrs.update({
                "placeholder": field.label,
                'class': "input-control"
            })
        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveDetail
        fields = '__all__'
        exclude = ['author']
        labels = {   
            'Reason': 'Reason/Comments',
        }
        

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['leave_type'].empty_label = 'Choice Leave Type'
        
        
        
        
        
        
        
        
# from bootstrap_datepicker_plus import DatePickerInput
# from django import forms

# # Custom Form usage
# class ToDoForm(forms.Form):
#     todo = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )
#     date = forms.DateField(
#         widget=DatePickerInput(format='%m/%d/%Y')
#     )
    
    
# # Model Form usage    
# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'start_date', 'end_date']
#         widgets = {
#             'start_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
#             'end_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
#         }
   
# # Types of DatePickers        
# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['start_date', 'start_time', 'start_datetime', 'start_month', 'start_year']
#         widgets = {
#             'start_date': DatePickerInput(),
#             'start_time': TimePickerInput(),
#             'start_datetime': DateTimePickerInput(),
#             'start_month': MonthPickerInput(),
#             'start_year': YearPickerInput(),
#         }
        
# # Implement date-range-picker
# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'start_date', 'end_date', 'start_time', 'end_time']
#         widgets = {
#             'start_date':DatePickerInput().start_of('event days'),
#             'end_date':DatePickerInput().end_of('event days'),
#             'start_time':TimePickerInput().start_of('party time'),
#             'end_time':TimePickerInput().end_of('party time'),
#         }