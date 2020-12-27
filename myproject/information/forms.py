from django import forms
from information.models import Clientdetails,Projectdetails,User
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from dal import autocomplete
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit, Button
from bootstrap_datepicker_plus import TimePickerInput,DatePickerInput
import datetime

class ClientForm(forms.ModelForm):
    requirements = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write requirements'}))

    contact = forms.CharField( widget=forms.TextInput(attrs={'type':'number'}))
  
    error_messages = {
        'contact': {
            'max_length': _("This contact no. is too long."),
           },
       }

    def clean_clientname(self):
        clientname = self.cleaned_data.get('clientname')
        if clientname.isnumeric():
            raise forms.ValidationError("Enter a valid name")
        return clientname

    class Meta:
        model = Clientdetails
        fields = ["clientname", "contact","requirements","budget","is_active"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()  

        self.helper.layout = Layout(
                Row(
                    Column('clientname', css_class='form-group col-md-6 mb-0'),
                    Column('contact', css_class='form-group col-md-3 mb-0'),
                    Column('budget', css_class='form-group col-md-3 mb-0'),
                    css_class='form-row'
                ),
            'requirements',
            'is_active',
            Submit('submit', 'Submit'),
            HTML('<a href="{% url "home" %}" class="btn btn-outline-dark ml-2">Cancel</a>'),
        )
   
class ProjectForm(forms.ModelForm):
    complete_date = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write description'}))

    userdata = forms.ModelMultipleChoiceField(widget=autocomplete.ModelSelect2Multiple(url='user-autocomplete'),queryset=User.objects.filter(is_active=1))
    clients = forms.ModelChoiceField(queryset=Clientdetails.objects.filter(is_active=1))

    def clean_projectname(self):
        projectname = self.cleaned_data.get('projectname')
        if projectname.isnumeric():
            raise forms.ValidationError("Enter a valid name")
        return projectname

    def clean_complete_date(self):
        complete_date = self.cleaned_data['complete_date']
        if complete_date < datetime.date.today():
            # print(complete_date)
            raise forms.ValidationError("The date cannot be in the past date")
        return complete_date

    class Meta:
        model = Projectdetails
        fields = ["projectname", "description","complete_date","clients","userdata","is_active"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()  
        self.fields["complete_date"].widget = DatePickerInput()
        self.fields['userdata'].help_text = "Click box to select mulitple users"
        self.fields['complete_date'].help_text = "The date cannot be the past date"


        self.helper.layout = Layout(
                Row(
                    Column('projectname', css_class='form-group col-md-6 mb-0'),
                    Column('complete_date', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
            'description',
            'clients',
            'userdata',
            'is_active',
            Submit('submit', 'Submit'),
            HTML('<a href="{% url "add_project" %}" class="btn btn-outline-dark ml-2">Cancel</a>'),
        )
   

   
