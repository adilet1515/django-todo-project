from django.forms import ModelForm, Textarea,CharField
from .models import TodoItem


class TodoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = ( "text",)
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 5, 'placeholder': 'Введите текст'}),

        }




