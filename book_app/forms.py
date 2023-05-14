from django import forms
from .models import FeedBack


class FeedBackFrom(forms.Form):
    # name = forms.CharField(max_length=7, min_length=2, error_messages={
    #     "max_length": "Слишком много символов, должно быть %(limit_value)d, сейчас символов %(show_value)d.",
    #     "min_length": "Слишком мало символов, должно быть %(limit_value)d, сейчас символов  %(show_value)d.",
    #     "required": "Обязательно к заполнению",
    # })
    name = forms.CharField()
    surname = forms.CharField()
    feedback = forms.CharField()

    class Meta:
        model = FeedBack
        fields =('name''surname','feedback')
