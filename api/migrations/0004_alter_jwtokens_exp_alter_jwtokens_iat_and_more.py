# Generated by Django 4.0.5 on 2022-06-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_jwtokens_minutes_alter_jwtokens_exp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jwtokens',
            name='exp',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='iat',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='jti',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='token',
            field=models.CharField(blank=True, editable=False, max_length=1000, null=True),
        ),
    ]
