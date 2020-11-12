# Generated by Django 3.1.3 on 2020-11-12 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_question_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='option',
        ),
        migrations.AddField(
            model_name='options',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz_app.question'),
            preserve_default=False,
        ),
    ]
