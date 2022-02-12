# Generated by Django 4.0.2 on 2022-02-12 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('max_depth', models.IntegerField()),
                ('site_type', models.CharField(max_length=100)),
                ('marine_life', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('visited', models.BooleanField()),
                ('favorite', models.BooleanField()),
                ('bucket_list', models.BooleanField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitors', to='dive.site')),
            ],
        ),
    ]