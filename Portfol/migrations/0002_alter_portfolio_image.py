# Generated by Django 4.2 on 2023-05-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='portfolio_images/'),
        ),
    ]
