# Generated by Django 2.0.6 on 2018-06-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180615_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet_text',
            field=models.TextField(max_length=300),
        ),
    ]
