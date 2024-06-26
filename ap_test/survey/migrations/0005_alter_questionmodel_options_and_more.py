# Generated by Django 4.2.11 on 2024-05-04 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_questionmodel_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionmodel',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='surveymodel',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='initial_question',
            field=models.BooleanField(default=False, verbose_name='Инициализирующий(первый) вопрос'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='depends_on',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_questions', to='survey.questionmodel', verbose_name='следующий вопрос'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='question',
            field=models.CharField(max_length=100, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='survey.surveymodel', verbose_name='опрос'),
        ),
        migrations.AlterField(
            model_name='surveymodel',
            name='description',
            field=models.TextField(verbose_name='Описание опроса.'),
        ),
        migrations.AlterField(
            model_name='surveymodel',
            name='servey_name',
            field=models.CharField(max_length=100, verbose_name='Наименование опроса'),
        ),
    ]
