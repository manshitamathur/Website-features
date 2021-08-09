from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Submit, Row, Column
# Create your forms here.

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name','last_name','subject','email_address','message')
        widgets = {
            'name':forms.TextInput(attrs={ 'style': 'border-color: blue;',
                'placeholder': 'Write your name here'}),
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 20}),
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('subject', css_class='form-group col-md-6 mb-0'),
                Column('email_address', css_class='form-group col-md-6 mb-0'),
                
                css_class='form-row'
            ),
            'message',
            Submit('submit', 'Submit Response')
        )



class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))