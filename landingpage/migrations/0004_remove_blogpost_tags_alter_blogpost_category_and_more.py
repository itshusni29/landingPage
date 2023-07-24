# Generated by Django 4.2.3 on 2023-07-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='tags',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('tech', 'Technology'), ('food', 'Food'), ('travel', 'Travel'), ('health', 'Health')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(),
        ),
    ]
