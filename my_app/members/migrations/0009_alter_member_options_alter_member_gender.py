# Generated by Django 5.1.7 on 2025-03-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_alter_member_options_alter_member_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
    ]
