# Generated by Django 3.1.3 on 2023-05-27 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0008_question_modify_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='voter',
            field=models.ManyToManyField(default=0, related_name='voter_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
