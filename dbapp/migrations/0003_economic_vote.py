# Generated by Django 3.2.3 on 2021-07-20 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0002_remove_economic_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='economic',
            name='vote',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
    ]
