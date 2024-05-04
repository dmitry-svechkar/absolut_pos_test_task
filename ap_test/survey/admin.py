from django.contrib import admin

from .models import AnswerModel, DataModel, QuestionModel, SurveyModel


class QuestionInline(admin.TabularInline):
    model = QuestionModel


class AnswerInline(admin.TabularInline):
    model = AnswerModel


@admin.register(SurveyModel)
class ServeyAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(AnswerModel)
class AnswerModelAdmin(admin.ModelAdmin):
    """
    Основная надстройка админ-панели по добавлению опросов
    Реализованы доп поля из связанных моделей
    depends_on - следующий вопрос
    survey - опрос
    initial_question - Bool: инициализирующий(первый) вопрос
    + подключен Inline данных модели QuestionModel
    """
    list_select_related = ['question',]
    list_display = [
        'survey',
        'question',
        'initial_question',
        'text_of_answer',
        'next_question',
        'depends_on'
    ]
    fields = [
        'question',
        'text_of_answer',
        'next_question',
    ]
    inlines = [QuestionInline,]

    def depends_on(self, obj):
        return obj.question.depends_on
    depends_on.short_description = 'следующий вопрос'

    def survey(self, obj):
        return obj.question.survey
    survey.short_description = 'Опрос'

    def initial_question(self, obj):
        return obj.question.initial_question
    initial_question.short_description = '(первый) вопрос'


@admin.register(DataModel)
class DataAdmin(admin.ModelAdmin):
    list_display = ['survey', 'question', 'answer', 'created_at']
