# Generated by Django 4.1.3 on 2022-12-05 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_produto_slogan_alter_categoria_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='data_lancamento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
