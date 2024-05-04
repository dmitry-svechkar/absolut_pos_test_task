
from django.contrib import admin
from django.contrib.auth.models import Group, User

from django.urls import path
from survey.views import survey_view

from .views import FinishSurveyView, MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/<int:question_id>/', survey_view, name='survey-view'),
    path('survey/finish', FinishSurveyView.as_view(), name='finished_survey'),
    path('', MainView.as_view(), name='main'),
]

admin.site.site_header = 'Админ панель опросов'
admin.site.site_title = 'Админ панель опросов'
admin.site.index_title = '''
Во вкладке Установочная модель опросов:
1. Создать опрос.
2. Создать вопросы и ответы.

Поле собранных данных опросов:
Данные для последующей аналитики.
'''

admin.site.unregister(Group)
admin.site.unregister(User)
