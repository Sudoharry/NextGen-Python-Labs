# Generated by Django 5.1.7 on 2025-03-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_attachement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='attachement',
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=122),
        ),
    ]
