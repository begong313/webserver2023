# Generated by Django 3.1.3 on 2023-05-24 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_answer_modify_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='modify_count',
            field=models.IntegerField(default=0),
        ),
    ]