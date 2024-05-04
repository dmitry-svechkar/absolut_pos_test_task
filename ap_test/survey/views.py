from django.shortcuts import redirect, render

from .forms import AnswerForm
from .models import AnswerModel, DataModel, QuestionModel


def survey_view(request, question_id):
    """
    Вью-функция обработки рендеринга данных
    и сохранения полученных ответов в БД.
    Вью-функция отвечает за обработку запросов к опросу
    и сохранение ответов в базе данных.

    Аргументы:
        request - объект запроса
        question_id - идентификатор вопроса

    Если  POST - обрабатывает данные формы
    и пользователь перенаправляется на следующий вопрос
    или на страницу с результатами опроса в зависимости от условий.
    Реализована логика редиректа со связанными условиями:
        Первая проверка: Зависимость след. вопроса от полученного ответа.
        Вторая провека: Зависимость след. вопроса от пред. вопроса.
        Должно быть реализовано только 1 из условий.

    Есди GET - функция возвращает шаблон с формой для ответа на вопрос.
    """
    form = AnswerForm()
    question = QuestionModel.objects.get(
        id=question_id
    )
    answers = AnswerModel.objects.filter(
        question=question
    )
    form.fields['answer'].queryset = answers

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            selected_answer = form.cleaned_data['answer']
            data_instance = DataModel(
                survey=question.survey,
                question=question,
                answer=selected_answer,
            )
            data_instance.save()
            next_question = AnswerModel.objects.get(
                text_of_answer=selected_answer
            ).next_question
            if next_question:
                return redirect(
                    'survey-view',
                    question_id=next_question.id
                )
            if question.depends_on:
                return redirect(
                    'survey-view',
                    question_id=question.depends_on.id
                )
            return redirect('finished_survey')
    return render(
        request,
        'survey.html',
        {'form': form, 'question': question}
    )
