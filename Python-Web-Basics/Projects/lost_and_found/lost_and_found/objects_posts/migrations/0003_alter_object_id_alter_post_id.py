# Generated by Django 4.0 on 2022-04-22 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects_posts', '0002_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
