# Generated by Django 4.0.4 on 2022-05-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_alter_user_fridge_fid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='calories',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='foods',
            name='protein',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='name',
            field=models.CharField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='time',
            field=models.IntegerField(blank=True),
        ),
    ]
