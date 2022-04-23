# Generated by Django 4.0 on 2022-04-23 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('profile_picture', models.ImageField(default='No Image', upload_to='images/profile_pictures/<django.db.models.fields.related.OneToOneField>')),
            ],
        ),
    ]