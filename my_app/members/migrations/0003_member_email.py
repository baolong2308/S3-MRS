# Generated by Django 5.1.7 on 2025-03-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
