# Generated by Django 5.0 on 2024-01-02 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_question_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
