# predictions/forms.py

from django import forms

class PredictionForm(forms.Form):
    sex = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    age = forms.IntegerField(min_value=18)
    region = forms.ChoiceField(choices=[('northwest', 'Northwest'), ('northeast', 'Northeast'),
                                       ('southwest', 'Southwest'), ('southeast', 'Southeast')])
    children = forms.IntegerField(min_value=0)
    smoker = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')])
    bmi = forms.FloatField(min_value=10.0)
