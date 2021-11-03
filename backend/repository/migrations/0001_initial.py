# Generated by Django 3.2.7 on 2021-10-18 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('eid', models.IntegerField(max_length=2, primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('error_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('fid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('famount', models.IntegerField(max_length=10)),
                ('fcal', models.FloatField()),
                ('fcarboh', models.FloatField()),
                ('fprotein', models.FloatField()),
                ('ffat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_id', models.AutoField(primary_key=True, serialize=False)),
                ('train_date', models.DateField(auto_now_add=True)),
                ('error_name', models.CharField(max_length=30)),
                ('count', models.IntegerField(max_length=2)),
                ('error_count', models.IntegerField(max_length=2)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.exercise')),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.users')),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('diet_id', models.AutoField(primary_key=True, serialize=False)),
                ('diet_datetime', models.DateTimeField()),
                ('meal', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=30)),
                ('amount', models.IntegerField(max_length=10)),
                ('cal', models.FloatField()),
                ('carboh', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.food')),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.users')),
            ],
        ),
    ]
