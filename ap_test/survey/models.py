from django.db import models


class SurveyModel(models.Model):
    """
    Модель опроса.
    Связана с моделью QuestionModel.

    Атрибуты:
        servey_name - Наименование опроса.
        description - Описание опроса.
    """
    servey_name = models.CharField(
        'Наименование опроса',
        max_length=100
    )
    description = models.TextField('Описание опроса.')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.servey_name


class QuestionModel(models.Model):
    """
    Модель вопросов

    Атрибуты:
        survey - FK к модели SurveyModel.
        question - объект вопроса
        depends_on - объект зависимого вопроса.
                Реализация связанного порядка вопросов друг за другом,
                без учета привязки к пред. ответам.
        answer - FK к модели AnswerModel.
        initial_question - Булево значение.
                'Инициализирующий(первый) вопрос',
                задается как первый вопрос в каждом опросе.
    """
    survey = models.ForeignKey(
        SurveyModel,
        on_delete=models.CASCADE,
        related_name='survey',
        verbose_name='опрос'
    )
    question = models.CharField('Вопрос', max_length=100)
    depends_on = models.ForeignKey('self',
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name='previous_questions',
                                   verbose_name='следующий вопрос')
    answer = models.ForeignKey(
        'AnswerModel',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    initial_question = models.BooleanField(
        'Инициализирующий(первый) вопрос',
        default=False
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question


class AnswerModel(models.Model):
    """
    Модель ответов на вопросы.

    Атрибуты:
        question - FK к модели QuestionModel.
        text_of_answer - ответ на вопрос.
        next_question - объект зависимого вопроса.
                Реализация связанного порядка вопросов друг за другом,
                Привязка реализуется по выбронному варианту ответа.

    """
    question = models.ForeignKey(
        QuestionModel,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос'
    )
    text_of_answer = models.CharField(
        'Ответ на вопрос',
        max_length=100,
        null=True,
        blank=True
    )
    next_question = models.ForeignKey(
        QuestionModel,
        on_delete=models.SET_NULL,
        related_name='next_questions',
        null=True,
        blank=True,
        verbose_name='Следующий вопрос, если выбран этот ответ'
    )

    class Meta:
        verbose_name = 'Установочная модель опросов'
        verbose_name_plural = 'Установочная модель опросов'

    def __str__(self):
        return self.text_of_answer


class DataModel(models.Model):
    """
    Модель сохранения данных, полученных с заполненной формы.

    Атрибуты:
        survey - FK к модели SurveyModel. Объект опроса
        question - FK к модели QuestionModel. Объект вопроса
        answer - FK к модели AnswerModel. Объект ответа на вопрос.
        created_at - Автополе даты-время получения и сохранения объекта в БД.
    """
    survey = models.ForeignKey(
        SurveyModel,
        on_delete=models.CASCADE,
        verbose_name='Опрос'
    )
    question = models.ForeignKey(
        QuestionModel,
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    answer = models.ForeignKey(
        AnswerModel,
        on_delete=models.CASCADE,
        verbose_name='Ответ на вопрос'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
        )

    class Meta:
        verbose_name = 'Поле собранных данных опросов.'
        verbose_name_plural = 'Поле собранных данных опросов.'

    def __str__(self):
        return f"Ответ пользователя {self.answer} на вопрос {self.question}"
