# Generated by Django 4.1.6 on 2023-06-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track_delivery', '0007_remove_package_receive_date_alter_package_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='owner',
            new_name='receiver',
        ),
        migrations.AddField(
            model_name='package',
            name='sender',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='track_id',
            field=models.CharField(default='586139073867', max_length=500, unique=True),
        ),
    ]