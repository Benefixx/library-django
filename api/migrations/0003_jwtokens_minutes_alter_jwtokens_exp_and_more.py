# Generated by Django 4.0.5 on 2022-06-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_user_id_jwtokens_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jwtokens',
            name='minutes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='exp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='iat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='jti',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='token',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]