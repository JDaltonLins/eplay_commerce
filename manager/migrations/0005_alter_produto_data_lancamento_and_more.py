# Generated by Django 4.1.3 on 2022-12-05 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_produto_data_lancamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='data_lancamento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Lançamento'),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=100),
        ),
    ]
