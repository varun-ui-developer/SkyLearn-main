# Generated by Django 4.2.16 on 2024-09-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0002_choice_choice_en_choice_choice_ru_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="choice_es",
            field=models.CharField(
                help_text="Enter the choice text that you want displayed",
                max_length=1000,
                null=True,
                verbose_name="Content",
            ),
        ),
        migrations.AddField(
            model_name="choice",
            name="choice_fr",
            field=models.CharField(
                help_text="Enter the choice text that you want displayed",
                max_length=1000,
                null=True,
                verbose_name="Content",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="content_es",
            field=models.CharField(
                help_text="Enter the question text that you want displayed",
                max_length=1000,
                null=True,
                verbose_name="Question",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="content_fr",
            field=models.CharField(
                help_text="Enter the question text that you want displayed",
                max_length=1000,
                null=True,
                verbose_name="Question",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="explanation_es",
            field=models.TextField(
                blank=True,
                help_text="Explanation to be shown after the question has been answered.",
                max_length=2000,
                null=True,
                verbose_name="Explanation",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="explanation_fr",
            field=models.TextField(
                blank=True,
                help_text="Explanation to be shown after the question has been answered.",
                max_length=2000,
                null=True,
                verbose_name="Explanation",
            ),
        ),
        migrations.AddField(
            model_name="quiz",
            name="description_es",
            field=models.TextField(
                blank=True,
                help_text="A detailed description of the quiz",
                null=True,
                verbose_name="Description",
            ),
        ),
        migrations.AddField(
            model_name="quiz",
            name="description_fr",
            field=models.TextField(
                blank=True,
                help_text="A detailed description of the quiz",
                null=True,
                verbose_name="Description",
            ),
        ),
        migrations.AddField(
            model_name="quiz",
            name="title_es",
            field=models.CharField(max_length=60, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="quiz",
            name="title_fr",
            field=models.CharField(max_length=60, null=True, verbose_name="Title"),
        ),
    ]
