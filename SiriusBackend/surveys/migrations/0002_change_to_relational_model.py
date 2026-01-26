# Generated migration for changing to relational model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        # Create QuestionAnswer model
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_value', models.PositiveSmallIntegerField(help_text='Answer value between 1 and 5', verbose_name='Answer value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='surveys.surveyquestion', verbose_name='Question')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='surveys.questionnaire', verbose_name='Questionnaire')),
            ],
            options={
                'verbose_name': 'Question Answer',
                'verbose_name_plural': 'Question Answers',
                'ordering': ['question__order'],
                'unique_together': {('questionnaire', 'question')},
            },
        ),
        # Remove the answers JSONField from Questionnaire
        migrations.RemoveField(
            model_name='questionnaire',
            name='answers',
        ),
    ]
