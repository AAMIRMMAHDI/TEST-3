# Generated by Django 4.2 on 2024-07-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0007_propertyes_alter_questions_options_pricing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='propertyes',
        ),
        migrations.AddField(
            model_name='pricing',
            name='propertyes',
            field=models.ManyToManyField(to='root.propertyes'),
        ),
    ]
