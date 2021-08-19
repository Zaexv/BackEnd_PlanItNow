# Generated by Django 3.1.4 on 2021-08-14 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_userprofile_public_username'),
        ('friendship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_requests_from_user', to='userprofiles.userprofile'),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_requests_to_user', to='userprofiles.userprofile'),
        ),
    ]
