# Generated by Django 5.1.4 on 2024-12-27 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_engine', '0002_remove_usuarios_id_alter_usuarios_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='nome_site',
            field=models.CharField(default='', max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nome',
            field=models.CharField(default='', max_length=500),
        ),
    ]