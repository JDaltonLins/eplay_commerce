# Generated by Django 4.1.3 on 2022-12-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_rename_categoria_produto_categorias'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuarioconfirmacao',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagem',
            field=models.ImageField(default='static/img/usuarios-default.svg', upload_to='usuarios'),
        ),
    ]
