# Generated by Django 3.2.7 on 2021-10-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20211024_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='eid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
