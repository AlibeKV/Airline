# Generated by Django 4.2.2 on 2023-10-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plane', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Аэрапорт')),
                ('data', models.DateField(verbose_name='дата вылета')),
                ('plane', models.ManyToManyField(to='plane.plane')),
            ],
        ),
    ]