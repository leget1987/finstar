# Generated by Django 3.2.13 on 2022-06-24 07:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_receipt', models.IntegerField()),
                ('time_issuance', models.TimeField(default=datetime.time)),
                ('sum_receipt', models.FloatField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finstar_task.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finstar_task.receipt')),
            ],
        ),
    ]