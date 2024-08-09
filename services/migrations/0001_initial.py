# Generated by Django 5.0.7 on 2024-08-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka_kodu', models.IntegerField()),
                ('tip_kodu', models.IntegerField()),
                ('marka_adi', models.CharField(max_length=255)),
                ('tip_adi', models.CharField(max_length=255)),
                ('model_2024', models.IntegerField()),
                ('model_2023', models.IntegerField()),
                ('model_2022', models.IntegerField()),
                ('model_2021', models.IntegerField()),
                ('model_2020', models.IntegerField()),
                ('model_2019', models.IntegerField()),
                ('model_2018', models.IntegerField()),
                ('model_2017', models.IntegerField()),
                ('model_2016', models.IntegerField()),
                ('model_2015', models.IntegerField()),
                ('model_2014', models.IntegerField()),
                ('model_2013', models.IntegerField()),
                ('model_2012', models.IntegerField()),
                ('model_2011', models.IntegerField()),
                ('model_2010', models.IntegerField()),
            ],
        ),
    ]