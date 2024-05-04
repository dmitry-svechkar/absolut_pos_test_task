from django import forms

from .models import AnswerModel


class AnswerForm(forms.Form):
    """
    Форма обработки ответов посредством выбора
    ОДНОГО из предоставленных ответов.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['answer'] = forms.ModelChoiceField(
            queryset=AnswerModel.objects.all(),
            widget=forms.RadioSelect
        )

    def clean_answer(self):
        data = self.cleaned_data['answer']
        return data
