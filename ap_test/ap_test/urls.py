
from django.contrib import admin
from django.urls import path
from survey.views import survey_view

from .views import FinishSurveyView, MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/<int:question_id>/', survey_view, name='survey-view'),
    path('survey/finish', FinishSurveyView.as_view(), name='finished_survey'),
    path('', MainView.as_view(), name='main'),
]
