# Generated by Django 4.0.2 on 2022-02-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divers', '0003_alter_review_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comments',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]
