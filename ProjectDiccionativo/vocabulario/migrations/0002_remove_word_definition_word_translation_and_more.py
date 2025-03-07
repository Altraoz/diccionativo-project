# Generated by Django 5.1.6 on 2025-02-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='definition',
        ),
        migrations.AddField(
            model_name='word',
            name='translation',
            field=models.CharField(default='Sin traducción', help_text='Traducción de la palabra', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='word',
            name='example',
            field=models.TextField(blank=True, help_text='Ejemplo de uso de la palabra', null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='language',
            field=models.CharField(help_text='Nombre de la lengua indígena', max_length=50),
        ),
        migrations.AlterField(
            model_name='word',
            name='term',
            field=models.CharField(help_text='La palabra en la lengua indígena', max_length=100),
        ),
    ]
