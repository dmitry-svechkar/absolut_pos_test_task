from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from survey.models import QuestionModel


class MainView(TemplateView):
    """
    Вью рендеренига шаблона первичной страницы.

    Допонительно передается объект первого вопроса
    к каждому конкретному опросу.

    """
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        initial_question = get_object_or_404(
            QuestionModel,
            initial_question=True
        )
        context['initial_question'] = initial_question
        return context


class FinishSurveyView(TemplateView):
    """
    Вью рендеренига шаблона завершения опроса.
    """
    template_name = "finish_survey.html"
