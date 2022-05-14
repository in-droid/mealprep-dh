# Generated by Django 4.0.4 on 2022-05-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='calories',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='foods',
            name='protein',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='time',
            field=models.IntegerField(null=True),
        ),
    ]
