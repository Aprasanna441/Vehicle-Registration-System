# Generated by Django 4.2.3 on 2023-07-12 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredvehicle',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.BigIntegerField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.registeredvehicle')),
            ],
        ),
    ]
