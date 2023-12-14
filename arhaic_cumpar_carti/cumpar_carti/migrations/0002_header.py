# Generated by Django 4.2.5 on 2023-12-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cumpar_carti', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.CharField(max_length=150)),
                ('paragraf1', models.TextField()),
                ('paragraf2', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('poza', models.ImageField(null=True, upload_to='static/images')),
            ],
            options={
                'verbose_name': 'Paragraf',
                'verbose_name_plural': 'Paragrafe',
                'db_table': '',
                'managed': True,
            },
        ),
    ]