# Generated by Django 3.1 on 2021-06-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcvidadAdicionalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.CharField(max_length=1000)),
            ],
        ),
    ]
