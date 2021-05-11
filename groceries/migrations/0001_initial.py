# Generated by Django 3.2 on 2021-05-11 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('serial', models.CharField(max_length=20)),
                ('value', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('note', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.teacher')),
            ],
            options={
                'verbose_name': '设备',
                'verbose_name_plural': '设备',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('date', models.DateTimeField(verbose_name='Borrow Date')),
                ('tel', models.CharField(max_length=20)),
                ('note', models.CharField(max_length=200)),
                ('back', models.DateTimeField(blank=True, null=True, verbose_name='Return Date')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceries.items')),
            ],
        ),
    ]
