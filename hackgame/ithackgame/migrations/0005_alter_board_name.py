# Generated by Django 5.0.1 on 2024-02-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ithackgame', '0004_comment_parent_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
