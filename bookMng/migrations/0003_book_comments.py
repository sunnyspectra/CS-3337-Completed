# Generated by Django 4.2.4 on 2023-11-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comments',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]