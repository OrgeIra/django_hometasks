# Generated by Django 5.0.4 on 2024-05-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_desc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=55)),
                ('age', models.IntegerField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'teacher_desc',
            },
        ),
    ]
