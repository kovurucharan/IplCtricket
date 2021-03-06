# Generated by Django 3.1.7 on 2021-05-17 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_auto_20210517_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playing_matches', models.IntegerField(default=0)),
                ('win', models.IntegerField(default=0)),
                ('loss', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.team')),
            ],
        ),
    ]
