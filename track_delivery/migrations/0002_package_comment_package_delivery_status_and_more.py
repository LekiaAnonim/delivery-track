# Generated by Django 4.1.6 on 2023-02-10 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track_delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='delivery_status',
            field=models.CharField(choices=[('s', 'Still at Station'), ('t', 'On Transit'), ('a', 'Arrived in Destination'), ('d', 'Delivered')], default='s', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='arrival_date',
            field=models.DateTimeField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='destination_address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='destination_country',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='owner',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='receive_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='short_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='track_id',
            field=models.CharField(default='El0jiGB8n39Q', max_length=500, unique=True),
        ),
    ]
