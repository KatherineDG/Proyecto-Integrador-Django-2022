# Generated by Django 4.1.1 on 2022-12-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='nombre')),
                ('apellido', models.TextField(verbose_name='apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('mensaje', models.TextField(verbose_name='mensaje')),
            ],
            options={
                'verbose_name': 'contacto',
            },
        ),
    ]
