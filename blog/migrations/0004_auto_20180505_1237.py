# Generated by Django 2.0.4 on 2018-05-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article1_pub_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article1',
            name='pub_time',
            field=models.DateTimeField(null=True),
        ),
    ]