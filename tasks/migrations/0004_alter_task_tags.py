# Generated by Django 5.1.4 on 2025-01-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(related_name='tasks', to='tasks.tag'),
        ),
    ]
